import numpy as np
import cv2

#dir method show the all function inbuild fuction in cv2
# event=[i for i in dir(cv2) if 'EVENT' in i] 
# print(event)
 
def click_event(event,x,y,flags,param):
    if event ==cv2.EVENT_LBUTTONDOWN:
        # for drawing line
        # cv2.circle(img,(x,y),3,(0,0,255),-1)
        # points.append((x,y))
        # if len(points) >= 2:
        #     cv2.line(img,(x,y),points[-2],(255,0,0),5)

        # cv2.imshow('image',img)    
# for see color of point on another window
        blue=img[x,y,0]
        green=img[x,y,1]
        red=img[x,y,2]
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        mycolorimage=np.zeros((512,512,3),np.uint8)
        # [:]=fill the every element of image with pass paramenter
        mycolorimage[:]=[blue,green,red]
        cv2.imshow('color',mycolorimage)


# img=np.zeros((512,512,3),np.uint8)
img=cv2.imread('ex.jpg')
cv2.imshow('image',img)
points=[]

cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()