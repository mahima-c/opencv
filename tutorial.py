import cv2
img=cv2.imread('ex.jpg',1)
print(img)
cv2.imshow("display",img)
h=cv2.waitKey(0)
if h==27:
    cv2.destroyAllWindows()
elif h== ord('s'):
    cv2.imwrite('hcopy.png',img)
    cv2.destroyAllWindows()
