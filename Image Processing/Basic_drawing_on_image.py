import cv2
import numpy as np
import matplotlib.pyplot as plt
imglink="C:/Users/new/Desktop/watch.jpg"
img=cv2.imread(imglink,cv2.IMREAD_COLOR)
cv2.line(img,(0,0),(150,150),(255,0,0),10)                 #last line define color of line is BGR(0 to 255) and lst parameter show line width
cv2.rectangle(img,(15,25),(200,150),(0,255,0),5)
cv2.circle(img,(100,63),55,(0,0,255),-1)                                #(center),radius,(color),-1 is filled
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'watch',(0,130),font,1,(255,255,0),1,cv2.LINE_AA)                    #img location,type of font,font size,color,thickness,alias
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.DestroyAllWindows()
