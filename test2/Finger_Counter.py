import cv2
import time 
import os 
import opencv
import hand
import math
def main():
    pTime=0
    
    overlayList=[]
    folderPath="FingerImages"
    myList=os.listdir(folderPath)
    for imPath in myList:
        image=cv2.imread("{0}//{1}".format(folderPath,imPath))
        image=opencv.rescaleFrame(image,scale=0.5)
        overlayList.append(image)
    detector=hand.handDetector(detectionCon=0.75)
    cap=cv2.VideoCapture(0)

    while 1:
        success,img=cap.read()
        img=detector.findHands(img,False)
        lmList=detector.findPosition(img,draw=False)
        if len(lmList)!=0:
            fingers=detector.handFingers()            
            cv2.putText(img,str(sum(fingers)),(475,300),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
            pic=overlayList[sum(fingers)-1]
            h,w=pic.shape[:2]
            img[0:h,0:w]=pic
        cTime=time.time()
        fps=1/(cTime-pTime)
        pTime=cTime
        cv2.putText(img,'fps'+str(int(fps)),(475,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
        cv2.imshow("Image",img)
        if cv2.waitKey(20)& 0xFF==ord('d'):
               break
    cap.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()

