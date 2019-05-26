import cv2
import numpy as np
import math
cap=cv2.VideoCapture(0)
w=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))            #get width of the frame
h=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))           #get the height of the frame


#ret,threshold=cv2.threshold(img,129,255,0)
#fourcc=cv2.VideoWriter_fourcc(*'MJPG')              #frw comp support XVID mine support MJPG
#out=cv2.VideoWriter('D:/output.avi',fourcc,20,(w,h))

while True:                                             #infinity loop
    ret,frame=cap.read()
    #cv2.drawContours(frame, contours, -1, (255,0,0) ,1)
    


    #gray = cv2.fastNlMeansDenoisingColoredMulti(frame,0,1,None,3,7,21)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)          #cvt or convert color to
    kernel1=np.ones((16,16),np.uint8)
    kernel2=np.ones((6,6),np.uint8)

    blur = cv2.GaussianBlur(gray,(15,15),0)
    

    gray=cv2.dilate(gray,kernel2,iterations=1)
    #gray=cv2.erode(gray,kernel1,iterations=1)
    retval, gray = cv2.threshold(gray, 127,255,0)
    ret,gray = cv2.threshold(blur,180,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    #gray = cv2.medianBlur(gray,1)


    #kernel = np.ones((5,5),np.uint8)
    #cv2.imshow("c",frame)
    #gray = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel1)
    #gray = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel2)

    gray = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel2)


    im2, contours, hierarchy = cv2.findContours(gray,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #print(len(contours))

    x=list()
    for i in range(0,len(contours)):
        x.append(i)

    for z in x:
        cnt = contours[z]
        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        hull=cv2.convexHull(cnt)
        #print hull
        crop_img = frame[100:300, 100:300]
        ctr = np.array(cnt).reshape((-1,1,2)).astype(np.int32)
        
        box = np.int0(box)
        #hull = np.int0(hull)
        frame = cv2.drawContours(frame,[box],0,(0,255,255),2)
        frame = cv2.drawContours(frame,[hull],0,(255,0,255),2)
        cnt = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)

        hull=cv2.convexHull(cnt,returnPoints=False)
      #  defects = cv2.convexityDefects(cnt,hull)
        #print defects.shape[0]
        #uu=len(defects)
        


        try:
            defects = cv2.convexityDefects(ctr,hull)
            mind=0
            maxd=0
            print defects.shape[0]
            for i in range(defects.shape[0]):
                
                s,e,f,d = defects[i,0]
                start = tuple(cnt[s][0])
                end = tuple(cnt[e][0])
                far = tuple(cnt[f][0])
                #print type(far)
                #dist = cv2.pointPolygonTest(cnt,centr,True)
                #cv2.line(frame,start,end,[0,255,0],2)
                    
                cv2.circle(frame,far,5,[0,0,255],-1)
            #print(i)
            i=0


        except:
            pass
    cv2.imshow('frame',frame)
    #cv2.imshow('hull',hull)
    cv2.imshow('gray',gray)
    


    if cv2.waitKey(1) & 0xFF==ord('q'):                 #press q to exit the window
        break

cap.release()
#hull.release()
#out.release()
cv2.destroyAllWindows()
print"terminated"
