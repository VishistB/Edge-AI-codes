import imutils
import cv2
import numpy as np

i=cv2.imread('sudoku.jpeg')
blurImg = cv2.blur(i,(3,3)) 
cv2.imshow('Original image',i)

# weighted averaging filter
cv2.waitKey(0)
cv2.imshow('blurred image',blurImg)
  
cv2.waitKey(0)