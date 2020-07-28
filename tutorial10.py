#perform some basic operation on images(arithematic operation)
import cv2
import numpy as np

img=cv2.imread('ld.jpg',1)
img2=cv2.imread('ex.jpg',1)

# print(img)
# print('gap')
print(img.shape)# it return no of coloum and row  and channel in tuple formate
print(img.size)#total no of pixel is accessed
print(img.dtype)#return image data type is obtained
b,g,r=cv2.split(img)
img=cv2.merge((r,g,b))
boll=img[280:340, 330:390]
print(boll)
img[273:333,100:160]=boll

# print(b)
# print(g)
# print(r)
#ROI(REGION OF INTRESET)
img=cv2.resize(img,(512,512))
img2=cv2.resize(img2,(512,512))

# dst=cv2.add(img,img2)
dst2=cv2.addWeighted(img,.9,img2,.1,0)
cv2.imshow('image',dst2)

cv2.waitKey(0)
cv2.destroyAllWindows()