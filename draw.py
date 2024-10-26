import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('blank', blank)

# adding colors to yhe blank screen
# blank[:] = 255,0,0
# cv.imshow('blank-green', blank)

# drawing a rectangle on the plane
cv.rectangle(blank, (0,0), (250,250),(0,255,0), thickness=2)
cv.imshow('rectangle', blank)

cv.waitKey(0)