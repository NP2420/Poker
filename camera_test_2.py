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

from picamera2 import Picamera2
from libcamera import controls
import time

picam2 = Picamera2()

# Configure for preview
config = picam2.create_preview_configuration()
picam2.configure(config)

# Start camera with preview
picam2.start(show_preview=True)

# Enable continuous autofocus
picam2.set_controls({"AfMode": controls.AfModeEnum.Auto})

time.sleep(10)  # Keep it running for 10 seconds before exit
