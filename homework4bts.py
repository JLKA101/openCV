import cv2
import numpy as np

img1 = cv2.imread("tae.png")
img2 = cv2.imread("luvbts.png")

wSum = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)
cv2.imshow("weighted image", wSum)
cv2.waitKey(0)


imgog = cv2.imread("tae.png", 1)
kernel = np.ones((3, 7), np.uint8) #5, 5 means matrix is 5x5
eroded_img = cv2.erode(imgog, kernel)

cv2.imshow("eroded image", eroded_img)
cv2.waitKey(0)


cv2.destroyAllWindows()