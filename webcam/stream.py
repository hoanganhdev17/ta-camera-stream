from threading import Thread
import cv2


class CameraStream(object):
    thread = None
    stream = None

    def __init__(self, source=0):
        # Get capture from source camera
        self.stream = cv2.VideoCapture(source)
        self.grabbed, self.frame = self.stream.read()

    def start(self):
        self.thread = Thread(target=self.update, args=())
        self.thread.start()

    def update(self):
        while True:
            self.grabbed, self.frame = self.stream.read()

    def read(self):
        frame = self.frame.copy()
        # Convert frame to jpeg
        ret, jpeg = cv2.imencode('.jpg', frame)
        # Convert the image to bytes and return
        return jpeg.tobytes()

    def stop(self):
        self.thread.join()

    def __exit__(self):
        self.stream.release()