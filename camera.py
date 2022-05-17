from picamera import PIcamera
import time
camera=PIcamera()
camera.resolution = (1280,720)
camera.rotation = 180
time.sleep(2)
file_name="/home/pi/Desktop/camera/image.jpg"
camera.capture(file_name)
print("Done. ")
