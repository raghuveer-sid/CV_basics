import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Reading images
img = cv.imread('./Photos/cats.jpg')
cv.imshow('cats',img)

blank = np.zeros(img.shape[:2],dtype='uint8')
# cv.imshow('blank',blank)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

circle = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
# cv.imshow('circle',circle)

mask = cv.bitwise_and(gray,gray,mask = circle)
cv.imshow('mask',mask)
# gray histogram

gray_hist = cv.calcHist([gray],[0],mask,[256],[0,256])

# plt.figure()
# plt.title('Gray histogram')
# plt.xlabel('bins')
# plt.ylabel(' # of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# Color histogram
circle = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
mask2 = cv.bitwise_and(img,img,mask = circle)
cv.imshow('mask',mask2)

plt.figure()
plt.title('Gray histogram')
plt.xlabel('bins')
plt.ylabel(' # of pixels')

colors = ('b','g','r')

for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i],circle,[256],[0,256])
    plt.plot(hist,color = col)
    plt.xlim([0,256])

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()