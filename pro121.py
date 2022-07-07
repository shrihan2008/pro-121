
import cv2
import time
from cv2 import COLOR_BGR2HSV
import numpy as np

fourcc=cv2.VideoWriter_fourcc(*"XVID")
output_file=cv2.VideoWriter('output.avi',fourcc,15.0,(640,4800))


cap=cv2.VideoCapture(0)
time.sleep(2)
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
    
    mask_1=cv2.inRange(hsv,l_black,u_black)

    l_black=np.array([104,153,78])
    u_black=np.array([30, 30, 0])
    mask_2=cv2.inRange(hsv,l_black,u_black)
    mask_1=mask_1+mask_2

    mask_1=cv2.morphologyEx(mask_1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))
    mask_1=cv2.morphologyEx(mask_1,cv2.MORPH_DILATE,np.ones((3,3),np.uint8))

    mask_2=cv2.bitwise_not(mask_1)
    res_1=cv2.bitwise_and(img,img,mask=mask_2)
    res_2=cv2.bitwise_and(bg,bg,mask=mask_1)

    last_output=cv2.addWeighted(res_1,1,res_2,1,0)
    output_file.write(last_output)
    cv2.imshow("Hello",last_output)
    cv2.waitKey(1)

cap.release()
out.release()
cv2.destroyAllWindows()

#l_black = np.array([0, 120, 50]) u_black = np.array([10, 255,255]) mask_1 = cv2.inRange(hsv, l_black, u_black) l_black = np.array([170, 170, 70]) u_black = np.array([180, 255, 255])