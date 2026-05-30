import cv2
import numpy as np

img = cv2.imread("btsyaya.png")
cv2.imshow("original image", img)
cv2.waitKey(0)

#gaussian
gaussian = cv2.GaussianBlur(img, (7, 7), 0)
cv2.imshow("gaussian blur", gaussian)
cv2.waitKey(0)

median = cv2.medianBlur(img, 5)
cv2.imshow("median blur", median)
cv2.waitKey(0) 

bilateral = cv2.bilateralFilter(img, 9, 75, 75)
cv2.imshow("bilateral filter", bilateral)
cv2.waitKey(0) 

cv2.destroyAllWindows()