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

cv.waitKey(0)