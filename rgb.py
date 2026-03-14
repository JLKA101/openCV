import cv2

img = cv2.imread("bts.png", 1) # 1 = color, 0 = grayscale
B, G, R = cv2.split(img) # splitting the colour channels
cv2.imshow("original", img)
cv2.waitKey(0)

cv2.imshow("blue saturation image", B) # blue channel
cv2.imwrite("bluebts.png", B)
cv2.waitKey(0)

cv2.imshow("green saturation image", G) # green channel
cv2.imwrite("greenbts.png", G)
cv2.waitKey(0)

cv2.imshow("red saturation image", R) # red channel
cv2.imwrite("redbts.png", R)
cv2.waitKey(0)

cv2.destroyAllWindows()