import imutils
import cv2
import numpy as np
from PIL import Image,ImageFilter


i=Image.open('sudoku.jpeg')
filt_img=i.filter(ImageFilter.MaxFilter(size=25))
# for integ in range(1,2):
#     print("epoch: ",integ)
#     # filt_img=filt_img.filter(ImageFilter.MinFilter(size=25))
#     filt_img=filt_img.filter(ImageFilter.EMBOSS)
filt_img.save('fil2.png')
#implement max,median filters
