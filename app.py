#!/usr/bin/env python
from importlib import import_module
import time

import os
from flask import Flask, render_template, Response, request, send_file

# import camera driver. Otherwise use pi camera by default
if os.environ.get('CAMERA'):
    Camera = import_module('camera_' + os.environ['CAMERA']).Camera
else:
    from camera_pi import Camera

import utils

app = Flask(__name__)


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/capture_image', methods=['GET', 'POST'])
def capture_image():
    utils.write_boolean_to_file("camera_state", False)

    filename = request.form.get('filename')
    arguments = request.form.get('arguments')

    cmd = f"raspistill --nopreview -t 1 -o {filename} {arguments}"
    print(cmd)

    retcode = os.system(cmd)

    print("Return code: %d"%retcode)
    if retcode == 0:
        return send_file(filename, mimetype='image/jpg')
    else:
        return "Error"

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
