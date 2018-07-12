import cv2
import numpy

cap = cv2.VideoCapture(0)

while(1):
    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    lower_orange = numpy.array([0, 41, 95])
    upper_orange = numpy.array([17, 68, 85])

    mask = cv2.inRange(hsv, lower_orange, upper_orange)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("res", res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()