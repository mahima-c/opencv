#how to use track bar in opencv
import cv2
import numpy as np


def nothing(x):
    print(x)

# img=np.zeros((300,512,3),np.uint8)
# img=cv2.imread('ld.jpg')
cv2.namedWindow('image')
#create track bar
cv2.createTrackbar('CP','image',10,400,nothing)



#ADD A SWITCH
switch='color/gray'
cv2.createTrackbar('switch','image',0,1,nothing)

while(1):
    img=cv2.imread('ld.jpg')
    


    k=cv2.waitKey(1) & OxFF 
    if k==27:
        break
    POS=cv2.getTrackbarPos('CP','image')
    font=cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,str(POS),(50,150),font,4,(0,0,255))
    S=cv2.getTrackbarPos('switch','image')

    if S==1:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        

    else:
        pass
    
    img=cv2.imshow('image',img)



cv2.destroyAllWindows()
