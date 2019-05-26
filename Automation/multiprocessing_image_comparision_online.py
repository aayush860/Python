#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 11:24:03 2018

@author: aayushbhargava
"""
from selenium import webdriver
import multiprocessing
import time
import threading
import pyautogui,sys
import cv2,os
import numpy as np
import pyscreenshot

from threading import Thread

driver=webdriver.Chrome('/Users/aayushbhargava/Downloads/chromedriver')

def stop(self):
    self.running = False


def worker():
    name = multiprocessing.current_process().name
    time.sleep(5)
    xxx=0
    while(xxx<1):
        print("Start"+str(3))
        pyautogui.screenshot('/Applications/anaconda/'+str(x)+'.jpg')
        img_rgb = cv2.imread('/Applications/anaconda/'+str(x)+'.jpg')
#cv2.imshow('Detected',img_rgb) 
# Convert it to grayscale
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
 
# Read the template
        template = cv2.imread('/Users/aayushbhargava/Desktop/tmpl.png',0)
 
# Store width and heigth of template in w and h
        w, h = template.shape[::-1]
 
# Perform match operations.
        res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
        
#        print(len(res))
#print(res)

# Specify a threshold
        threshold = 0.8
 
# Store the coordinates of matched area in a numpy array
        loc = np.where( res >= threshold) 
        print(len(loc[0]))
        if (len(loc[0]))>3:
            print("-----------")
            pyautogui.screenshot('/Applications/anaconda/sucess.jpg')
            xxx=5
        time.sleep(5)


       # print (x)
    print name, 'Exiting'

def my_service():
    name = multiprocessing.current_process().name
    
    print("stRTEX--------------")

#    driver=webdriver.Chrome('/Users/aayushbhargava/Downloads/chromedriver')
#    driver.get("https://ehealthreminders.net/dv2/")
    driver.get("https://app1.dev.evivehealth.com:48800/dashboard/")
    upx=["test185gapscarer3user1@evivehealth.com"]
    x=4
    for upn in upx:
        uname=driver.find_elements_by_name("username")
        uname[0].send_keys(upn)
        pswd=driver.find_element_by_name("password")
        pswd.send_keys("evivetest")
        time.sleep(2)
        #    driver.get_screenshot_as_file("/Applications/anaconda/true_cases_more_than_50_no_minor/"+upn+"_sc1"+".png")       #screenshot1
        time.sleep(2)
        rstpswd=driver.find_elements_by_xpath('//*[@id="container"]/div/div/div[1]/div/div/div/form/button')
        rstpswd[0].click()
        time.sleep(3)

        outer=driver.find_elements_by_xpath('//*[@id="container"]/div/div/div[2]/div[2]/div/div[1]/div/div[1]/ul')[0].get_attribute("outerHTML")
        laxes=(outer.count('.png'))
        print(laxes)
        for lx in range(1,(laxes-1)):
            print (lx)
            try:
                fhtmll=driver.find_elements_by_xpath('//*[@id="container"]/div/div/div[2]/div[2]/div/div[1]/div/div[1]/ul/li['+str(lx)+']/a')[0].get_attribute("outerHTML")
            except:
                fhtmll=''
                exit
                
            print(fhtmll)
#            if(fhtmll.count('7589f877df.png')==1):                                            #for telemed
            if(fhtmll.count('38cc3034.png')==1):                                            #for conv
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx----------------------------------------")
                framex=driver.find_elements_by_xpath('//*[@id="container"]/div/div/div[2]/div[2]/div/div[1]/div/div[1]/ul/li['+str(lx)+']/a')
                print(framex[0])
                xcount=0
                for xt in range(0,lx):
                    try:
                        print("ppppppppppppppppppppppppppppppppppppppppppppppppp")
                        time.sleep(2)
                        framex[0].click()
                        lx=xt+1
                        laxes=1
                        time.sleep(3)
                        driver.get("https://app1.dev.evivehealth.com:48800/logout")
                        exit
                    except:
                        time.sleep(5)
        #os._exit(0)
         #upx=["test185gapscarer3user1@evivehealth.com"]


    print name, 'Exitingx'
#    Thread(target = worker).stop()


if __name__ == '__main__':
    x=0

    #time.sleep(3)
    Thread(target = my_service).start()
    Thread(target = worker).start() 
    
    if x>2:
        Thread(target = worker).stop()
#    service = multiprocessing.Process(target=my_service)
 #   service.start()  

    #service.daemon=False
  #  worker_1 = multiprocessing.Process( target=worker)
   # worker_1.start()

    #worker_1.daemon=True
    #worker_2 = multiprocessing.Process(target=worker) # use default name
    #service.join()
   # worker_1.join()
  