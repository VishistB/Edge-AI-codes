import numpy as np
import cv2 as cv
img = cv.imread('animal.jpeg')
gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#sift = cv.SIFT_create()
sift =cv.xfeatures2d.SIFT_create()
#sift = cv.BRISK_create()
kp, des = sift.detectAndCompute(gray,None)
img=cv.drawKeypoints(gray,kp,img)
cv.imwrite('sift_keypoints.jpg',img)

#see the difference between the 2
#img=cv.drawKeypoints(gray,kp,img,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#cv.imwrite('sift_keypoints.jpg',img)



#Some changes with respect to versions

''' Feature Detector 
if detectorName == "SIFT":
	detector = cv2.xfeatures2d.SIFT_create(400)
	distanceType = cv2.NORM_L2
elif detectorName == "SURF":
	detector = cv2.xfeatures2d.SURF_create(400)
	distanceType = cv2.NORM_L2
elif detectorName == "BRISK":
	detector = cv2.BRISK_create()
	distanceType = cv2.NORM_HAMMING
else:
	detector = cv2.ORB_create()
	distanceType = cv2.NORM_HAMMING
'''