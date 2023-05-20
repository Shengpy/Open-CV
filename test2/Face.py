import cv2 
import mediapipe as mp
import time
import opencv
class FaceDetector():
    def __init__(self,minDetectionCon=0.5):
        self.minDetectionCon=minDetectionCon

        self.mpFaceDetection=mp.solutions.face_detection
        self.mpDraw=mp.solutions.drawing_utils
        self.faceDetection=self.mpFaceDetection.FaceDetection()
    def findFaces(self,img,draw=True):
        imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results=self.faceDetection.process(imgRGB)
        bboxs=[]
        if self.results.detections:
            for id,detection in enumerate(self.results.detections):
                #mpDraw.draw_detection(img,detection)
                print(detection.location_data.relative_bounding_box)
                bboxC=detection.location_data.relative_bounding_box
                h,w,c=img.shape
                bbox=int(bboxC.xmin*w),int(bboxC.ymin*h),int(bboxC.width*w),int(bboxC.height*h)
                bboxs.append([id,bbox,detection.score])          
                if draw:
                    img=self.fancyDraw(img,bbox)
                    #cv2.putText(img,f'{int(detection.score[0]*100)}%',
                    #        (bbox[0],bbox[1]-20),cv2.FONT_HERSHEY_PLAIN,
                    #        2,(0,255,0),2)
        return img,bboxs
    def fancyDraw(self,img,bbox,l=30,t=10,rt=1):
        x,y,w,h=bbox
        x1,y1 = x+w,y+h
        cv2.rectangle(img,bbox,(255,0,255),rt)
        cv2.line(img,(x,y),(x+l,y),(255,0,255),t)
        cv2.line(img,(x,y),(x,y+l),(255,0,255),t)

        cv2.line(img,(x1,y1),(x1-l,y1),(255,0,255),t)
        cv2.line(img,(x1,y1),(x1,y1-l),(255,0,255),t)
        return img 
def main():
    cap=cv2.VideoCapture(0)
    pTime=0 
    detector=FaceDetector()
    while True:
        success,img=cap.read()
        img= opencv.rescaleFrame(img,scale=1.5)
        img,bboxs=detector.findFaces(img)
        
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
