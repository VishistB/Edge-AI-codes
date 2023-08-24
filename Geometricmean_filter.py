import cv2
import numpy as np

i=cv2.imread("social_10091641.png")
r,c,ch=i.shape
m=3
n=3

print(i.shape)
for chan in range(ch):
    for row in range(1,r-1):
        for col in range(1,c-1):
            cons_mat= i[row-(m-1)//2: row + (m-2)//2 , col-(n-1)//2 : col+(n-1)//2]
            cons_mat=cons_mat/255
            g=np.prod(cons_mat)
            g=g/(m*n)
            t=i[row,col,chan]
            i[row,col,chan]=g
cv2.imshow(i)