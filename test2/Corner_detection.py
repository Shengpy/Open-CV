#import cv2
#import mediapipe as mp
#import time 
#import numpy as np 
#def main():
#    pTime=0
#    cap=cv2.VideoCapture(0)

#    while 1:
#        success,img=cap.read()
#        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#        width=int(cap.get(3))
#        height=int(cap.get(4))
#        corners=cv2.goodFeaturesToTrack(img,100,0.01,10)
#        corners=np.int0(corners)
        
#        for corner in corners:
#            x,y=corner.ravel()
#            cv2.circle(img,(x,y),5,(255,0,0),-1)
#        #for i in range(len(corners)):
#        #    for j in range(i+1,len(corners)):
#        #        corner1=tuple(corners[i][0])
#        #        corner2=tuple(corners[j][0])
#        #        #color=tuple(map(lambda x:int(x),np.random.randint(0,255,size=3)))
#        #        #cv2.line(img,corner1,corner2,color,3)
#        cTime=time.time()
#        fps=1/(cTime-pTime)
#        pTime=cTime
#        cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
#        cv2.imshow("Image",img)
#        if cv2.waitKey(20)& 0xFF==ord('d'):
#               break
#    cap.release()
#    cv2.destroyAllWindows()
#if __name__ == "__main__":
#    main()

