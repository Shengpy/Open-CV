import cv2 as cv
import numpy as np 
#red 0,0,255
#white 255,255,255
#BACKGROUND
#doc------ngang
#blank=np.zeros((500,500,3),dtype='uint8')
#cv.imshow('blank',blank)
#doc-------ngang
#blank[200:300,300:400]=0,255,0 
#cv.imshow('green',blank)

#thickness(-1,+99)
#cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,0,255),thickness=-1)
#cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),100,(0,255,0),thickness=-1)
#cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=3)
#cv.putText(blank,'hello sheng!!',(0,250),cv.FONT_HERSHEY_TRIPLEX,1,(0,255,0))
#cv.imshow('text',blank)
#cv.waitKey(0)
#---------------------------------------------------------------resize function------------------------------
def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1] * scale)
    height=int(frame.shape[0] * scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_CUBIC)
#interpolation=cv.INTER_AREA
#---------------------------------------------------------------StackImage -------------------------------
#img=np.hstack((img1,img2))        #xếp ngang 
#img=np.vstack((img,img))           #xếp dọc 
def stackImages(imgArray,scale=1):
    rows=len(imgArray[0])
    cols=len(imgArray)
    for i in range(0,cols):
        for j in range(0,rows):
            imgArray[i][j]=rescaleFrame(imgArray[i][j],scale=scale)
    width=imgArray[0][0].shape[1]
    height=imgArray[0][0].shape[0]
    hor = imgArray[0][0]
    for j in range(1,rows):
        hor=np.hstack((hor,imgArray[0][j]))
    result=hor
    for i in range(1,cols):
            hor = imgArray[i][0]
            for j in range(1,rows):
                hor=np.hstack((hor,imgArray[i][j]))
            result=np.vstack((result,hor))
    return result
#----------------------------------------------------------------translate-------------------------------------
#def translate(img,x,y):
#    transmat=np.float32([[1,0,x],[0,1,y]])
#    dimensions=(img.shape[1],img.shape[0])
#    return cv.warpAffine(img,transmat,dimensions)
#def rotate(img,angle,rotPoint=None):
#    (height,width)=img.shape[:2]
#    if rotPoint is None:
#        rotPoint=(width//2,height//2)
#    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
#    dimensions=(width,height)
#    return cv.warpAffine(img,rotMat,dimensions)
#img=cv.imread('vip.jpg')
#width,height=350,210
#pts1=np.float32([[399,183],[681,58],[496,415],[759,250]]) #left righ left right 
#pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
#matrix=cv.getPerspectiveTransform(pts1,pts2)
#imgOutput=cv.warpPerspective(img,matrix,(width,height))
#cv.imshow('image',img)
#cv.imshow('output',imgOutput)
#cv.waitKey(0)
#----------------------------------------------------------------image-----------------------------
#img=cv.imread('idol.jpg')
##img=cv.flip(img,0)
#cv.imshow('human',img)
##gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
##cv.imshow('gray',gray)
#blur=cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
#cv.imshow('human-blured',blur)                   
#canny=cv.Canny(img,125,175)
#cv.imshow('canny edges',canny)
#cv.waitKey(0)
#--------------------------------------------------------------video------------------------------------
#0 webcam 
#capture=cv.VideoCapture(0)
#while True:
#    isTrue, frame =capture.read()
#    frame_resized= rescaleFrame(frame,scale=.2)
#    cv.imshow('Video',frame)
#    cv.imshow('video resized',frame_resized)
#    if cv.waitKey(20)& 0xFF==ord('d'):
#        break
#capture.release()
#cv.destroyAllWindows()
#------------------------------------------------------------------------------------------------
#import cv2 as cv
#import mediapipe as mp
#import time 
#def main():
#    pTime=0
#    cap=cv.VideoCapture(0)
#    while 1:
#        success,img=cap.read()
        
#        cTime=time.time()
#        fps=1/(cTime-pTime)
#        pTime=cTime
#        cv.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
#        cv.imshow("Image",img)
#        if cv.waitKey(20)& 0xFF==ord('d'):
#               break
#    cap.release()
#    cv.destroyAllWindows()
#if __name__ == "__main__":
#    main()






