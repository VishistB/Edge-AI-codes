import cv2
from PIL import Image
import torchvision.transforms as transforms


transform = transforms.Compose([transforms.ToTensor()])

#Reading image using opencv
i=cv2.imread('social_10091641.png')
print(i.shape)

igray=cv2.imread('social_10091641.png',0)
print(igray.shape)


#Reading image using pillow

j=Image.open('social_10091641.png')
jarray=transform(j)
print(jarray.shape,"lol")
# What is the difference between the shapes and the read type?


#Selecting a region in an image
r = cv2.selectROI("select the area", i)
print(r)

#Modifying image ROI areas
i[r[1]:r[1]+r[3],r[0]:r[0]+r[2],0]=0
i[r[1]:r[1]+r[3],r[0]:r[0]+r[2],1]=0
i[r[1]:r[1]+r[3],r[0]:r[0]+r[2],2]=255

cv2.imshow("Modified image", i)
cv2.waitKey(0)

#Pasting a different image in ROI

k=cv2.imread("social_10091641.png")
#Resizing the image...
k1=cv2.resize(k,(r[2],r[3]))
i[r[1]:r[1]+r[3],r[0]:r[0]+r[2]]=k1

cv2.imshow("Modified image2", i)
cv2.waitKey(0)

#What are the different uses of ROI selections? 




