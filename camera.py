from turtle import home
from picamera import PiCamera
import time
import os
import RPi.GPIO as GPIO
if not os.path.exists("/home/pi/Desktop/PIcamera/pictures"):
    os.mkdir("/home/pi/Desktop/PIcamera/pictures")
camera=PiCamera()
camera.resolution = (1280,720)
camera.rotation = 180
suff=0
for path in os.listdir("/home/pi/Desktop/PIcamera/pictures"):
    # check if current path is a file
    if os.path.isfile(os.path.join("/home/pi/Desktop/PIcamera/pictures", path)):
        suff += 1
    print("images that exists: image_"+str(suff)+".jpg")
suff+=1
print("continuing from image_"+str(suff)+".jpg")
time.sleep(2)
try :
    while True:
        file_name="/home/pi/Desktop/PIcamera/pictures/"+"image_"+str(suff)+".jpg"
        print(file_name +" to be taken")
        camera.capture(file_name)
        print(file_name +" taken")
        suff+=1
        time.sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup
        

""" file_name_1="image.jpg"
camera.capture(file_name_1)
print("pic taken")
time.sleep(1)
file_name_2="vid.h264"
camera.start_recording(file_name_2)
camera.wait_recording(5)
camera.stop_recording()

print("vid taken")
 """
#comment
