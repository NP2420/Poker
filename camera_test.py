from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2 as cv

IM_WIDTH = 1280
IM_HEIGHT = 720

# Initialize PiCamera and grab reference to the raw capture
camera = PiCamera()
camera.resolution = (IM_WIDTH,IM_HEIGHT)
camera.framerate = 10
rawCapture = PiRGBArray(camera, size=(IM_WIDTH,IM_HEIGHT))

rawCapture.truncate(0)
# Press 'p' to take a picture
for frame in camera.capture_continuous(rawCapture, format="bgr",use_video_port=True):

    image = frame.array
    cv.imshow("Card",image)
    key = cv.waitKey(1) & 0xFF
    if key == ord("p"):
        break

    rawCapture.truncate(0)