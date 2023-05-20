import cv2
import mediapipe as mp
import time 
class FaceMeshDetector():
    def __init__(self,mode=False,maxFaces=2,minDetectionCon=0.5,minTrackCon=0.5):
        self.mode=mode
        self.maxFaces=maxFaces
        self.minDetectionCon=minDetectionCon
        self.minTrackCon=minTrackCon

        self.mpDraw=mp.solutions.drawing_utils
        self.mpFaceMesh=mp.solutions.face_mesh
        self.faceMesh=self.mpFaceMesh.FaceMesh(self.mode,self.maxFaces,self.minDetectionCon,self.minTrackCon)
        self.drawSpec=self.mpDraw.DrawingSpec(thickness=1,circle_radius=2)
    def findFaceMesh(self,img,draw=True):
        self.imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results=self.faceMesh.process(self.imgRGB)
        if self.results.multi_face_landmarks:
            faces=[]
            for faceLms in self.results.multi_face_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img,faceLms,self.mpFaceMesh.FACEMESH_CONTOURS,self.drawSpec,self.drawSpec)
                for id,lm in enumerate(faceLms.landmark):
                    h,w,c=img.shape
                    x,y=int(lm.x*w),int(lm.y*h)
                    #cv2.putText(img,str(id),(x,y),cv2.FONT_HERSHEY_PLAIN,0.5,(0,255,0),1)
                    faces.append([id,x,y])
        return img,faces
def main():
    pTime=0
    cap=cv2.VideoCapture(0)
    detector=FaceMeshDetector(maxFaces=1)
    while 1:
        success,img=cap.read()
        img,faces=detector.findFaceMesh(img,True)
        if len(faces)!=0:
            print(faces[0])
            #cv2.circle(img,(faces[0][1],faces[0][2]),5,(255,0,255),cv2.FILLED)
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
