from picamera2 import Picamera2, Preview
from libcamera import controls
import time

picam2 = Picamera2()

# Set main capture and preview to high resolution
config = picam2.create_preview_configuration(
    main={"size": (4608, 2592)},   # Full resolution for capture
    lores={"size": (1920, 1080)}   # Higher-res preview (instead of tiny default)
)
picam2.configure(config)

# Enable continuous autofocus
picam2.set_controls({"AfMode": controls.AfModeEnum.Continuous})

picam2.start_preview(Preview.QTGL)
picam2.start()

try:
    while True:
        af_state = picam2.get_controls().get("AfState", None)
        print(f"Autofocus state: {af_state}")
        time.sleep(1)
except KeyboardInterrupt:
    picam2.stop()
