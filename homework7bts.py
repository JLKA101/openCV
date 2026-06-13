import cv2
import numpy as np

img = cv2.imread("tae2.png")
if img is None:
    print("Image not found")
    exit()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_,thresh = cv2.threshold(gray, 190, 255, cv2.THRESH_BINARY_INV) #pixels darker than 190 become white, pixels lighter than 190 become black #THRESH_BINARY_INV is used because simple blob detector usually detects white blobs on a black background
params = cv2.SimpleBlobDetector_Params()
#filter by area
params.filterByArea = True
params.minArea = 2000
params.maxArea = 200000

#filter by colour (colour-specific blobs)
params.filterByColor = True
params.blobColor = 255 #detect white blobs

#turn off shape restrictions (coz they are blobs)
params.filterByCircularity = False
params.filterByConvexity = False
params.filterByInertia = False

detector = cv2.SimpleBlobDetector_create(params)

#detect blobs
keypoints = detector.detect(thresh) #threshold image
print ("Detected blobs: ", len(keypoints))

#draw circles around detected blobs
output = cv2.drawKeypoints(
    img,
    keypoints,
    None,
    (0, 0, 255),
    cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS #around blobs
) #keypoints = detected blobs

#cv2.namedWindow("Blob Detection", cv2.WINDOW_NORMAL) #output window can be resized
cv2.imshow("Blob Detection", output)
cv2.waitKey(0)
cv2.destroyAllWindows()