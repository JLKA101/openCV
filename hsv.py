import cv2

img = cv2.imread("bts.png", cv2.IMREAD_COLOR)

if img is None:
    print("Image not found")

else:
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imshow("original", img)
    cv2.waitKey(0)
    cv2.imshow("hsv image", hsv_img) #hue saturation values
    cv2.waitKey(0)
    cv2.destroyAllWindows()