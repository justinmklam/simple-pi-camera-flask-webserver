# Simple Raspberry Pi Camera Webserver

Simple Flask-based webserver to show the camera video stream and enable image capture.

## Context

When a Raspberry Pi is setup in headless mode, it's troublesome to view the camera stream and take pictures through an SSH session. Using this webserver, you can view the camera stream through your web browser. When an image is captured, it's served to the client's browser and can then easily be saved to the client's desktop.

## Acknowledgements

Thanks to Miguel Grinberg for doing all the legwork in implementing the streaming functionality ([original](http://blog.miguelgrinberg.com/post/video-streaming-with-flask) and its [follow-up](http://blog.miguelgrinberg.com/post/flask-video-streaming-revisited) post).
