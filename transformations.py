import cv2 as cv
from cv2 import imshow
import numpy as np

img = cv.imread('./Photos/park.jpg')

# Translating image

def translation(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

# -x ---> Left
# -y --> Up
# x ---> Right
# y --> Down

translated = translation(img,100,100)
cv.imshow('translated',translated)

# Rotating image

def rotate(img, angle, rotPoint = None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = (width, height)

    return cv.warpAffine(img,rotMat,dimensions)

rotated = rotate(img,30)
cv.imshow('rotated',rotated)

# Resizing

resize = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('resized',resize)

# Flipping
# 0 --> vertical flip 
# 1 --> Horizontal flip
# -1 --> Both vertical and horizontal


flip = cv.flip(img,0)
cv.imshow('fliped',flip)

# Crop

crop = img[200:400,300:400]
cv.imshow('cropped',crop)

cv.waitKey(0)
cv.destroyAllWindows()