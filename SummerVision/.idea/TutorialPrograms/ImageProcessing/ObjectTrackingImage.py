import cv2
import numpy

image = cv2.imread("C:\\Users\\josep\\Desktop\\Programming\\OpenCV\\Opentcv Test Media\\stimage1.jpg", 1)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_yellow = np.array([0, 41, 95])
upper_yellow = np.array([17, 68, 85])

mask = cv2.inRange(hsv,lower_yellow, upper_yellow)

cv2.imshow("Image", image)
cv2.imshow("Mask", mask)

while(1):
  k = cv2.waitKey(0)
  if(k == 27):
    break

cv2.destroyAllWindows()