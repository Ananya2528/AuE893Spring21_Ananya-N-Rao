#!/usr/bin/env python3
import cv2
import numpy as np
img = cv2.imread('test1.jpg')
#gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#edges = cv2.Canny(gray,50,150,apertureSize = 7)

edges = cv2.Canny(img,50,100)
minLineLength = 500
maxLineGap = 10
lines = cv2.HoughLinesP(edges,1,np.pi/180,500,minLineLength,maxLineGap)
for x1,y1,x2,y2 in lines[0]:
    cv2.line(img,(x1,y1),(x2,y2),(0,300,0),2)
cv2.imwrite('houghlines1.jpg',img)
