from picamera import PiCamera
import time
camera=PiCamera()
camera.resolution = (1280,720)
camera.rotation = 180
time.sleep(2)
file_name="image.jpg"
camera.capture(file_name)
print("Done. ")
#comment
