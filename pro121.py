
import cv2
import time
from cv2 import COLOR_BGR2HSV
import numpy as np
cap=cv2.VideoCapture(0)
Image=cap.read()

fourcc=cv2.VideoWriter_fourcc(*"XVID")
Frame=cv2.VideoWriter('output.avi',fourcc,15.0,(1000,1000))

Image=cv2.resize(Image,(640,480))
Frame=cv2.resize(Frame,(640,480))
bg=0
for i in range(60):
    ret,bg=cap.read()

bg=np.flip(bg,axis=1)

while(cap.isOpened()):
    ret,img=cap.read()
    if ret==False:
        break
    img=np.flip(img,axis=1)
    hsv=cv2.cvtColor(img,COLOR_BGR2HSV)
    u_black=np.array([104, 153,78])
    l_black=np.array([30, 30, 5])
    
    mask=cv2.inRange(hsv,l_black,u_black)
    res=cv2.bitwise_and(Frame,Frame,mask=mask)

    last_output=cv2.addWeighted(res,1,res,1,0)
    Frame.write(last_output)
    cv2.imshow("Hello",last_output)
    cv2.waitKey(1)

    
    f=Frame-res
    f=np.where(f==0,Image,f)

    if cv2.waitKey(1) & 0xFF==ord('q'):
            break



cap.release()
out.release()
cv2.destroyAllWindows()

#l_black = np.array([0, 120, 50]) u_black = np.array([10, 255,255]) mask_1 = cv2.inRange(hsv, l_black, u_black) l_black = np.array([170, 170, 70]) u_black = np.array([180, 255, 255])