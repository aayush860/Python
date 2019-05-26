#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 14:13:31 2018

@author: aayushbhargava
"""

import time
import json
import threading
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
START_TIME = time.time()
PATH_ADDRESS = "/Users/aayushbhargava/Documents/evive/"
UPIN_SS = ['test1032cmprole1user1@evivehealth.com', 'test1032cmprole3user1@evivehealth.com']
def tempx(UPIN_SS):
    driver_templ_id = str(UPIN_SS)
    driver_templ_id = webdriver.Chrome("/Users/aayushbhargava/Downloads/chromedriver")
    website = 'https://ehealthreminders.net/signin'
    payload = {'username':UPIN_SS, 'password':'enecjnej'}
    session = requests.session()
    #---------------------login
    r_1 = session.post(website, data=payload, allow_redirects=True)
    #---------------------resetTracking
    session.get("https://ehealthreminders.net/resetTrackingForSinglePerson", cookies=r_1.cookies)
    driver_templ_id.get("https://ehealthreminders.net/dashboard")
    #--------------------adding session cookies to selenium browser from request module
    for sess_coki in session.cookies:
        driver_templ_id.add_cookie({'name': sess_coki.name, 'value': sess_coki.value,
                                    'path': sess_coki.path, 'expiry': sess_coki.expires})
    #--------------------launching driver
    driver_templ_id.get("https://ehealthreminders.net/resources/home")
    wait = WebDriverWait(driver_templ_id, 20)
    wait.until(EC.presence_of_element_located((By.XPATH, ('/html/body/pre'))))
    #screenshot1
    driver_templ_id.get_screenshot_as_file(PATH_ADDRESS+"_"+str(UPIN_SS)+"_avail_res"+".png")
    temp_id = ['telemed_nl1', 'current_employee_nl5']
    for tmpx in temp_id:
        click_to_fwd = 0
    #---------------------checking_rec_campaigns
        r_3 = session.get("https://ehealthreminders.net/resources/home", cookies=r_1.cookies).text
        j = json.loads(r_3)
        click_to_fwd = 0
        for cmp_lst in range(0, len(j["campaignList"])):
            if j["campaignList"][cmp_lst]['templateId'] == tmpx:
                click_to_fwd = cmp_lst
                print "----------------"+str(cmp_lst)
                break
            else:
                click_to_fwd = -1
            print j["campaignList"][cmp_lst]['templateId']
    #---------------------taking_screenshot_of_wanted_campaigns
        if click_to_fwd >= 0:
            driver_templ_id.get("https://ehealthreminders.net/dashboard")
            wait = WebDriverWait(driver_templ_id, 20)
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, ('slider'))))
            count = 0
            while count < click_to_fwd:
                nextt_x = driver_templ_id.find_elements_by_class_name('slider-decorator-1')
                nextt_x[0].click()
                count = count+1
            time.sleep(1)
            #screenshot2
            scr_shot1 = PATH_ADDRESS+str(tmpx)+"_"+str(UPIN_SS)+"_log_first_screen"+".png"
            driver_templ_id.get_screenshot_as_file(scr_shot1)
            img_click = driver_templ_id.find_elements_by_class_name('slider-frame')
            img_click2 = img_click[0].find_elements_by_class_name('slider-list')
            img_click3 = img_click2[0].find_elements_by_class_name('slider-slide')
            img_click3[click_to_fwd].click()
            wait = WebDriverWait(driver_templ_id, 20)
            x_path = '//*[@id="container"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[2]/div/h1'
            wait.until(EC.presence_of_element_located((By.XPATH, (x_path))))
            #screenshot3
            driver_templ_id.get_screenshot_as_file(PATH_ADDRESS+str(tmpx)+"_"+
                                                   str(UPIN_SS)+"_clicked_screen"+".png")
        else:
            print str(tmpx)+"===Do not exsist"
    driver_templ_id.close()
THD_ONE = threading.Thread(target=tempx, kwargs={'UPIN_SS':"test1032cmprole3user1@evivehealth.com"},
                           name='test1032cmprole3user1@evivehealth.com')
THD_ONE.start()
THD_TWO = threading.Thread(target=tempx, kwargs={'UPIN_SS':"test1032cmprole1user1@evivehealth.com"},
                           name='test1032cmprole1user1@evivehealth.com')
THD_TWO.start()
THD_ONE.join()
THD_TWO.join()
print str(time.time()-START_TIME)+" seconds"
