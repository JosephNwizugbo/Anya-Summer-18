import cv2
import math

image = cv2.imread("C:\\Users\\josep\\Downloads\\spot.jpg")

#Lists to store points
center = []
circumfrence = []

def drawCircle(action, x, y, flags, userdata):
    global center, circumfrence
    if action == cv2.EVENT_LBUTTONDOWN:
        center = [(x, y)]
        #**WIP**: radius = math.sqrt(math.pow(center[0][0]-circumfrence[0][0],2) + math.pow(center[0[1]-circumfrence[0][1], 2)}