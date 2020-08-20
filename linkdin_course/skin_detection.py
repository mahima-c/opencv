import numpy as np
import cv2

img=cv2.imread('hcopy.png',1)
img=cv2.resize(img,(500,500))

hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
h=hsv[:,:,0]
s=hsv[:,:,1]
v=hsv[:,:,2]
#dispalay these channel side by side in one axis
hsv_split=np.concatenate((h,s,v),axis=1)
cv2.imshow("split_hsv",hsv_split)
ret,min_sat=cv2.threshold(s,40,255,cv2.THRESH_BINARY)
cv2.imshow("sat filter",min_sat)

ret,max_hue=cv2.threshold(h,15,255,cv2.THRESH_BINARY_INV)

cv2.imshow("hue-filter",max_hue)
final=cv2.bitwise_and(min_sat,max_hue)
cv2.imshow("final",final)
cv2.imshow("original",img)

cv2.waitKey(0)
cv2.destroyAllWindows()