import cv2

#Identifies and reads image info
image = cv2.imread("C:\\Users\\josep\\Downloads\\spot.jpg")

#Converts image to grayscale
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Saves new grayscale image, and gives it a new name
cv2.imwrite("C:\\Users\\josep\\Downloads\\grayspot.jpg", grayImage)

#Creates windows to display images
cv2.namedWindow("image", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("gray image", cv2.WINDOW_NORMAL)

#Names windows
cv2.imshow("image", image)
cv2.imshow("gray image", grayImage)

cv2.waitKey(0)

#HELL YEAH!