import numpy as np
import cv2

def gamma_corr(image,gamma):
	invGamma = 1.0 / gamma
	table = np.array([((i / 255.0) ** invGamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
	# apply gamma correction using the lookup table
	return cv2.LUT(image, table)

def log_transform(image,c):
	#c*log(image + 1)....apply 0-255 back and forth
	table = np.array([(np.log((i / 255.0)+1) * c) * 255 for i in np.arange(0, 256)]).astype("uint8")
	return cv2.LUT(image, table)

def img_add(image,factor):
	#apply normalization 0-255 after addition
	return image+factor

def img_mul(image,factor):
	#apply normalization 0-255 after multiplication
	return image*factor

i=cv2.imread('dark.jpeg')
i_corr1=gamma_corr(i,0.5)
i_corr2=log_transform(i,1.5)

cv2.imshow('orig',i)
cv2.waitKey(0)

cv2.imshow('gamma=0.5',i_corr1)
cv2.waitKey(0)

cv2.imshow('log',i_corr2)
cv2.waitKey(0)
