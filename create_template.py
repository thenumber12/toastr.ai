import cv2 as cv
import sys

filename = sys.argv[1]

img = cv.imread(filename)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret,thresh = cv.threshold(gray,100,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

for i in range(9):
    thresh = cv.dilate(thresh, None)
for i in range(6):
    thresh = cv.erode(thresh, None)

cv.imwrite(filename.split('.')[0] + "-binary.png", thresh)

cont, hier = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
for i in range(len(cont)):
    c = cont[i]
    h = hier[0, i]
    if h[2] != -1 and h[3] != -1:
        thresh = cv.drawContours(thresh, [c], -1, (0,0,0), -1)
        t = cv.boundingRect(c)

x = t[0]
y = t[1]
w = t[2]
h = t[3]

template = thresh[y-10:y+h+10, x-10:x+w+10]

cv.imwrite(filename.split('.')[0] + "-template.png", template)