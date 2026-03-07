import cv2
import os

img = cv2.imread("pika.jpg", cv2.IMREAD_COLOR)
cv2.imshow("pikachu image", img)

img2 = cv2.imread("pika.jpg", 0)
cv2.imshow("pikachu in grayscale", img2)

saved_directory = r"C:\Users\ASUS\Documents\openCV"
os.chdir(saved_directory)
cv2.imwrite("pikaBandW.jpg", img2)
print("Saved successfully")

cv2.waitKey(0)
cv2.destroyAllWindows()