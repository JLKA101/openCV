import cv2
import numpy as np

### adding identical images

img1 = cv2.imread("bts2.png")
img2 = cv2.imread("bts3.png")
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

weightedSum = cv2.addWeighted(img1, 0.5, img2, 0.4, 0) #0.5 means each pixel of img1 will be multiplied by 0.5, 0 means no extra brightness
cv2.imshow("weighted image", weightedSum)
cv2.waitKey(0)
cv2.destroyAllWindows()

### subtracting identical images

img1 = cv2.imread("bts2.png")
img2 = cv2.imread("bts3.png")
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

sub = cv2.subtract(img1, img2)
cv2.imshow("subtracted image", sub)
cv2.waitKey(0)
cv2.destroyAllWindows()

### erosion
imgog = cv2.imread("bts2.png", 1)
img = cv2.resize(imgog, (368, 552), 1)
kernel = np.ones((3, 7), np.uint8) #5, 5 means matrix is 5x5
eroded_img = cv2.erode(img, kernel)

cv2.imshow("eroded image", eroded_img)
cv2.waitKey(0)
cv2.destroyAllWindows()