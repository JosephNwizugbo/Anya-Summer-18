import cv2

image = cv2.imread("spotmini.jpg")

grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite("grayspot.jpg", grayImage)

cv2.namedWindow("image", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("gray image", cv2.WINDOW_NORMAL)

cv2.imshow("image", image)
cv2.imshow("gray image", grayImage)

cv2.waitKey(0)