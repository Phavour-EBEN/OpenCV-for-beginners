import cv2 as cv
import numpy as np

img = cv.imread('photos\photo_5878501912922403677_x.jpg')
cv.imshow("Image", img)

# Cropping function
crop_img = img[50:250, 0:250]
cv.imshow("Cropped Image", crop_img)

# Transformation
def img_tranformatioN(img, x, y):
    matrix = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    translate = cv.warpAffine(img, matrix, dimensions)

    return translate
'''
note: 
-x--left
x---right
-y--up
y---down
'''
trans_img = img_tranformatioN(img, -250,250)
cv.imshow("Translated Image", trans_img)

# rotation

def rotate(img, angle, rotPoint=None):
    if rotPoint is None:
        rotPoint = (img.shape[1]//2, img.shape[0]//2)

    coordinate = (img.shape[1], img.shape[0])
    matrix = cv.getRotationMatrix2D(rotPoint, angle, 1)

    return cv.warpAffine(img, matrix, coordinate)

rotated_img = rotate(img, 45)
cv.imshow("Rotated Image", rotated_img) 


cv.waitKey(0)