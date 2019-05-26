import cv2

address="D:/shape.png"

img1=cv2.imread(address)
img=cv2.imread(address,0)
ret,thresh = cv2.threshold(img,230,255,1)

im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

print len(contours)

c = max(contours, key = cv2.contourArea)
print c
cv2.drawContours(img1,[c+1],0,(0,255,0),4)
cv2.imshow('img1',img1)


for cnt in contours:
        approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
        

        #print len(approx)

        if len(approx)==5:
            e=approx[0]
            M = cv2.moments(cnt)
            #print M
            #print e[0][0]
            cv2.putText(img1, "pentagone", (e[0][0],e[0][1]),cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 0, 0), 2)
            print "pentagon"
            #c=cnt.astype("float")        
            cv2.drawContours(img1,[cnt],0,(0,255,255),4)

        elif len(approx)==4:
            e=approx[0]
            M = cv2.moments(cnt)
            #print M
            #print e[0][0]
            cv2.putText(img1, "square", (e[0][0],e[0][1]),cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 0, 0), 2)
            print "Square"
            #c=cnt.astype("float")        
            cv2.drawContours(img1,[cnt],0,(0,255,255),4)


cv2.imshow('img',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()


##shape="undef"
##perimeter=cv2.aceLength(c,True)
##approx=cv2.approxPolyDP(c,0.04*perimeter,True)
