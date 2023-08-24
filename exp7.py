import cv2
import numpy as np
import skimage
import random

i=cv2.imread('tower.jpeg')
cv2.imshow('original',i)
cv2.waitKey(0)

#cv2.imwrite('compressed.jpg',i,[cv2.IMWRITE_JPEG_QUALITY,20])
#o=skimage.util.random_noise(i/255.0,var=0.0001,mode="gaussian")*255

#o=skimage.util.random_noise(i/255.0,mode="poisson")*255

# cv2.imshow('noisy',np.uint8(o))
# cv2.waitKey(0)


number_of_pixels = random.randint(30 , 100)
row,col,ch=i.shape
for k in range(number_of_pixels):

# Pick a random y coordinate
    y_coord=random.randint(0, row - 1)

    # Pick a random x coordinate
    x_coord=random.randint(0, col - 1)

    # Color that pixel to black
    i[y_coord][x_coord] = 0


number_of_pixels = random.randint(30 , 100)
row,col,ch=i.shape
for k in range(number_of_pixels):

# Pick a random y coordinate
    y_coord=random.randint(0, row - 1)

    # Pick a random x coordinate
    x_coord=random.randint(0, col - 1)

    # Color that pixel to white
    i[y_coord][x_coord] = 255

cv2.imshow('noisy',np.uint8(i))
cv2.waitKey(0)