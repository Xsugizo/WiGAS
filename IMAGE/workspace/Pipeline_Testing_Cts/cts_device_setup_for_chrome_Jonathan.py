#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import uiautomator2 as u2
import time
import os
import sys
from multiprocessing import Process



def get_devices_serials():
    s_num=sys.argv
    del s_num[0]
    series=s_num
    print(series)
    
    if len(series)!=0:
        return series
        
    else:
        fd = os.popen("adb devices")
        devices_list_src = fd.readlines()#返回list
        fd.close()
        for device in devices_list_src:
            if "device\n" in device:
                device = device.replace("\tdevice\n","")
                series.append(device)
        return series


def wizard_step(serial):
    print("run cts_device_setup_for_chrome_Jonathan")
    os.system("python3 -m uiautomator2 init  --serial %s"%serial)
    d = u2.connect(serial)
    # d.dump_hierarchy()
    # d.healthcheck()
    d.uiautomator.start() # 启动

    print(d.info)
    #main function
    try:
        # d(resourceId="com.google.android.setupwizard:id/start").wait()
        # d(resourceId="com.google.android.setupwizard:id/start").click()
        time.sleep(5)
        print('Start')
        if d(text='Start').exists:
            print('find Start')
            d(text="Start").click()
        # else:
        #     reset_devie_status(serial)
        time.sleep(1)
        if d(text='Skip').exists:
            print('push skip')
            d(text="Skip").click()
        time.sleep(1)
        if d(text="Set up offline").exists:
            print('Set up offline')
            d(text="Set up offline").click()
        time.sleep(1)
        if d(resourceId="android:id/button1").exists:
            print('push button')
            d(resourceId="android:id/button1").click()
        time.sleep(5)
        if d(text='Next').exists:
            print('push next')
            d(text="Next").click()
        time.sleep(1)
        for _ in range(2):
            print('push more')
            d(text="More").click()
        time.sleep(1)
        d(text="Accept").click()
        time.sleep(4)
        if d(text='Set a PIN').exists:
            print("find Set a PIN")
            time.sleep(2)
            if d(text='Skip').exists:
                print('push skip')
                d(text='Skip').click()
            time.sleep(2)
            if d(text='Skip anyway').exists:
                print('push skip anyway')
                d(text='Skip anyway').click()
            time.sleep(5)
        else:
            
            if d(resourceId="android:id/title", text="Not now").exists:
                print('push not now')
                d(resourceId="android:id/title", text="Not now").click()
            if d(resourceId="android:id/button1").exists:
                print('push button')
                d(resourceId="android:id/button1").click()
            time.sleep(30)
        os.system('adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X shell settings put global stay_on_while_plugged_in 3')
        time.sleep(1)
        d.app_start("com.android.settings",".Settings$WifiSettings2Activity")
        time.sleep(1)
        d(text="B13F-2Q05-GMS").click()
        time.sleep(1)
        # d.send_keys("8888800000")
        d.shell("input text 8888800000")
        time.sleep(1)
        # d(text="CONNECT").click()
        d.xpath('//*[@resource-id="com.google.android.inputmethod.latin:id/key_pos_ime_action"]/android.widget.FrameLayout[1]/android.widget.ImageView[1]').click()
        time.sleep(10)
        os.system("adb -s %s shell am start -n 'com.android.settings/.Settings\$MyDeviceInfoActivity'"%serial) # set stay awake to true 
        time.sleep(2)

        os.system("adb -s %s shell settings put global development_settings_enabled 1"%serial) # set stay awake to true 
        time.sleep(1)
        # d(scrollable=True).scroll.to(text="Build number")
        # for _ in range(10):
        #     d(text="Build number").click()
        # time.sleep(3)
        # while True:
        #     print ('serial=',serial)
        #     d(scrollable=True).scroll.to(text="Build number")
        #     time.sleep(8)
        #     if d(text="Build number").exists:
        #         for _ in range(10):
        #             if d(text="Build number").exists:
        #                 print("Build number")
        #                 d(text="Build number").click()
        #             else:
        #                 print('Build number somthing happend')
        #                 os.system('adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X shell input keyevent 3') # Home鍵
        #                 time.sleep(1)
        #                 d.app_clear("com.android.settings")
        #                 time.sleep(5)
        #                 d.shell("am start -n com.android.settings/.Settings\$MyDeviceInfoActivity") # set stay awake to true 
        #                 time.sleep(5)
        #                 # os.system("adb -s %s shell am start -n 'com.android.settings/.Settings\$MyDeviceInfoActivity'"%serial) # set stay awake to true 
        #                 break
        #         break
        #     else:
        #         print("cannot find build number ")
        #         os.system('adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X shell input keyevent 3') # Home鍵

        #         time.sleep(1)
        #         d.app_clear("com.android.settings")
        #         time.sleep(5)

        #         d.shell("am start -n com.android.settings/.Settings\$MyDeviceInfoActivity") # set stay awake to true 
        #         time.sleep(5)

                # os.system("adb -s %s shell am start -n 'com.android.settings/.Settings\$MyDeviceInfoActivity'"%serial) # set stay awake to true 


        # os.system("adb -s %s shell am start -n 'com.android.settings/.Settings\$DevelopmentSettingsDashboardActivity'"%serial) # set stay awake to true 
        d.shell("am start -n com.android.settings/.Settings\$DevelopmentSettingsDashboardActivity") # set stay awake to true 

        # d(scrollable=True).scroll.to(text="Stay awake")
        # if d(text="Stay awake").exists:
        #     d(text="Stay awake").click()
        time.sleep(5)

        while True:
            print("serial=",serial)
            d(scrollable=True).scroll.to(text="Allow Mock Modem")
            time.sleep(8)
            # d(text="Allow Mock Modem").wait(timeout=5.0)
            
            if d(text="Allow Mock Modem").exists:
                print("find the Allow Mock Modem and enabled ")
                d(text="Allow Mock Modem").click()
                d.press('home')
                break
            else:
                print("cannot find Allow Mock Modem ")

                os.system('adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X shell input keyevent 3') # Home鍵
                d.app_clear("com.android.settings")
                time.sleep(5)
                d.shell("am start -n com.android.settings/.Settings\$DevelopmentSettingsDashboardActivity") # set stay awake to true 

                # os.system("adb -s %s shell am start -n 'com.android.settings/.Settings\$DevelopmentSettingsDashboardActivity'"%serial) # set stay awake to true 

                # os.system("adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X shell pm uninstall -k --user 0 com.github.uiautomator")
                # os.system("python3 -m uiautomator2 init  --serial %s"%serial)
                # print(serial +" devices refind Allow Mock Mode begin")
                # d = u2.connect(serial)
                time.sleep(5)
        
        # d(scrollable=True).scroll.to(text="Allow Mock Modem")

        # if d(text="Allow Mock Modem").exists:
        #     print('find Allow Mock Modem and enabled ')
        #     # d(text="Allow Mock Modem").wait()
        #     d(text="Allow Mock Modem").click()
        # time.sleep(10)
        # d.press('home')
        os.system("adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X shell pm uninstall -k --user 0 com.github.uiautomator")
        return 1
    except:
        print('wizard_step exception')
        return 0
        # reset_devie_status(serial)
        # start_element(serial)
        # wizard_step(serial)
#----------------------------------
def reset_devie_status(serial):
    os.system("./Factory_Reset.sh -s %s"%serial)
    time.sleep(100)
    k=wizard_step(serial) #wizard setup
    print ('k= ', k)
    if k==1:
        p=start_element(serial)
    else:
        p=1
    return p
    # os.system("./CAD_test.py --name %s"%serial)#device setup for test




#---------------------

count=0
print("setting chrome begin")
def start_element(serial):
    global count
    os.system("python3 -m uiautomator2 init  --serial %s" %serial)
    d = u2.connect(serial)
    # d.dump_hierarchy()
    # d.healthcheck()
    #main function
    try:
        os.system('adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X shell settings put global stay_on_while_plugged_in 3')
        time.sleep(10)
        if d(resourceId="com.android.chrome:id/fre_logo").exists:
            print('in chrome setting page')
        elif d(resourceId="com.android.chrome:id/image").exists:
            print('in chrome setting page')
        else:
            print ("screen on")
            d.screen_on()
            time.sleep(10)
            print (" home key")
            os.system('adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X shell input keyevent 3') # Home鍵
            
            time.sleep(10)
            print ("push Chrome")
            # d(text='Chrome').wait()
            if d(text='Chrome').exists:
                d(text='Chrome').click()
            else:
                os.system('adb -s %s shell am start -n com.android.chrome/com.google.android.apps.chrome.Main'%serial) # open GMS chrome 
        time.sleep(4)
        
        if d(resourceId="com.android.chrome:id/terms_accept").exists:
            # d(resourceId="com.android.chrome:id/terms_accept").wait(timeout=8.0)
            d(resourceId="com.android.chrome:id/terms_accept").click()
        
        elif d(resourceId="com.android.chrome:id/fre_bottom_group").exists:
            # d(resourceId="com.android.chrome:id/fre_bottom_group").wait(timeout=8.0)
            d(resourceId="com.android.chrome:id/fre_bottom_group").click()
            
        elif d(resourceId="com.android.chrome:id/signin_fre_dismiss_button").exists:
            # d(resourceId="com.android.chrome:id/fre_bottom_group").wait(timeout=8.0)
            d(resourceId="com.android.chrome:id/signin_fre_dismiss_button").click()

        else:
            print('Cannot find accept button ')
            return 1
            # global count
            # count=count+1
            # print('count:',count)
            # if count>=1:
            #     ans = input('do you wnat to factory reset  y or n')
            #     print (ans)
            #     if ans == "y":
            #         print (ans)

                    # reset_devie_status(serial)

        time.sleep(3)
        if d(resourceId="com.android.chrome:id/negative_button").exists:
            print("push negative_button")
            d(resourceId="com.android.chrome:id/negative_button").click()
            time.sleep(3)
            #d.press('home')
            os.system('adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X shell input keyevent 3') #home鍵
            time.sleep(3)
            os.system("adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X shell pm uninstall -k --user 0 com.github.uiautomator")
            #os.system("adb shell pm uninstall -k com.github.uiautomator")
        return 2
    except:

        count=count+1
        print('exception happen need to re-processing again')
        # print('count:',count)
        return 0
        # if count>=1:
        #     val= input('I Cannot find accept button, do you wnat to factory reset ? Y or N')
        #     if val=="y":
        #         reset_devie_status(serial)
        #     else:
        #         print('refind chrome icon')
        #         start_element(serial)
        
if __name__ == "__main__":
    process_list = []
    serial_list = get_devices_serials()
    # for index in range( len(serial_list) ):
        #創建子進程執行start_element()的函數
    # p = Process( target=start_element, args=( serial_list[0],  ) )
    p=start_element(serial_list[0])
    # p.start()
    while True:
        print('p=',p)
        print('factroty reset :',count ,'times to push accept button')

        count=count+1
        if p==1:
            # ans=input("factroy reset y/n ?")
            # if ans=="y":
            print("facrtory reset find chrome accept button")
            p=reset_devie_status(serial_list[0])
            # else:
            #     print('refind chrome icon')
            #     p=start_element(serial_list[0])
        if p==0:
            ans=input("exception happen need to re-processing again y/n ?")
            if ans=="y":
                # p=reset_devie_status(serial_list[0])
                p=start_element(serial_list[0])
            else:
                print("terminate find chrome accept button processing")
                break
        if p is None:
            break 
        if p==2:
            print('p=',p)
            print('factroty reset :',count ,'times to push accept button')

            break 

    #     process_list.append(p)
    # for p in process_list:
    #     p.join()
    print("all task done!")

