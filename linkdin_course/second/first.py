import numpy as np
import cv2

img= cv2.imread("hcopy.png")
cv2.namedWindow("image",cv2.WINDOW_NORMAL)
cv2.imshow("image",img)
#waitkey mean user can intract with window
cv2.waitKey(0)
cv2.imwrite("output.jpg",img)