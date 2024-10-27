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

#grayed the image 
gray_img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow("grayed", gray_img)

# edge detecton
edges = cv.Canny(gray_img,100,200)
cv.imshow("edges", edges)

blur = cv.GaussianBlur(edges, (7,7),cv.BORDER_DEFAULT)

# Threshold
ret, thresh = cv.threshold(gray_img, 125,255, cv.THRESH_BINARY)
cv.imshow('threh', thresh)

# fing the contours
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(len(contours))
# blank img
blank = np.zeros(image.shape, dtype='uint8')
cv.imshow("blank", blank)

# drawing contours
contours_drawn = cv.drawContours(blank, contours, -1, (0,0,225), 1)
cv.imshow("contours", contours_drawn)


cv.waitKey(0)