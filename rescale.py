import imghdr
import cv2 as cv
import numpy as np


img = cv.imread('./Photos/cat_large.jpg')
cv.imshow('catl',img)

# Rescale frames

def rescaleFrame(frame, scale = 0.75):
    # works for images, videos and live videos
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img,0.2)
cv.imshow('resized_image',resized_image)


def changeRes(width,height):
    # works only for live videos
    capture.set(3,width)
    capture.set(4,height)


# Reading videos

capture = cv.VideoCapture('./Videos/dog.mp4')

while True:
    isTrue,frame = capture.read()

    frame_resized = rescaleFrame(frame,0.2)

    #cv.imshow('video',frame)
    cv.imshow('resized_video',frame_resized)

    if cv.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()

cv.waitKey(0)
cv.destroyAllWindows()