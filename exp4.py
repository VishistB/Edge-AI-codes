import imutils
import cv2
import numpy as np

i=cv2.imread('dark.jpeg')
alpha = 1.04
c=1
for beta in range(25):
	new_image = cv2.convertScaleAbs(i, alpha=alpha, beta=beta)
	cv2.imwrite('aug/'+str(c)+'.jpg',new_image)
	c=c+1

ii=1
for r in np.linspace(-10,10,91):
	rotated = imutils.rotate_bound(i, r)
	cv2.imwrite('aug/r'+str(ii)+'.jpg',rotated)
	ii = ii + 1