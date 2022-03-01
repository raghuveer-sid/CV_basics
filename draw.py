import imghdr
import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('blank',blank)

# img = cv.imread('./Photos/cat.jpg')
# cv.imshow('cat',img)

# Paint image a certain color full
blank[:] = 0,255,255
cv.imshow('Green',blank)

# Paint image a certain color small part
blank[200:300,300:400] = 0,255,0
cv.imshow('Green',blank)

# Draw rectangle
cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=2)
cv.imshow('rect',blank)

# Draw rectangle filled
cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=-1)
cv.imshow('rect',blank)

# Draw rectangle filled in a particular space half half
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=-1)
cv.imshow('rect',blank)

# Draw circle
cv.circle(blank,(250,250),5,(255,0,0),thickness=2)
cv.imshow('circlr',blank)

# Draw liine
cv.line(blank,(0,0),(250,250),(255,255,0),thickness=2)
cv.imshow('line',blank)

# Put text
cv.putText(blank,'YOLO',(0,250),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,0),thickness=2)
cv.imshow('text',blank)



cv.waitKey(0)
cv.destroyAllWindows()