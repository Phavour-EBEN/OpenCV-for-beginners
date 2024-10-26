import cv2 as cv
import numpy as np

# converting BGR to Graycale

img = cv.imread('photos\photo_5782648610926740550_y.jpg')
cv.imshow("image", img)

# resizing
def resized_frame(frame, scale=0.7):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    resized = cv.resize(frame, dimensions,interpolation=cv.INTER_AREA)
    return resized

# converting to gray
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray_img = resized_frame(gray_img)
cv.imshow("gray", gray_img)

# Blurrig and image
blur_img = cv.blur(img, (5,5), cv.BORDER_DEFAULT)
blur_img = resized_frame(blur_img)
cv.imshow("blur", blur_img)

# finding the edges//edge cascade
edges = cv.Canny(img, 125,100)
edges = resized_frame(edges)
cv.imshow("edges", edges)

# Dilate and Erode
dilated_img = cv.dilate(edges, (7,7),iterations=3)
dilated_img = resized_frame(dilated_img)
cv.imshow("dilated", dilated_img)

eroded_img = cv.erode(edges, (7,7), iterations=3)
eroded_img = resized_frame(eroded_img)
cv.imshow("eroded", eroded_img)



cv.waitKey(0)
