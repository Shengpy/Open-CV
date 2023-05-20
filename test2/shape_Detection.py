import cv2 as cv
import mediapipe as mp
import time 
import opencv 
import numpy as np
class shapeDetector():
    def __init__(self):
        pass
    def getContours(img):
        imgContour=img.copy()
        imgGray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        imgBlur=cv.GaussianBlur(imgGray,(7,7),1)
        imgCanny=cv.Canny(imgBlur,50,50)        
        
        contours,hierarchy=cv.findContours(imgCanny,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
        for cnt in contours:
            area=cv.contourArea(cnt)
            if area>500:    
                cv.drawContours(imgContour,cnt,-1,(255,0,0),1 )
                peri=cv.arcLength(cnt,True)
                approx=cv.approxPolyDP(cnt,0.02*peri,True)    #coordinates of  vertex 
                objCor=len(approx)    #số cạnh                  
                x,y,w,h=cv.boundingRect(approx)
                
                if objCor==3:
                    objectType='Tri'
                elif objCor==4:
                    aspRatio=w/float(h)
                    if aspRatio>0.95 and aspRatio<1.05: objectType='Square'
                    else: objectType='rectangle'
                else:objectType='None'
                cv.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
                cv.putText(imgContour,objectType,(x+w//2,y+h//2),cv.FONT_HERSHEY_PLAIN,1,(0,0,0),1) 
        return imgContour
def main():
    img=cv.imread('hinhhoc.jpg')
    #imgBlank=np.zeros_like(imgGray) 
    
    imgContour=shapeDetector.getContours(img)
    #imgStack=opencv.stackImages([[imgGray,imgBlur,imgCannny],[imgBlank,imgBlank,imgBlank]],0.5)
    #imgStack=opencv.stackImages([img,imgContour],0.5)
    
    #cv.imshow('Detection',imgStack)
    cv.imshow('Detection',img)
    cv.imshow('Detection1',imgContour)
    cv.waitKey(0)
if __name__ == "__main__":
    main()
