# from picamera2 import Picamera2
# import cv2

# picam2 = Picamera2()
# picam2.preview_configuration.main.size = (640, 480)
# picam2.preview_configuration.main.format = "RGB888"
# picam2.configure("preview")
# picam2.start()

# frame = picam2.capture_array()
# cv2.imshow("Camera", frame)
# cv2.waitKey(0)

from picamera2 import Picamera2, Preview
from libcamera import Transform
picam2 = Picamera2()
picam2.start_preview(Preview.QTGL, x=100, y=200, width=800, height=600,
transform=Transform(hflip=1))
picam2.start()