import cv2 as cv
from cv2 import threshold
import numpy as np

# Reading images
img = cv.imread('./Photos/cats.jpg')
cv.imshow('cats',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# Simple thresholding for advanced cases defining thresh value by ourselfs may be aproblem
threshold,thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow('threshed',thresh)
# print(threshold)

threshold_inv,thresh_inv = cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow('threshed_inv',thresh_inv)

# Adaptive thresholding selects thresh value when computing optimal thresh value

adaptive = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,1)
cv.imshow('adaptive',adaptive)



cv.waitKey(0)
cv.destroyAllWindows()