from picamera import PiCamera
import time
camera=PiCamera()
camera.resolution = (1280,720)
camera.rotation = 180
time.sleep(2)
file_name_1="image.jpg"
camera.capture(file_name_1)
print("pic taken")
time.sleep(1)
file_name_2="vid.h264"
camera.start_recording(file_name_2)
camera.wait_recording(5)
camera.stop_recording()

print("vid taken")

#comment
