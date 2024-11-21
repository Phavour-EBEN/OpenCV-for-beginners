import cv2 as cv
import numpy as np

img = cv.imread('photos\photo_5785046641491951809_y.jpg')
# rescale the image
def rescale(image, scale=0.5):
    width = int(image.shape[1] * scale)
    height = int(image.shape[0] * scale)
    dimensions = (width, height)
    resized_img = cv.resize(image, dimensions, interpolation=cv.INTER_AREA)
    return resized_img
image = rescale(img)
cv.imshow('image',image)

# Convert the image to grayscale
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# reading in the haarcasde file
haar_cascade = cv.CascadeClassifier('haarcascade_frontalface_default (1).xml')
face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
print(f'Number of faces found is: {len(face_rect)}')

for (x, y, w, h) in face_rect:
    cv.rectangle(image, (x,y), (x+w, y+h), (0,255,0),  2)
cv.imshow('detected face', image)

cv.waitKey(0)