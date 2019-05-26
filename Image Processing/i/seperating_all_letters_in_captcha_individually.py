import imutils
import cv2
import numpy as np


address='C:/Users/new/Desktop/3.jpg'
#ff=open('D:/Python projects/edges.txt','w')
img=cv2.imread(address,0)
img=cv2.resize(img,(1000,500))


ret,threshold=cv2.threshold(img,129,255,0)
laplacian=cv2.Laplacian(threshold,cv2.CV_64F)
edges=cv2.Canny(img,700,700)
kernel=np.ones((5,5),np.uint8)
threshold=cv2.erode(threshold,kernel,iterations=1)

im2, contours, hierarchy = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print len(contours)

x=list()
for i in range(0,len(contours)):
    x.append(i)

for z in x:
    cnt=contours[z]

    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)

    x,y,w,h=cv2.boundingRect(cnt)
    roi=threshold[y:y+h,x:x+w]
    retval,th=cv2.threshold(roi,129,255,0)
    #th=cv2.resize(th,(20,20))
    #cv2.imshow(str(z),th)
    
    dd=cv2.contourArea(cnt)
    
    #print dd

    if dd>10000 and dd<450000:
        print dd
        print z
        print 'eol'
        cv2.imshow(str(z),th)
        th=cv2.resize(th,(200,200))
        loc="d:/"+str(z)+".png"
        cv2.imwrite(loc,th)
    
    
    box = np.int0(box)
    
    threshold = cv2.drawContours(threshold,[box],0,(0,0,255),2)
    x=np.array(th)
    xx=str(x.tolist())
    xxx=str(z)+'\n'+xx+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'
    
    #ff.write(xxx)
    #print 'eol'


#ff.close()
cv2.imshow('orig',img)
cv2.imshow('thres',threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
