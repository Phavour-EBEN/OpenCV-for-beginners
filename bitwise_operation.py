import cv2 as cv
import numpy as np

blank = np.zeros((500,500), 'uint8')

rec = cv.rectangle(blank.copy(), (25,25), (475,475), 255,-1)
circle = cv.circle(blank.copy(), (250,250),(250),(255),-1)
cv.imshow('rec',rec)
cv.imshow('cir',circle)

# bitwise operations
bitwise_and  = cv.bitwise_and(rec,circle)
cv.imshow("bitwise_and", bitwise_and)

bitwise_or = cv.bitwise_or(rec,circle)
cv.imshow('bitwise_or', bitwise_or)

bitwise_xor = cv.bitwise_xor(rec,circle)
cv.imshow('bitwise_xor', bitwise_xor)

bitwise_not = cv.bitwise_not(rec,circle)
cv.imshow('bitwise_not', bitwise_not)



cv.waitKey(0)