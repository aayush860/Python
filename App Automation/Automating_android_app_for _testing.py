#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 16:08:13 2018

@author: aayushbhargava5037
4723
"""


import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


desired_caps = {}
desired_caps['platformName'] = 'Android'
#desired_caps['platformName'] = 'Android'
#desired_caps['platformVersion'] = '8.1'
desired_caps['platformVersion'] = '7.0'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['automationName']= 'UiAutomator2'
#desired_caps['appPackage'] = 'com.evivernappv0'
#capabilities.setCapability("fullReset", "false")
#desired_caps['app'] = '/Users/aayushbhargava/Downloads/myevive_v2.1.0_apkpure.com.apk'
desired_caps['app'] = '/Users/aayushbhargava/Downloads/app-release-6.apk'
driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)

time.sleep(10)
username_xpth = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.EditText'
password_xpth = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.EditText'
                
signinfp_xpth = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]'
sidebarr_xpth = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]'
setting_xpth = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup'
#setting_usic_xpth = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[6]'
setting_usic_xpth = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[7]'
currents_xpth = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.HorizontalScrollView/android.view.ViewGroup'
serchtxt_xpth = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.EditText'
trblerrr_xpth = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button'
logout_for_aa = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[7]'
toolkit_fro_ptrson = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]'
retirement_calc = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]'
nextbutton_rec = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[1]'
in_nextbutton_rec = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[2]'
benquiz_scroll = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]'
benquiz_imclick = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]'
health_assessment = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]'
take_action_xpthh = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]'
start_xpth = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup'
option_ss = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]'
nextt_xpth = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]'
nexxtt_xpth = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]'
passcode_switch = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.Switch'
enter_psasscode = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText'
passcode_submit = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]'

account_details = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup'
privacy_switch = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]'
terms_switch = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]'
about_switch = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[3]'
passcode = ''
helpcenter = ''


toolkit_ellucian_xpth = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]'
stress_bus_xpth = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]'
stress_take_xpth = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[4]/android.widget.Button'
stress_strt_xpth = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[9]/android.view.View/android.view.View[1]'
stress_2nd_xpth = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[9]/android.view.View/android.view.View[1]'
def tilllogin():
    try:
        
        el = driver.find_element_by_class_name("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.EditText")
        el.send_keys("gapinc")
        time.sleep(1)
        el = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]')
        el.click()
        time.sleep(3)
        el = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView')
        el.click()
        time.sleep(7)
    except:
        print("sucessful")
    el = driver.find_element_by_xpath(username_xpth)
    el.send_keys("test1049dbluser4@goevive.com")
    el = driver.find_element_by_xpath(password_xpth)
    el.send_keys("knjnjkj")
    el = driver.find_element_by_xpath(signinfp_xpth)
    el.click()
    time.sleep(8)
    
    el = driver.find_element_by_xpath(sidebarr_xpth)
    el.click()
    time.sleep(3)
##############################################################################

def deductibles():
    START_TIME = time.time()
    tilllogin()
    driver.tap([(400,870)], 900)
    time.sleep(3)
    driver.save_screenshot('/Users/aayushbhargava/Documents/evive/daily_prod_checkout/deductibles/' + 'sc1_app.png')
    el = driver.find_element_by_xpath(sidebarr_xpth)
    el.click()
    time.sleep(1)
    print "Total time to execute deductibles: "+str(time.time()-START_TIME)+" seconds"
##############################################################################

def help_Center():
    START_TIME = time.time()
    tilllogin()
    driver.tap([(340,1575)], 900)
    time.sleep(2)
    driver.save_screenshot('/Users/aayushbhargava/Documents/evive/daily_prod_oct/helpcenter/' + 'homescreen.png')
    
    for x in range(1,4):
        el = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup['+str(x)+']')
        el.click()
        time.sleep(2.3)
        driver.save_screenshot('/Users/aayushbhargava/Documents/evive/daily_prod_oct/helpcenter/' + 'sc1_app'+str(x)+'.png')
        el = driver.find_element_by_xpath('//android.widget.Button[@content-desc="Help Center"]')
        el.click()
        time.sleep(2)
        
    el = driver.find_element_by_xpath(serchtxt_xpth)
    el.send_keys('can')
    driver.keyevent(67)
    driver.save_screenshot('/Users/aayushbhargava/Documents/evive/daily_prod_checkout/helpcenter/' + 'searchscreen.png')
    print "Total time to execute help_center: "+str(time.time()-START_TIME)+" seconds"
##############################################################################
    
def getmytoken():
    START_TIME = time.time()
    tokenlist = ["americanairlines","myeviveaa"]
    userlist = ["test1013migraineuser1@evivehealth.com","test1013migraineuser2@evivehealth.com"]
# "americanaa",               ,"test1013migraineuser2@evivehealth.com"]
    for token in tokenlist:
        el = driver.find_element_by_class_name("android.widget.EditText")
        el.send_keys(token)
        time.sleep(1)
        el = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]')
        el.click()
        time.sleep(3)
        try:
            el = driver.find_element_by_xpath(trblerrr_xpth)
            driver.save_screenshot('/Users/aayushbhargava/Documents/evive/daily_prod_oct/getmytoken/'+'_falsetoken.png')
            el.click()
            time.sleep(2)
        except:
            pass
    time.sleep(4)
    for use in userlist:
        el = driver.find_element_by_xpath(username_xpth)
        el.send_keys(use)
        el = driver.find_element_by_xpath(password_xpth)
        el.send_keys("knjnjkj")
        driver.save_screenshot('/Users/aayushbhargava/Documents/evive/daily_prod_oct/getmytoken/'+use+'_truetoken.png')
        el = driver.find_element_by_xpath(signinfp_xpth)
        el.click()
        time.sleep(7)
        print("getmytoken fully executed")
        el = driver.find_element_by_xpath(sidebarr_xpth)
        el.click()
        time.sleep(3)
        driver.save_screenshot('/Users/aayushbhargava/Documents/evive/daily_prod_oct/getmytoken/' +use+'_loginacvepted.png')
        el = driver.find_element_by_xpath(logout_for_aa)
        el.click()
        time.sleep(4)
    print "Total time to execute get_my_token: "+str(time.time()-START_TIME)+" seconds"
###############################################################################    


def retirementcalc():
    START_TIME = time.time()
    try:
        print 'x:70 y:137into it!!!!!!!!!!!!!!!!!'
        el = driver.find_element_by_accessibility_id('9408f084-88cf-4e93-b814-4714dd94e5eb')
        #el = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.EditText")
#                                         /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.EditText
        el.send_keys("myevivepatterson")
        #time.sleep(3)
        #element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]")))
        el = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]')
        el.click()
        
        time.sleep(4)
        el = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView')
        el.click()
        time.sleep(7)
    except:
        print("sucessful")
    el = driver.find_element_by_xpath(username_xpth)
    el.send_keys("test1003csuser6@goevive.com")
    el = driver.find_element_by_xpath(password_xpth)
    el.send_keys("knjnjkj")
    element_name = [[signinfp_xpth, sidebarr_xpth],[8,3]]
    for y in range(0,7):
        try:
            if y==2:
                driver.tap([(70,135)],900)
                break
            el = driver.find_element_by_xpath(element_name[0][y])
            el.click()
            time.sleep(element_name[1][y])
        except:
            pass
    el = driver.find_element_by_accessibility_id('Tool Kit')
    el.click()
    time.sleep(2)
    el = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]')
    el.click()
    time.sleep(1)
    driver.save_screenshot('/Users/aayushbhargava/Documents/evive/daily_prod_feb/retirement_calculator/'+'_1st_april_screen_primary.png')
    for x in range(0,8):
        el = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[8]')
        el.click()
        time.sleep(2)
        driver.save_screenshot('/Users/aayushbhargava/Documents/evive/daily_prod_feb/retirement_calculator/'+'_1st_april_screenno.'+str(x)+'.png')    
    print "Total time to execute retirement_calculator: "+str(time.time()-START_TIME)+" seconds"

###############################################################################    


def ben_quiz():
    START_TIME = time.time()
    try:
        el = driver.find_element_by_class_name("android.widget.EditText")
        el.send_keys("usic")
        time.sleep(1)
        el = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]')
        el.click()
        time.sleep(7)
    except:
        print("sucessful")
    el = driver.find_element_by_xpath(username_xpth)
    el.send_keys("test1048regressionsuser3@goevive.com")
    el = driver.find_element_by_xpath(password_xpth)
    el.send_keys("knjnjkj")
    element_name = [[signinfp_xpth, sidebarr_xpth, benquiz_scroll, benquiz_imclick, health_assessment, take_action_xpthh, start_xpth],[8,3,5,5,2,5,2]]
    for y in range(0,7):
        try:
            el = driver.find_element_by_xpath(element_name[0][y])
            el.click()
            time.sleep(element_name[1][y])
        except:
            pass
    try:
        el = driver.find_element_by_xpath(option_ss)
        el.click()
        time.sleep(0.5)
        driver.save_screenshot('/Users/aayushbhargava/Documents/evive/daily_prod_checkout/benifit_quiz/'+'app_primary'+'.png')
        driver.swipe(100, 1800, 100, 150)
        el = driver.find_element_by_xpath(nextt_xpth)
        el.click()
        time.sleep(1)
    except:
        pass
            

    for x in range(0,20):
        try:
            el = driver.find_element_by_xpath(option_ss)
            el.click()
            time.sleep(0.5)
            driver.save_screenshot('/Users/aayushbhargava/Documents/evive/daily_prod_checkout/benifit_quiz/'+'app_quesno.'+str(x)+'.png')    
            driver.swipe(100, 1800, 100, 150)
            el = driver.find_element_by_xpath(nexxtt_xpth)
            el.click()
            time.sleep(1)
            
        except:
            pass

    print "Total time to execute benifit quiz: "+str(time.time()-START_TIME)+" seconds"
            

def touch_id():
    START_TIME = time.time()
    try:
        el = driver.find_element_by_class_name("android.widget.EditText")
        el.send_keys("mister")
        time.sleep(1)
        el = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]')
        el.click()
        time.sleep(7)
    except:
        print("sucessful")
    el = driver.find_element_by_xpath(username_xpth)
    el.send_keys("test1046regressionsuser2@goevive.com")
    el = driver.find_element_by_xpath(password_xpth)
    el.send_keys("knjnjkj")
    element_name = [[signinfp_xpth, sidebarr_xpth, setting_xpth, passcode_switch],[8,3,1,1]]
    for y in range(0,4):
        try:
            el = driver.find_element_by_xpath(element_name[0][y])
            el.click()
            time.sleep(element_name[1][y])
            driver.save_screenshot('/Users/aayushbhargava/Documents/evive/daily_prod_oct/passcode/'+'screen1.'+str(y)+'.png')
        except:
            pass
    time.sleep(1)
    driver.save_screenshot('/Users/aayushbhargava/Documents/evive/daily_prod_oct/passcode/'+'screen1.'+'.png')
    el = driver.find_element_by_xpath(enter_psasscode).send_keys('5555')
    el = driver.find_element_by_xpath(passcode_submit).click()
    time.sleep(2)
    print "Total time to execute passcode: "+str(time.time()-START_TIME)+" seconds"

def settings():
    START_TIME = time.time()
    try:
        print 'x:70 y:137into it!!!!!!!!!!!!!!!!!'
        el = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.EditText")
#        /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.EditText
        el.send_keys("gapinc")
        #time.sleep(3)
        #element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]")))
        el = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]')
        el.click()
        
        time.sleep(4)
        el = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView')
        el.click()
        time.sleep(7)
    except:
        print("sucessful")
    el = driver.find_element_by_xpath(username_xpth)
    el.send_keys("test1048regressionsuser3@goevive.com")
    el = driver.find_element_by_xpath(password_xpth)
    el.send_keys("knjnjkj")
    element_name = [[account_details,signinfp_xpth, sidebarr_xpth],[8,3]]
    for y in range(0,7):
        try:
            if y==2:
                driver.tap([(70,135)],900)
                break
            el = driver.find_element_by_xpath(element_name[0][y])
            el.click()
            time.sleep(element_name[1][y])
        except:
            pass
    time.sleep(1)
    el = driver.find_element_by_accessibility_id('Account')
    el.click() 
    time.sleep(1)
    driver.save_screenshot('/Users/aayushbhargava/Documents/evive/daily_prod_feb/settings/'+'screen1.'+'_29_march_'+str(y)+'.png')
    element_name = [privacy_switch,terms_switch,about_switch]
    for x in range(0,7):
        try:
            el = driver.find_element_by_xpath(element_name[x])
            el.click()
            time.sleep(4)
            driver.save_screenshot('/Users/aayushbhargava/Documents/evive/daily_prod_feb/settings/'+'screen1.'+'_29_march_'+str(x)+'.png')
            driver.back()
        except:
            pass
    driver.back()
    print "Total time to execute passcode: "+str(time.time()-START_TIME)+" seconds"


def camp():
    START_TIME = time.time()
    try:
        el = driver.find_element_by_class_name("android.widget.EditText")
        el.send_keys("myevivepatterson")
        time.sleep(1)
        el = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]')
        el.click()
        time.sleep(7)
    except:
        print("sucessful")
    el = driver.find_element_by_xpath(username_xpth)
    el.send_keys("test1029regressionsuser5@goevive.com")
    el = driver.find_element_by_xpath(password_xpth)
    el.send_keys("knjnjkj")
    element_name = [[signinfp_xpth ],[8]]
    for y in range(0,1):
        try:
            el = driver.find_element_by_xpath(element_name[0][y])
            el.click()
            time.sleep(element_name[1][y])
        except:
            pass
    time.sleep(15)
    for x in range(0,3):
        driver.save_screenshot('/Users/aayushbhargava/Documents/evive/daily_prod_oct/CAMP/'+str(x)+'.png')
        if x==1:
            time.sleep(7)
        else:
            time.sleep(3)
    print "Total time to execute camp: "+str(time.time()-START_TIME)+" seconds"

def stress():
    print "Executing stress"
    START_TIME = time.time()
    try:
        el = driver.find_element_by_class_name("android.widget.EditText")
        el.send_keys("ellucian")
        time.sleep(1)
        el = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]')
        el.click()
        time.sleep(7)
    except:
        print("sucessful")
    el = driver.find_element_by_xpath(username_xpth)
    el.send_keys(" ")
    el = driver.find_element_by_xpath(password_xpth)
    el.send_keys("knjnjkj")
    element_name = [[signinfp_xpth, sidebarr_xpth, toolkit_ellucian_xpth, stress_bus_xpth],[9,4,4,9]]
    for y in range(0,7):
        try:
            el = driver.find_element_by_xpath(element_name[0][y])
            el.click()
            time.sleep(element_name[1][y])
            if y==2:
                driver.save_screenshot('/Users/aayushbhargava/Documents/evive/daily_prod_oct/stress/'+'a'+'.png')
        except:
            pass
    try:
        driver.save_screenshot('/Users/aayushbhargava/Documents/evive/daily_prod_oct/stress/'+'x'+'.png')
        driver.swipe(100, 1800, 100, 150)
        driver.save_screenshot('/Users/aayushbhargava/Documents/evive/daily_prod_oct/stress/'+'y'+'.png')
    except:
        time.sleep(5)
        driver.save_screenshot('/Users/aayushbhargava/Documents/evive/daily_prod_oct/stress/'+'x'+'.png')
        driver.swipe(100, 1800, 100, 150)
        driver.save_screenshot('/Users/aayushbhargava/Documents/evive/daily_prod_oct/stress/'+'y'+'.png')

    driver.swipe(100, 500, 100, 1800)
    time.sleep(1)
    el = driver.find_element_by_xpath(stress_take_xpth)
    el.click()
    time.sleep(2)
    tap_coordinates = [(800,1150),(519,1188),(519,1188),(365,1057),(523,1281),(321,1262),(933,995),(557,1339),(813,1065),(557,1337),(859,979),(557,1337),(557,1293)]
    count = 0
    for tapping in tap_coordinates:
        driver.tap([tapping], 900)
        print "tap function executed"      
        if count>1:
            time.sleep(1.2)
        else:
            time.sleep(5)
        driver.save_screenshot('/Users/aayushbhargava/Documents/evive/daily_prod_oct/stress/'+str(tapping)+'.png')
        count=count+1
    print "Total time to execute camp: "+str(time.time()-START_TIME)+" seconds"


def img_upload():
    START_TIME = time.time()
    try:
        el = driver.find_element_by_class_name("android.widget.EditText")
        el.send_keys("mister")
        time.sleep(1)
        el = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]')
        el.click()
        time.sleep(7)
    except:
        print("sucessful")
    el = driver.find_element_by_xpath(username_xpth)
    el.send_keys("test1046regressionsuser2@goevive.com")
    el = driver.find_element_by_xpath(password_xpth)
    el.send_keys("knjnjkj")
    element_name = [[signinfp_xpth, sidebarr_xpth],[8,3]]
    for y in range(0,7):
        try:
            el = driver.find_element_by_xpath(element_name[0][y])
            el.click()
            time.sleep(element_name[1][y])
        except:
            pass
    print "now"
    time.sleep(25)
    driver.save_screenshot('/Users/aayushbhargava/Documents/evive/daily_prod_oct/img_upload/'+"screenshotxx"+'.png')
    print "Total time to execute img_upload: "+str(time.time()-START_TIME)+" seconds"


def loginxxx():
    START_TIME = time.time()
    try:
        el = driver.find_element_by_class_name("android.widget.EditText")
        el.send_keys("myevivelowes")
        time.sleep(1)
        el = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]')
        el.click()
        time.sleep(7)
    except:
        print("sucessful")
    el = driver.find_element_by_xpath(username_xpth)
    el.send_keys("test1020appsmokecrole3@evivehealth.com")
    el = driver.find_element_by_xpath(password_xpth)
    el.send_keys("knjnjkj")
    element_name = [[signinfp_xpth, sidebarr_xpth],[8,3]]
    for y in range(0,7):
        try:
            el = driver.find_element_by_xpath(element_name[0][y])
            el.click()
            time.sleep(element_name[1][y])
        except:
            pass
    print "Total time to execute img_upload: "+str(time.time()-START_TIME)+" seconds"

#camp()
#img_upload()

    #loginxxx()
#stress()    
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx   will need relaunch
#touch_id()

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx   will need relaunch
    #ben_quiz()

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx   will need relaunch
#getmytoken()

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx   will need relaunch
retirementcalc()
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#deductibles()
#help_Center()

#xxxxxxxxxxxxxxxxxxxxxxxxxxx
#settings()




'''
4,6
800,1150
:{"x":519,"y":1188}
logout_for_aa = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[7]'
/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[4]/android.widget.Button

240 1556
error_xpth = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button'
search text=/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.EditText
#un==/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.EditText
#pd==/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.EditText
/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[6]/android.view.ViewGroup[0]
x=400
y=870
890,1546

'''