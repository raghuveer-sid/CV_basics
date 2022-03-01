import cv2 as cv
from cv2 import imshow
import numpy as np

# Reading images
img = cv.imread('./Photos/cats.jpg')
cv.imshow('cats',img)

# Averaging
# higher th ekernel size higher the blurr
average = cv.blur(img,(3,3))
cv.imshow('averaged',average)

# Gaussian 

gaussian = cv.GaussianBlur(img,(3,3),0)
cv.imshow('gaussian',gaussian)

# Median blurr

median = cv.medianBlur(img,3)
cv.imshow('median',median)

# Bilateral

bilateral = cv.bilateralFilter(img,5,15,15)
cv.imshow('bilateral',bilateral)

cv.waitKey(0)
cv.destroyAllWindows()