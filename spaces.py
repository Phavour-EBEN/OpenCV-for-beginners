import cv2 as cv
import numpy as np

image = cv.imread('photos\photo_5785046641491951809_y.jpg')

# resized function
def resize_frame(img, scale=0.7):
    width = int(img.shape[1]*scale)
    height = int(img.shape[0]*scale)

    dimensions = (width, height)
    resized_img = cv.resize(img, dimensions, interpolation=cv.INTER_AREA)
    return resized_img
image = resize_frame(image)
cv.imshow('img',image)

# converting to gray-scale
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('grayed', gray) 

# converting to HSV
HSV = cv.cvtColor(image, cv.COLOR_BGR2HSV)
cv.imshow("hsv", HSV)
# BGR TO LAB
LAB = cv.cvtColor(image, cv.COLOR_BGR2LAB)
cv.imshow("LAB", LAB)
# BGR2RGB
RGB = cv.cvtColor(image, cv.COLOR_BGR2RGB)
cv.imshow("RGB", RGB)


cv.waitKey(0)