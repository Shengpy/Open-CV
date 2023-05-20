import cv2
import mediapipe as mp
import time 
import opencv
import math
class handDetector():
    def __init__(self,mode=False,max_hands=2,detectionCon=0.5,trackCon=0.5):  
        self.mode=mode
        self.maxHands=max_hands
        self.detectioncon=detectionCon
        self.trackcon=trackCon
        self.mpHands=mp.solutions.hands
        self.hands=self.mpHands.Hands(self.mode,
                                      self.maxHands,
                                      self.detectioncon,
                                      self.trackcon)
        self.mpDraw=mp.solutions.drawing_utils
    def findHands(self,img,draw=True):
        imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results= self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
          for handLms in self.results.multi_hand_landmarks:
            if draw:
              self.mpDraw.draw_landmarks(img,handLms,self.mpHands.HAND_CONNECTIONS)
        return img 
    def findPosition(self,img,handNo=0,draw=True):
        self.lmList=[] 
        if self.results.multi_hand_landmarks:
            myHand=self.results.multi_hand_landmarks[handNo]
            for id,lm in enumerate(myHand.landmark):  #id hand point's position  
                height,width,channels=img.shape
                cx,cy=int(lm.x*width),int(lm.y*height)
                self.lmList.append([id,cx,cy])
                #if id==8:
                #    cv2.circle(img,(cx,cy),5,(255,0,255),cv2.FILLED)    
        return self.lmList
    def findDistance(self,img,p1,p2,draw=True,r=15,t=3):
       x1,y1=self.lmList[p1][1:]
       x2,y2=self.lmList[p2][1:]
       cx,cy=(x1+x2)//2,(y1+y2)//2
       if draw:
           cv2.circle(img,(x1,y1),15,(255,0,255),cv2.FILLED)
           cv2.circle(img,(x2,y2),15,(255,0,255),cv2.FILLED)
           cv2.line(img,(x1,y1),(x2,y2),(255,0,255),3)
           cv2.circle(img,(cx,cy),15,(255,0,255),cv2.FILLED)
       lenght=math.hypot(x2-x1,y2-y1)
       return lenght,img,[x1,y1,x2,y2,cx,cy]
    def handFingers(self):
       fingers=[]
       tipIds=[4,8,12,16,20]
       for id in range(0,5):
              if id==0 :
                  if self.lmList[tipIds[id]][1]>self.lmList[tipIds[id+3]][1]:
                    if self.lmList[tipIds[id]][1]>self.lmList[tipIds[id]-1][1]:
                        fingers.append(1)
                    else:
                        fingers.append(0)
                  elif  self.lmList[tipIds[id]][1]<self.lmList[tipIds[id+3]][1]:
                    if self.lmList[tipIds[id]][1]<self.lmList[tipIds[id]-1][1]:
                        fingers.append(1)
                    else:
                        fingers.append(0)
              else:
                    if self.lmList[tipIds[id]][2]<self.lmList[tipIds[id]-2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)
       return fingers
def main():
    pTime=0
    cap=cv2.VideoCapture(0)
    detector=handDetector()
    while 1:
        success,img=cap.read()
        img= opencv.rescaleFrame(img,scale=1.5)
        img=detector.findHands(img)
        lmList=detector.findPosition(img)
        
        if len(lmList) != 0:
            print(lmList[4])

        cTime=time.time()
        fps=1/(cTime-pTime)
        pTime=cTime
        cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
        cv2.imshow('Image',img)
        cv2.waitKey(1)
        if cv2.waitKey(20)& 0xFF==ord('d'):
           break
    cap.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()
