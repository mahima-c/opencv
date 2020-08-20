import numpy as np
import cv2
canvas=np.ones([500,500,3],'uint8')*255
radius=3
color=(0,255,0)
pressed=False


#click callback
def click(event,x,y,flags,param):
    global canvas
    global pressed
    if event ==cv2.EVENT_LBUTTONDOWN:
        pressed=True
        cv2.circle(canvas,(x,y),radius,color,-1)
    elif event==cv2.EVENT_MOUSEMOVE and pressed==True:
        cv2.circle(canvas,(x,y),radius,color,-1)
    elif event==cv2.EVENT_LBUTTONUP:
        pressed=False

#window initalization and callback assignment
cv2.namedWindow("canvas")
cv2.setMouseCallback("canvas",click)
#forever draw loop
while True:
    cv2.imshow("canvas",canvas)

    #key capture every 1ms
    ch=cv2.waitKey(1)
    if ch==ord("q"):
        break
    elif ch==ord("b"):
        color=(255,0,0)

    elif ch==ord("g"):
        color=(0,255,0)
    elif ch==ord("c"):
        canvas=np.ones([500,500,3],'uint8')*255


cv2.destroyAllWindows()