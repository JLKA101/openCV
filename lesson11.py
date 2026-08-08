import cv2
import numpy as np
import time

print("OpenCV version:", cv2.__version__)

capture_video = cv2.VideoCapture("masking.mp4")

time.sleep(0.5)

width = int(capture_video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture_video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(capture_video.get(cv2.CAP_PROP_FPS))

if fps == 0:
    fps = 30

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(
    "Invisible_Box_Output.avi",
    fourcc,
    fps,
    (width, height)
)

background = None
for i in range(60): #first sixty frames will be captured
    ret, background = capture_video.read()
    if not ret:
        continue

background = np.flip(background, axis=1) #flip horizontally

delay = 1
frame_count = 0

while capture_video.isOpened():
    ret, img = capture_video.read()

    if not ret:
        break

    frame_count += 1

    img = np.flip(img, axis=1)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)

    lower_red2 = np.array([160, 120, 70])
    upper_red2 = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    mask = mask1 + mask2

    kernel = np.ones((3, 3), np.uint8)

