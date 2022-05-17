from turtle import home
from picamera import PiCamera
import time
import os
import RPi.GPIO as GPIO
if os.path.isfile("/home/pi/Desktop/PIcamera/pictures")== True:
    os.mkdir("/home/pi/Desktop/PIcamera/pictures")
camera=PiCamera()
camera.resolution = (1280,720)
camera.rotation = 180
suff=0
while os.path.isfile("/home/pi/Desktop/PIcamera/pictures/image_"+str(suff)+".jpg")== True:
    suff+=1
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
