import cv2
import os

imgog = cv2.imread("bts2.png", 1)
img = cv2.resize(imgog, (368, 552))
B, G, R = cv2.split(img)
cv2.imshow("original", img)
cv2.waitKey(0)

cv2.imshow("blue saturation image", B)
cv2.imwrite("bluebts2.png", B)
cv2.waitKey(0)

cv2.imshow("green saturation image", G)
cv2.imwrite("greenbts2.png", G)
cv2.waitKey(0)

cv2.imshow("red saturation image", R)
cv2.imwrite("redbts.png", R)
cv2.waitKey(0)

save_dir = "C:/Users/ASUS/Documents/openCV"
os.chdir(save_dir)
cv2.imwrite("redsatbts.png", R)

cv2.destroyAllWindows()