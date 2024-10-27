import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

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

blank = np.zeros(image.shape[:2],dtype='uint8')
'''
#grayed the image
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)
'''
circle = cv.circle(blank,(image.shape[1]//2+210,image.shape[0]//2-60),(130),(255),-1)
# cv.imshow('circle',circle)

mask_img = cv.bitwise_and(image,image,mask=circle)
cv.imshow('mask',mask_img)
'''
mask = cv.bitwise_and(gray,gray,mask=circle)
cv.imshow('mask',mask)
'''
'''
# gray_scale hist
gray_hist = cv.calcHist([gray],[0],mask,[256],[0,256])
plt.figure(figsize=(7,7))
plt.title('graycale histogram')
plt.xlabel('bins')
plt.ylabel('number of pixels')
plt.plot(gray_hist)
plt.show()
'''

# color-hist
plt.figure(figsize=(7,7))
plt.title('colored histogram')
plt.xlabel('bins')
plt.ylabel('number of pixels')
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([image],[i],circle,[256],[0,256])
    plt.plot(hist, color=col)
    
plt.show()

cv.waitKey(0)