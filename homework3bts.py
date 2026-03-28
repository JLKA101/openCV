import cv2

imgog = cv2.imread("bts3.png", 1)
img = cv2.resize(imgog, (329, 590))

if img is None:
    print("Image not found")

else:
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imshow("original", img)
    cv2.waitKey(0)
    cv2.imshow("hsv image", hsv_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()