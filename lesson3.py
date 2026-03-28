import cv2
import numpy as np

### adding identical images

img1 = cv2.imread("beachai.png")
img2 = cv2.imread("beachgirlai.png")

weightedSum = cv2.addWeighted(img1, 0.5, img2, 0.4, 0) #0.5 means each pixel of img1 will be multiplied by 0.5, 0 means no extra brightness
cv2.imshow("weighted image", weightedSum)
cv2.waitKey(0)
cv2.destroyAllWindows()

### subtracting identical images

img1 = cv2.imread("beachai.png")
img2 = cv2.imread("beachgirlai.png")

sub = cv2.subtract(img1, img2)
cv2.imshow("subtracted image", sub)
cv2.waitKey(0)
cv2.destroyAllWindows()