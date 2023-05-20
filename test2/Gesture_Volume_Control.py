import cv2
import mediapipe as mp
import time 
import opencv
import numpy as np
import hand 
import math
from ctypes import cast,POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
def main():
    #wCam,hCam=300,300
    pTime=0
    cap=cv2.VideoCapture(0)
    #cap.set(3,wCam)
    #cap.set(4,hCam)
    detector=hand.handDetector() 
    devices=AudioUtilities.GetSpeakers()
    interface=devices.Activate(IAudioEndpointVolume._iid_,CLSCTX_ALL,None)
    volume=cast(interface,POINTER(IAudioEndpointVolume))
    volRange=volume.GetVolumeRange()
    minVol=volRange[0]
    maxVol=volRange[1]
    volBar=150
    volPer=100
    while 1:
        success,img=cap.read()
        img=detector.findHands(img,draw=True)
        lmList=detector.findPosition(img)
        if len(lmList)!=0:    
           fingers=detector.handFingers()
           if fingers[2]==0:
                lenght,img,position=detector.findDistance(img,4,8)
                vol=np.interp(lenght,[50,150],[minVol,maxVol])
                volBar=np.interp(lenght,[50,150],[400,150])
                volPer=np.interp(lenght,[50,300],[0,100])
                volume.SetMasterVolumeLevel(vol,None)
                if lenght<50:
                    cv2.circle(img,(position[4],position[5]),15,(0,255,0),cv2.FILLED)
                    #volume.GetMute()
        cv2.rectangle(img,(50,150),(85,400),(0,255,0),3)
        cv2.rectangle(img,(50,int(volBar)),(85,400),(0,255,0),cv2.FILLED)
        cv2.putText(img,str(int(volPer)) +'%',(50,450),cv2.FONT_HERSHEY_PLAIN,2,(255,0,255),2)

        cTime=time.time()
        fps=1/(cTime-pTime)
        pTime=cTime
        cv2.putText(img,'FPS: '+str(int(fps)),(10,30),cv2.FONT_HERSHEY_PLAIN,1.5,(255,0,255),1)
        cv2.imshow('Image',img)
        cv2.waitKey(1)
        if cv2.waitKey(20)& 0xFF==ord('d'):
           break
    cap.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()
#------------------------------------------------------------
#devices=AudioUtilities.GetSpeakers()
#interface=devices.Activate(IAudioEndpointVolume._iid_,CLSCTX_ALL,None)
#volume=cast(interface,POINTER(IAudioEndpointVolume))
#volume.GetMute()
#volume.GetMasterVolumeLevel()
#volume.GetVolumeRange()
#volum.SetMasterVolumeLevel(-20.0,None)
