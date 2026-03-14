import cv2
import os

img = cv2.imread("bts.png", cv2.IMREAD_COLOR)
cv2.imshow("bts colour", img)

img2 = cv2.imread("bts.png", 0)
cv2.imshow("bts B&W", img2)

saved_directory = r"C:\Users\ASUS\Documents\openCV"
os.chdir(saved_directory)
cv2.imwrite("btsbw.jpg", img2)
print("Saved successfully")

cv2.waitKey(0)
cv2.destroyAllWindows()