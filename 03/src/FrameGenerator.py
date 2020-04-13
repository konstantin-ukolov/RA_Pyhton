import cv2
import time
import sys


class FrameGenerator(object):
    def __init__(self, fps=25):
        self._fps = fps
        self._capture = cv2.VideoCapture(0)

    def __iter__(self):
        return self

    def __next__(self):
        time.sleep(1 / float(self._fps))
        success, data = self._capture.read()

        if success:
            ret, jpeg = cv2.imencode('.jpg', data)
            return jpeg.tobytes()
        else:
            print("Can't read capture")
            sys.exit(1)


if __name__ == '__main__':
    frame_generator = FrameGenerator(fps=12)

    for index, frame in enumerate(frame_generator):
        with open('frames/frame_{0}.jpg'.format(index), 'wb') as f:
            f.write(frame)
