#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 11:56:49 2018

@author: aayushbhargava
"""

import time
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformName'] = 'Android'
#desired_caps['platformVersion'] = '8.1'
desired_caps['platformVersion'] = '7.0'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['automationName']= 'UiAutomator2'
#desired_caps['appPackage'] = 'com.evivernappv0'
#capabilities.setCapability("fullReset", "false")
#desired_caps['app'] = '/Users/aayushbhargava/Downloads/myevive_v2.1.0_apkpure.com.apk'
desired_caps['app'] = '/Users/aayushbhargava/Downloads/app-release-6.apk'
print 'dfccd'
driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
time.sleep(10)

#                 /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]
username_xpth = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.EditText'
password_xpth = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.EditText'
signinfp_xpth = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[7]'
sidebarr_xpth = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup'
setting_xpth = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup'
passcode_switch = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.Switch'
enter_psasscode = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText'
passcode_submit = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]'

benquiz_scroll = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]'
benquiz_imclick = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[6]'
benquiz_imclick2 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[5]'
health_assessment = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]'
take_action_xpthh = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]'
start_xpth = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup'
option_ss = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]'
nextt_xpth = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]'
nexxtt_xpth = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]'
#/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]


setx=['8','9','8','7','7','6','8','8']
#client=['powerupmylife','travelers','ellucian','mister','newavon','usic','gapinc','davita']
client=['mywellbeing','mywellbeing','mywellbeing','mywellbeing']
uname=['test1039livongoxrole15user1@goevive.com','test1039livongoxrole16user1@goevive.com','test1039helloheartxrole15user1@goevive.com','test1039helloheartxrole16user1@goevive.com']

def touch_id():
    START_TIME = time.time()
    for x in range(0,8):
        print x
        try:
            el = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.EditText")
            el.send_keys(client[x])
            time.sleep(1)
            el = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]')
            el.click()
            time.sleep(7)
        except:
            print("sucessful")
        el = driver.find_element_by_xpath(username_xpth)
        el.send_keys(uname[x])
        el = driver.find_element_by_xpath(password_xpth)
        el.send_keys("jnejne")
        el = driver.find_element_by_xpath(signinfp_xpth)
        el.click()
        time.sleep(20)
        driver.reset()
        time.sleep(7)
        
'''
        element_name = [[signinfp_xpth, sidebarr_xpth, setting_xpth+'['+str(setx[x])+']', passcode_switch],[8,3,1,1]]
        for y in range(0,4):
            try:
                el = driver.find_element_by_xpath(element_name[0][y])
                el.click()
                time.sleep(element_name[1][y])
                driver.save_screenshot('/Users/aayushbhargava/Documents/evive/daily_prod_oct/passcode/'+'screen1.'+str(uname[x])+'.png')
            except:
                pass
        time.sleep(1)
        driver.save_screenshot('/Users/aayushbhargava/Documents/evive/daily_prod_oct/passcode/'+'screen2.'+str(uname[x])+'.png')
        el = driver.find_element_by_xpath(enter_psasscode).send_keys('5555')
        el = driver.find_element_by_xpath(passcode_submit).click()
        time.sleep(2)
        print "Total time to execute passcode: "+str(time.time()-START_TIME)+" seconds"
        driver.reset()
        time.sleep(7)
        #print "reset done"
'''

unamex = ['myevivepatterson','ups']
cli=['test1029401kuser6@evivehealth.com', 'test1037role4user9@evivehealth.com']
     #'test1037role4user10@evivehealth.com']
def bq():
    START_TIME = time.time()
    for x in range(0,2):
        try:
            el = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.EditText")
            el.send_keys(client[x])
            time.sleep(1)
            el = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]')
            el.click()
            time.sleep(7)
        except:
            print("sucessful")
        el = driver.find_element_by_xpath(username_xpth)
        el.send_keys(cli[x])
        el = driver.find_element_by_xpath(password_xpth)
        el.send_keys("jnecjn")
        if x==0:
            bqc=benquiz_imclick
        else:
            bqc=benquiz_imclick2
        element_name = [[signinfp_xpth, sidebarr_xpth, benquiz_scroll, bqc, health_assessment, take_action_xpthh, start_xpth],[8,3,5,15,2,5,2]]
        for y in range(0,7):
            try:
                if y==3 and x==0:
                    driver.swipe(100, 1800, 100, 150)
                el = driver.find_element_by_xpath(element_name[0][y])
                el.click()
                time.sleep(element_name[1][y])
            except:
                pass
        
        try:
            el = driver.find_element_by_xpath(option_ss)
            el.click()
            time.sleep(0.5)
            driver.save_screenshot('/Users/aayushbhargava/Documents/evive/daily_prod_oct/bq/'+str(x)+'app_primary'+'.png')
            driver.swipe(100, 1800, 100, 150)
            el1 = driver.find_element_by_xpath(nextt_xpth)
            el1.click()
            time.sleep(1)
        except:
            pass
        for xxx in range(0,20):
            try:
                el2 = driver.find_element_by_xpath(nexxtt_xpth)
                el2.click()
                el = driver.find_element_by_xpath(option_ss)
                el.click()
                print "clicked"
                driver.save_screenshot('/Users/aayushbhargava/Documents/evive/daily_prod_oct/bq/'+'patterson'+'app_quesno.'+str(xxx)+'.png')    
                driver.swipe(100, 1800, 100, 150,100)
                el2 = driver.find_element_by_xpath(nexxtt_xpth)
                el2.click()
                time.sleep(1)
                
            except:
                pass
    
        print "Total time to execute benifit quiz: "+str(time.time()-START_TIME)+" seconds"
        #driver.reset()
        time.sleep(7)
        print "reset done"


def nearby():
    START_TIME = time.time()
    for x in range(0,2):
        try:
            el = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.EditText")
            el.send_keys(client[x])
            time.sleep(1)
            el = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]')
            el.click()
            time.sleep(7)
        except:
            print("sucessful")
        el = driver.find_element_by_xpath(username_xpth)
        el.send_keys('test1035tbcampaignsuser6@goevive.com')
        el = driver.find_element_by_xpath(password_xpth)
        el.send_keys("jnecjn")
        
        allow= '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[2]'
        doc = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.ImageView'
        uc = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.widget.ImageView' 
        hospitals = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[3]/android.widget.ImageView'
        pharma = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[4]/android.widget.ImageView'
        producers = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[5]/android.widget.ImageView'

        element_name = [[signinfp_xpth, sidebarr_xpth, benquiz_scroll, doc, allow, uc, hospitals, pharma, producers],[8,3,5,2,7,7,7,7,7,7]]
        for y in range(0,10):
            try:
                el = driver.find_element_by_xpath(element_name[0][y])
                el.click()
                time.sleep(element_name[1][y])
                if y>3:
                    driver.save_screenshot('/Users/aayushbhargava/Documents/evive/daily_prod_feb/nearby/'+'1035_'+'nearby._'+str(y)+'.png')
                    driver.back()
                    time.sleep(3)
            except:
                pass
            
    time.sleep(19)
        
    

'''
doc = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.ImageView'
uc = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.widget.ImageView' 
/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup'
/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.ImageView

hospitals = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[3]/android.widget.ImageView'
pharma = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[4]/android.widget.ImageView'
producers = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[5]/android.widget.ImageView'
'''
nearby()
#bq()
#need_launch()str(unamex[x]
#touch_id()