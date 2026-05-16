import cv2
import numpy as np

img = np.full((500, 500, 3), (166, 98, 83), dtype="uint8")
points = np.array([[250, 100], [100, 400], [400, 400]])
points = points.reshape((-1, 1, 2))
cv2.fillPoly(img, [points], (0, 255, 0))

points = np.array([[250, 80], [100, 200], [150, 400], [350, 400], [400, 200]])
points = points.reshape((-1, 1, 2))
cv2.fillPoly(img, [points], (255, 0, 255))

points = np.array([[250, 100], [100, 250], [250, 400], [400, 250]])
points = points.reshape((-1, 1, 2))
cv2.fillPoly(img, [points], (255, 255, 0))

cv2.arrowedLine(img, (50, 250), (450, 250), (0, 255, 255), 5)

cv2.imshow("extra shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()