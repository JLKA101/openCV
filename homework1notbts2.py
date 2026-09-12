import cv2
import numpy as np
import time

print("OpenCV version:", cv2.__version__)

capture_video = cv2.VideoCapture("darkpinkmasking.mp4")

time.sleep(0.5)

width = int(capture_video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture_video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(capture_video.get(cv2.CAP_PROP_FPS))

if fps == 0:
    fps = 30

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(
    "Invisible_Pillow_Output.avi",
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

    lower_red1 = np.array([145, 80, 70])#lighter shade hsv HW
    upper_red1 = np.array([160, 255, 255])#
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)

    lower_red2 = np.array([161, 80, 70])#darker shade hsv HW
    upper_red2 = np.array([179, 255, 255])#
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    mask = mask1 + mask2

    kernel = np.ones((3, 3), np.uint8)

    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel) #morphology removes leftover noise
    #dilation, enlarges detected red area
    mask = cv2.dilate(mask, kernel)
    #inversion red-> black, non-red -> white
    mask_inv = cv2.bitwise_not(mask)
    #red -> bg
    res1 = cv2.bitwise_and(background, background, mask=mask)
    #non-red are not visible in current frame:
    res2 = cv2.bitwise_and(img, img, mask=mask_inv)
    final_output = cv2.add(res1, res2)
    cv2.imshow("Invisible Cloak Effect", final_output)
    out.write(final_output) # saves output vid
    key = cv2.waitKey(delay)&0xFF #escape key
    if key == 27:
        break
    #ext window manually by clicking X:
    if cv2.getWindowProperty("Invisible Cloak Effect", cv2.WND_PROP_VISIBLE) < 1:
        break

capture_video.release()
out.release() # save output
cv2.destroyAllWindows()