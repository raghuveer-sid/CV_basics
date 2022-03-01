import cv2 as cv
import numpy as np

img = cv.imread('./Photos/cats.jpg')

blank = np.zeros(img.shape,dtype='uint8')
cv.imshow('blanked',blank)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
# cv.imshow('blurred',blur)

# canny = cv.Canny(blur,125,175)
# cv.imshow('canny edges',canny)

ret, thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('threshed',thresh)

# Contours 

contours, hierarchies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)

print(f'{len(contours)} contours found')

cv.drawContours(blank,contours,-1,(0,0,255),thickness=1) #-1 is for all  contours
cv.imshow('draw contours',blank)

cv.waitKey(0)
cv.destroyAllWindows()