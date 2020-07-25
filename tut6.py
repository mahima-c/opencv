#how to show date and time
import cv2
import datetime

#if we want to read viedo from anyfile then give filename as parameter of viedocapture
#for read from camera give the index 0 or some device have -1 also and if we have multiple camera then we use index as 1,2,3 as.
cap= cv2.VideoCapture(0);

cap.set(3, 3000)#associated no of width
cap.set(4, 3000)#assosiated no of height
# print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))



#print(cap.isOpened())
while(True):
    #for capture
    ret,frame = cap.read()
    if ret ==True:
      
    #if frame is available then ret is ture otherwise false
        font= cv2.FONT_HERSHEY_SIMPLEX 
        text='width:' + str(cap.get(3)) + 'height:' + str(cap.get(4))
        datet =str(datetime.datetime.now())
        frame=cv2.putText(frame,datet,(10,50),font,1,(0,255,255),1,cv2.LINE_AA)
        cv2.imshow('frame',frame)
    #IF user press q then quit the window
    #waitkey is that wait whenever user give any input
        if cv2.waitKey(1) == ord('q'):
            break

    else:
        break

cap.release()

cv2.destroyAllWindows()    