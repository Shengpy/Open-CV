import cv2 as cv
import mediapipe as mp
import time 
import numpy as np 
import opencv 
class ColorDetection():
    def __init__(self):
        self.mycolors=[[5,107,0,19,255,255],
                       [133,56,0,159,156,255],
                       [57,76,0,100,255,255]]   
    def findColor(self,image):
        hsv=cv.cvtColor(image,cv.COLOR_BGR2HSV)
        #lower=np.array(self.mycolors[0][0:3])
        #upper=np.array(self.mycolors[0][3:6])
        #mask=cv.inRange(hsv,lower,upper )        
        #cv.imshow('test',mask)
        for color in self.mycolors:
            lower=np.array(color[0:3])
            upper=np.array(color[3:6])
            mask=cv.inRange(hsv,lower,upper )        
            cv.imshow(str(color[0]),mask)
#def main():
#    def empty(a):
#        pass       
#    cv.namedWindow('TrackBars')
#    cv.resizeWindow('TrackBars',640,240)
#    cv.createTrackbar('Hue Min','TrackBars',0,179,empty)
#    cv.createTrackbar('Sat Min','TrackBars',0,255,empty)
#    cv.createTrackbar('Val Min','TrackBars',0,255,empty)
#    cv.createTrackbar('Hue Max','TrackBars',179,179,empty)   
#    cv.createTrackbar('Sat Max','TrackBars',255,255,empty)
#    cv.createTrackbar('Val Max','TrackBars',255,255,empty) 
#    while 1:
#        img=cv.imread('doaremon.jpg')
#        gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#        hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
#        h_min=cv.getTrackbarPos('Hue Min','TrackBars') 
#        h_max=cv.getTrackbarPos('Hue Max','TrackBars') 
#        s_min=cv.getTrackbarPos('Sat Min','TrackBars') 
#        s_max=cv.getTrackbarPos('Sat Max','TrackBars') 
#        v_min=cv.getTrackbarPos('Val Min','TrackBars') 
#        v_max=cv.getTrackbarPos('Val Max','TrackBars') 
#        lower=np.array([h_min,s_min,v_min])
#        upper=np.array([h_max,s_max,v_max])
#        mask=cv.inRange(hsv,lower,upper )
#        result=cv.bitwise_and(img,img,mask=mask)
#        #cv.imshow('human',img)
#        #cv.imshow('test',mask)
#        cv.imshow('result',result)
#        cv.waitKey(1)
def main():
    pTime=0
    cap=cv.VideoCapture(0)
    CD=ColorDetection()
    while 1:
        success,img=cap.read()
        CD.findColor(img)
        cv.imshow('Result',img)
        cv.waitKey(1)
        if cv.waitKey(20)& 0xFF==ord('d'):
           break
    cap.release()
    cv.destroyAllWindows()
if __name__ == "__main__":
    main()
