import cv2 as cv
import numpy as np

# Reading images
img = cv.imread('./Photos/cat.jpg')
cv.imshow('cat',img)

# Reading videos

capture = cv.VideoCapture('./Videos/dog.mp4')

while True:
    isTrue,frame = capture.read()
    cv.imshow('video',frame)

    if cv.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()

cv.waitKey(0)
cv.destroyAllWindows()