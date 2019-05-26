import numpy as np
import cv2

face=cv2.CascadeClassifier("C:/Users/new/Desktop/face.xml")
fin=cv2.CascadeClassifier("C:/Users/new/Desktop/fin.xml")
fist=cv2.CascadeClassifier("C:/Users/new/Desktop/hand.xml")

cap=cv2.VideoCapture(0)
w=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))            #get width of the frame
h=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))           #get the height of the frame

fourcc=cv2.VideoWriter_fourcc(*'MJPG')              #frw comp support XVID mine support MJPG
out=cv2.VideoWriter('D:/output.mp4',fourcc,20,(w,h))


while True:
    
    ret,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    fins=fin.detectMultiScale(gray,1.3,5)
    fistt=fist.detectMultiScale(gray,1.3,5)
    faces=face.detectMultiScale(gray,1.3,5)
    #print len(fistt)
    ee=len(fins)

    if len(faces)==1:
        cv2.putText(img, "Hello there", (25,125),cv2.FONT_HERSHEY_SIMPLEX,1.2, (0, 0, 0), 2)
    elif len(faces)==0:
        cv2.putText(img, "LOOK AT ME", (25,125),cv2.FONT_HERSHEY_SIMPLEX,1.2, (0, 0, 0), 2)
    
    if ee==1:
        cv2.putText(img, "I CAN SEE YOUR FINGER", (25,25),cv2.FONT_HERSHEY_SIMPLEX,1.2, (0, 0, 0), 2)
        
    elif ee>2:
        cv2.putText(img, "DO YOU WANT ME TO TELL U YOUR HOROSCOPE", (25,25),cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 0, 0), 2)
    
    else:
        cv2.putText(img, "", (25,25),cv2.FONT_HERSHEY_SIMPLEX,1.2, (0, 0, 0), 2)

    if len(fistt)==1:
        cv2.putText(img, "FUCK U SJ", (25,65),cv2.FONT_HERSHEY_SIMPLEX,1.2, (0, 0, 0), 2)


    for(x,y,w,h) in fins:        
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        #roi=gray[y:y+h,x:x+w]
        #colr=imgimg[  ]
    for(x,y,w,h) in fistt:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)

    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)
    cv2.imshow('img',img)
    out.write(img)
    
    if cv2.waitKey(1) & 0xFF==ord('q'):                 #press q to exit the window
        break
cap.release()
cv2.destroyAllWindows()
