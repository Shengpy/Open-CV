import cv2
import time 
import hand 
import numpy as np 
import pyautogui
from pynput.mouse import Button, Controller
def main():
    pTime=0
    cap=cv2.VideoCapture(0)
    mouse = Controller()
    width, height= pyautogui.size()
    detector=hand.handDetector(max_hands=2)
    while 1:
        success,img=cap.read()
        img=detector.findHands(img)
        lmList=detector.findPosition(img)
        if len(lmList)!=0:
            x1,y1=lmList[8][1:]
            x2,y2=lmList[12][1:]
            fingers=detector.handFingers()   
            if fingers[1]==1 and fingers[2]==0:
            #Convert Coordinates
                x=np.interp(x1,(100,int(img.shape[1]-100)),(0,width))
                y=np.interp(y1,(100,int(img.shape[0]-100)),(0,height))
                mouse.position=(width-x,y)
                if fingers[4]==1:
                    mouse.press(Button.left)
                    mouse.release(Button.left)           
        cTime=time.time()
        fps=1/(cTime-pTime)
        pTime=cTime
        cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
        cv2.imshow("Image",img)
        if cv2.waitKey(20)& 0xFF==ord('d'):
               break
    cap.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()

