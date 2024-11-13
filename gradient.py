import cv2 as cv
import numpy as np

image = cv.imread('photos\photo_5878501912922403677_x.jpg')

def resize(image, scale=0.5):
    width = int(image.shape[1]* scale)
    height = int(image.shape[0]* scale)

    dimensions  = (width, height)
    resized_img = cv.resize(image, dimensions,interpolation=cv.INTER_AREA)
    return resized_img

resized_image = resize(image)
cv.imshow('image', resized_image)

# converting to gray scale
gray = cv.cvtColor(resized_image, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# laplacian transformation(edge detection)pencil format
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('laplacian', lap, )

# sobel detection
sobelx = cv.Sobel(gray, cv.CV_64F, 1,0)
sobely = cv.Sobel(gray, cv.CV_64F, 0,1)
combine_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow("sobel", combine_sobel)

canny = cv.Canny(gray, 100,200)
cv.imshow("canny", canny)

cv.waitKey(0)