import cv2
import numpy as np

img = cv2.imread("bts3.png")
cv2.imshow("original image", img)
cv2.waitKey(0)

#gaussian
gaussian = cv2.GaussianBlur(img, (7, 7), 0) #0 removes the extra brightness
cv2.imshow("gaussian blur", gaussian)
cv2.waitKey(0)

#median (removes salt and pepper noise)
median = cv2.medianBlur(img, 5)
cv2.imshow("median blur", median)
cv2.waitKey(0) 

#bilateral (reduces noise but keeps sharp edges)
bilateral = cv2.bilateralFilter(img, 9, 75, 75) #9 = diameter of pixel area (bigger the value, the smoother the img). First 75 contols how much colour difference allowed (bigger the value, the more blended the colours). Second 75 is 'sigma space', controls how far the pixels can influence each other based on the distance (the higher the value, the further away the pixels will be affected by the filter)
cv2.imshow("bilateral filter", bilateral)
cv2.waitKey(0) 

#bordered image
borderedimg = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=(255, 0, 0))
cv2.imshow("bordered img", borderedimg)
cv2.waitKey(0) 

borderedimg2 = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REFLECT)
cv2.imshow("bordered img 2", borderedimg2)
cv2.waitKey(0) 

borderedimg3 = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REFLECT101)
cv2.imshow("bordered img 3", borderedimg3)
cv2.waitKey(0) 

cv2.destroyAllWindows()