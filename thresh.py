import cv2 as cv
import numpy as np

img = cv.imread('photos/pexels-ron-lach-9034670.jpg')

# resized function
def resize_frame(img, scale=0.1):
    width = int(img.shape[1]*scale)
    height = int(img.shape[0]*scale)

    dimensions = (width, height)
    resized_img = cv.resize(img, dimensions, interpolation=cv.INTER_AREA)
    return resized_img
image = resize_frame(img)
cv.imshow('img',image)

# grayscaled
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY, cv.BORDER_DEFAULT)
cv.imshow('gray', gray)

# thresh
threshold, thresh = cv.threshold(gray, 150.0, 255.0, cv.THRESH_BINARY)
cv.imshow('thresh', thresh)
print(f"threshold: ", {threshold})

threshold_inv, thresh_inv = cv.threshold(gray, 150.0, 255.0, cv.THRESH_BINARY_INV)
cv.imshow('thresh_inv', thresh_inv)
print(f"threshold: ", {threshold_inv})

# Adaptive threshold
Adaptive_threh = cv.adaptiveThreshold(gray, 150, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11,5)
cv.imshow("Adative thresh", Adaptive_threh)

cv.waitKey(0)