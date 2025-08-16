from picamera2 import Picamera2, Preview
import time

picam2 = Picamera2()
config = picam2.create_preview_configuration(main={"size": (1296,972)},
                                             sensor={'output_size': camera_config['main']['size']} )

picam2.configure(config)
picam2.start_preview(Preview.QTGL)
picam2.start()
time.sleep(2)