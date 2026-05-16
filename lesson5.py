import cv2
import numpy as np

img = np.zeros((500, 500, 3), dtype="uint8") ##all pixels converted to 0s -> blank black img, 3 shows num colour channels, uint8 - unassigned integer of 8 bits, otherwise would give us decimals which would not present a colour
cv2.circle(img, (350,  200), 80, (0, 0, 255), -1) #-1 fills shape
cv2.imshow("circle image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()