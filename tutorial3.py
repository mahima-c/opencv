#how to draw diffrent geomentric shapa
import cv2
import numpy as np

#img=cv2.imread('ex.jpg',1)
#we can create an image from numpy zero method
#for black image 3
img=np.zeros([512,512,3],np.uint8)



img=cv2.line(img,(0,0),(455,0),(255,0,0),3)
img=cv2.arrowedLine(img,(0,0),(455,0),(255,0,0),3)
#top lest vertix ang lower  right 
img=cv2.rectangle(img,(349,0),(655,280),(234,87,99),5)#if we give thickness negative than it filled with that color which is given to 
#circle
#for put text to image
font=cv2.FONT_HERSHEY_SIMPLEX
img= cv2.putText(img,'mahima',(10,500),font,4,(255,70,0),10,cv2.LINE_AA)
cv2.imshow("display",img)
cv2.waitKey(0)

cv2.destroyAllWindows()
