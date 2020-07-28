#how to use track bar in opencv
import cv2
import numpy as np


def nothing(x):
    print(x)

img=np.zeros((300,512,3),np.uint8)
cv2.namedWindow('image')
#create track bar
cv2.createTrackbar('B','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('S','image',0,1,nothing)



#ADD A SWITCH
switch='0:OFF\n 1:ON'
while(1):
    cv2.imshow('image',img)
    k=cv2.waitKey(1) #& OxFF 
    if k==27:
        break
    B=cv2.getTrackbarPos('B','image')
    G=cv2.getTrackbarPos('G','image')
    R=cv2.getTrackbarPos('R','image')
    S=cv2.getTrackbarPos('S','image')

    if S==1:
        img[:]=[B,G,R]
    else:
        img[:]=0



cv2.destroyAllWindows()
