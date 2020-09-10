import numpy as np
import cv2

img=cv2.imread("hcopy.png",1)
cv2.imshow("image",img)
#explictily set window,basically set the window coordinate
cv2.moveWindow("image",0,0)
height,width,channels = img.shape
b,g,r=cv2.split(img)
#create unintialise empty array 
rgb_split=np.empty([height,width*3,3],'uint8')


cv2.waitKey(0)
cv2.destroyAllWindows()
