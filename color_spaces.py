import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt



img = cv.imread('./Photos/park.jpg')

# # matlob displays as RGB rather thab BGR in cv so matlob invets rgb to bgr or bgr to rgb
# plt.imshow(img)
# plt.show()

# BGR to gray scale

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#BGR to HSV

hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('hav',hsv)

#BGR to LAB

lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('lab',lab)

# BGR to RGB

rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)

# HSV to BGR

hsv_bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('hsvbgr',hsv_bgr)

# LAB to BGR

lab_bgr = cv.cvtColor(lab,cv.COLOR_LAB2BGR)
cv.imshow('labbgr',lab_bgr)


cv.waitKey(0)