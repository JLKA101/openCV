import cv2
import numpy as np

imgog = cv2.imread("tae.png")
img = cv2.resize(imgog, (600, 600))
img = cv2.putText(img, "BTS", (50, 80), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 137, 207), 3)
cv2.imshow("bts text", img)
cv2.waitKey(0)
cv2.destroyAllWindows()