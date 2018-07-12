import cv2

imageRGB = cv2.imread("C:\\Users\\josep\\Downloads\\spot.jpg")

HSV = cv2.cvtColor(imageRGB, cv2.COLOR_BGR2HSV)

cv2.imshow("Image", imageRGB)
cv2.imshow("HSV", HSV)

cv2.waitKey(0)
