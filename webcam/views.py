from django.shortcuts import render
from django.http import StreamingHttpResponse
from .stream import CameraStream

# RTSP camera link
RTSP_SOURCE = 'rtsp://admin:adminCAFWOK@1.54.171.178:60961/Streaming/Channels/102/'

def get_frame():
    # Get capture from webcam or rtsp camera link
    cap = CameraStream(RTSP_SOURCE)
    cap.start()
    while cap:
        # Get frame from capture
        frame = cap.read()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


def live_stream(request):
    """ Video streaming route """
    return StreamingHttpResponse(get_frame(), content_type='multipart/x-mixed-replace; boundary=frame')


def index(request):
    """ Home page view """
    return render(request, template_name='webcam/index.html')
