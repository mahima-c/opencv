import numpy as np
import cv2

# img= cv2.imread("hcopy.png",1)
black=np.zeros([150,200,1],"uint8")
cv2.imshow("black",black)

print(black.shape)
print(black[0,0,:])
ones=np.ones([150,200,3],"uint8")
cv2.imshow("ones",ones)
print(ones.shape)
print(ones[0,0,:])

white=np.ones([150,200,3],"uint16")
white *=(2**16-1)
cv2.imshow("white",white)
print(white.shape)
print(white[0,0,:])
color=ones.copy()
color[:,:]=(255,0,0)
cv2.imshow("blue",color)


print(color[0,0,:])

cv2.waitKey(0)
cv2.destroyAllWindows()