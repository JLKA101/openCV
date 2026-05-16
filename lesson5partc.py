import cv2
import numpy as np

img = np.ones((500, 500, 3), dtype="uint8")*255 #*255 makes the ones change to 255

img = cv2.rectangle(img, (200, 100), (300, 415), (66, 66, 66), -1)
cv2.circle(img, (250,  165), 40, (0, 0, 255), -1)
cv2.circle(img, (250,  255), 40, (26, 213, 255), -1)
cv2.circle(img, (250,  345), 40, (196, 217, 9), -1)


cv2.imshow("traffic light", img)
cv2.waitKey(0)
cv2.destroyAllWindows()