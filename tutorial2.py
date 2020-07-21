#capture livestream from camera
import cv2
#if we want to read viedo from anyfile then give filename as parameter of viedocapture
#for read from camera give the index 0 or some device have -1 also and if we have multiple camera then we use index as 1,2,3 as.
cap= cv2.VideoCapture(0);
#create class for write viedo      fourcc code which is specify for viedo codec ,identify the data formate
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))



#print(cap.isOpened())
while(True):
    #for capture
    ret,frame = cap.read()
    if ret ==True:

        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))#PROP ID are many to know the property
        out.write(frame)
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #if frame is available then ret is ture otherwise false
        cv2.imshow('frame',gray)
    #IF user press q then quit the window
    #waitkey is that wait whenever user give any input
        if cv2.waitKey(1) == ord('q'):
            break

    else:
        break

cap.release()
out.release()

cv2.destroyAllWindows()    