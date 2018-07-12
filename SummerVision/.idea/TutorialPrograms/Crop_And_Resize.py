import cv2

image = cv2.imread("C:\\Users\\josep\\Downloads\\spot.jpg")

#Scaling variables used in "ScaleDown" and "ScaleUp"
scaleX = .6
scaleY = .6

#Scaled images
ScaleDown = cv2.resize(image, None, fx=scaleX, fy=scaleY, interpolation= cv2.INTER_LINEAR)
ScaleUp = cv2.resize(image, None, fx=scaleX*3, fy=scaleY*3, interpolation= cv2.INTER_LINEAR)

#Cropped images - numbers are pixels
crop = image[50:150, 20:120]

cv2.imshow("Original", image)
cv2.imshow("Scaled Down", ScaleDown)
cv2.imshow("Scaled Up", ScaleUp)
cv2.imshow("Cropped", crop)

cv2.waitKey(0)

#HELL YEAH!