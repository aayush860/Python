import glob,os
import cv2
import numpy as np
dir="D:/training set/English/Img/GoodImg/Bmp/Sample011"
sdir=open('C:/Users/new/Desktop/tempo2.txt','w')
os.chdir(dir)
x=0
#def thr():
    
z=list()
for file in glob.glob("*.png"):
    x=x+1
    z.append(dir+'/'+str(file))

x=0
for xx in z:
    x=x+1
    xx='C:/Users/new/Desktop/aa.png'
    img=cv2.imread(xx,0)
    img=cv2.resize(img,(20,20))
    ret,threshold=cv2.threshold(img,15,255,0)
    threshold=cv2.Laplacian(threshold,cv2.CV_64F)
    th3=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    #blur = cv2.GaussianBlur(athes,(5,5),0)
    #ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    

    li=list()
    if x==1:
        ar=np.array(th3)
        for i in range(0,20):
            t=str(ar[i])
            t=t.replace("255","1",10000)
            t=t.replace("]","",10000)
            t=t.replace("\n","",1000)
            t=t.replace("[","",10000)
            t=t.replace("'","",10000)
            t=t.replace(" ","",10000)
            rre=0
            for itee in t:
                itee=int(itee)
                rre=rre+itee
            li.append(rre)
        #print li
        f=0
        for d in range(0,20):
            f=f+li[d]
        #print f
        w=str(li)   
        w=w.replace("]","",10000)
        w=w.replace("[","",10000)
        w=w.replace(" ","",10000)
        w=w.strip()

        stw=str(f)+','+w
        sdir.write(stw)
        print stw
        #print th3
        #print stw
        #cv2.imshow(str(x)+'orig',img)
        th3=cv2.resize(th3,(200,200))
        cv2.imshow('vgvg',th3)        
        print('\n'+"end of line")
#print stw
sdir.close()
cv2.waitKey(0)
cv2.destroyAllWindows()
    
