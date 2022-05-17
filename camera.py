from turtle import home
from picamera import PiCamera
import time
import os, sys
import RPi.GPIO as GPIO
os.mkdir(/home/pi/Desktop/PIcamera/pictures, 0755);
camera=PiCamera()
camera.resolution = (1280,720)
camera.rotation = 180
suff=0
time.sleep(2)
try :
    while True:
        file_name="image"+suff+".jpg"
        camera.capture(file_name)
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
