import cv2
import mediapipe as mp
import time 
import Pose
import opencv 
def main():
    pTime=0
    cap=cv2.VideoCapture(0)
    detector = Pose.poseDetector()
    count=0
    t=0
    h=0
    while 1:
        success,img=cap.read()
        img= opencv.rescaleFrame(img,scale=1.5)
        img=detector.findPose(img)
        lmList=detector.findPosition(img)
        if len(lmList) != 0:
              img,angle1=detector.findAngle(img,11,13,21)   
              img,angle2=detector.findAngle(img,12,14,22)  
              if angle1<90 and t==0:
                count+=1
                print(count)
                t=1
              if angle1>90 and t==1:
                t=0
              if angle2<90 and h==0:
                count+=1
                print(count)
                h=1
              if angle2>90 and h==1:
                h=0  
              cv2.putText(img,str(count),(50,140),cv2.FONT_HERSHEY_PLAIN,6,(255,0,255),3)
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
if 1:
    print("Sheng")
if 0:
    print("Tien")