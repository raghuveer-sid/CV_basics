import cv2 as cv

img = cv.imread('./Photos/park.jpg')
cv.imshow('park',img)

# Convert to gray scale
gray = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
cv.imshow('gray',gray)

# Blur
blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

# Edge cascade
canny = cv.Canny(img,125,175)
cv.imshow('canny edges',canny)

# Dilating the images
dialated = cv.dilate(canny,(3,3),iterations=3)
cv.imshow('dialated',dialated)

# Eroding
erode = cv.erode(dialated,(3,3),iterations=3)
cv.imshow('erode',erode)

# Resized
resize = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('resize',resize)

# Cropping
crop = img[50:200,200:400]
cv.imshow('cropped',crop)




cv.waitKey(0)
cv.destroyAllWindows()