import cv2 as cv
import numpy as np

image = cv.imread('photos/photo_5782648610926740550_y.jpg')

# resized function
def resize_frame(img, scale=0.7):
    width = int(img.shape[1]*scale)
    height = int(img.shape[0]*scale)

    dimensions = (width, height)
    resized_img = cv.resize(img, dimensions, interpolation=cv.INTER_AREA)
    return resized_img
image = resize_frame(image)
cv.imshow('img',image)

b,g,r = cv.split(image)
cv.imshow('b',b)
cv.imshow('g',g)
cv.imshow('r', r)

merged = cv.merge([b,g,r])
cv.imshow('merged', merged)

# getting the actual b,g,r
blank = np.zeros(image.shape[:2], 'uint8')

b_merged = cv.merge([b,blank,blank])
cv.imshow('col_merged', b_merged)

g_merge = cv.merge([blank,g,blank])
cv.imshow('g_merge',g_merge)

r_merge = cv.merge([blank,blank,r])
cv.imshow('r_merge',r_merge)

cv.waitKey(0)