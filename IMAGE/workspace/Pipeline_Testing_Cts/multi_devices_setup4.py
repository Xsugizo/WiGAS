#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from re import X
from this import s
from pandas import Series
import uiautomator2 as u2
from multiprocessing import Process
import sys
import time
import yaqing
d_count=None
dis_devices=[]
series=[]

def get_devices_serials():
    s_num=sys.argv
    del s_num[0]
    series=s_num
    print(series)
    
    if len(series)!=0:
        return series
        
    else:
        #devices_list = []
        fd = os.popen("adb devices")
        devices_list_src = fd.readlines()#返回list
        fd.close()
        for device in devices_list_src:
            if "device\n" in device:
                device = device.replace("\tdevice\n","")
                series.append(device)
        return series


count=0
def start_element(serial):
    global count
    
    # os.system("adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X shell pm uninstall -k --user 0 com.github.uiautomator")
    print("multi_devices_setup_A13")
    os.system("python3 -m uiautomator2 init  --serial %s"%serial)
    print(serial +" devices setup begin")
    d = u2.connect(serial)
    
    # d.uiautomator.stop()
    # d.uiautomator.start() # 启动
    # d.uiautomator.running() # 是否在运行
    # print("devices setup begin")
    # print("d.dump_hierarchy()")
    # d.dump_hierarchy()
    # d.healthcheck()
    print(d.info)
    #main function
    try:
        
        
        d.screen_on()
        # os.system('adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X shell input keyevent 3') # Home鍵

        # d(resourceId="com.google.android.setupwizard:id/start").wait()
        # d(resourceId="com.google.android.setupwizard:id/start").click()
        time.sleep(5)
        # for _ in range(10):
        #     d(text="Start").click()
        # time.sleep(1)
        if d(text='Start').exists:
            print('find Start')
            d(text="Start").click()
        else:
            print('ignore Start')
        # else:
        #     os.system("./Factory_Reset.sh -s %s"%serial)
        #     time.sleep(100)
        #     start_element(serial)
        
        # # d(text='Start', className='android.widget.Button').click()
        # time.sleep(1)
        # if d(text="Start").exists:
        #     d(text="Start").click()
        # time.sleep(1)
        time.sleep(2)
        if d(text='Skip').exists:
            print('push Skip')
            d(text="Skip").click()
        else:
            print('ignore skip')
        time.sleep(3)
        if d(text='Set up offline').exists:
            print('Set up offline')
            d(text="Set up offline").click()
        else:
            print('ignore set up offline')
        time.sleep(2)
        if d(resourceId="android:id/button1").exists:
            print('push button')
            d(resourceId="android:id/button1").click()
        else:
            print('ignore push button')
        time.sleep(5)
        if d(text='Next').exists:
            print('push next')
            d(text="Next").click()
        else:
            print('ignore push next')
        time.sleep(2)
        # while d(text='More').exists:
            # print('Finded !')
            # d(text="More").click()
        for _ in range(2):
            if d(text="More").exists:
                print('push More')
                d(text="More").click()
            else:
                print('ignore pusg More')
                break
        time.sleep(1)
        if d(text="Accept").exists:
            print('push Accept')
            d(text="Accept").click()
        else:
            print('ignore Accepet')
        time.sleep(4)
        if d(text='Set a PIN').exists:
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
        time.sleep(2)
        d.app_start("com.android.settings",".Settings$WifiSettings2Activity")

        time.sleep(2)
        print("wifi-setting")
        if d(text="B13F-2Q05-GMS").exists:
            d(text="B13F-2Q05-GMS").click()
            time.sleep(1)
            # d.send_keys("8888800000")
            print("input password")
            d.shell("input text 8888800000")
            time.sleep(1)
        # d(text="CONNECT").click()
        d.xpath('//*[@resource-id="com.google.android.inputmethod.latin:id/key_pos_ime_action"]/android.widget.FrameLayout[1]/android.widget.ImageView[1]').click()
        time.sleep(5)
        d.app_clear("com.android.settings")
        # d.app_start("com.android.settings",".Settings\$MyDeviceInfoActivity") # d.app

        # os.system("adb -s %s shell am start -n 'com.android.settings/.Settings\$MyDeviceInfoActivity'"%serial) 
        d.shell("am start -n com.android.settings/.Settings\$MyDeviceInfoActivity") # set stay awake to true 

        time.sleep(5)

        dut=serial

        while True:
            print ('serial=',dut)
            d(scrollable=True).scroll.to(text="Build number")
            time.sleep(8)
            if d(text="Build number").exists:
                for _ in range(10):
                    if d(text="Build number").exists:
                        print("Build number")
                        d(text="Build number").click()
                    else:
                        print('Build number somthing happend')
                        p=1
                        break

                break

            else:
                print("cannot find build number ")
                p=1
                # os.system("adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X shell pm uninstall -k --user 0 com.github.uiautomator")
                # os.system("python3 -m uiautomator2 init  --serial %s"%dut)
                # print(dut +" devices refind build number begin")
                # d = u2.connect(dut)
                # time.sleep(3)
                # d.press('down')
                # os.system("adb -s %s shell am kill 'com.android.settings/.Settings\$MyDeviceInfoActivity'"%serial) # set stay awake to true 
                # time.sleep(5)
                os.system('adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X shell input keyevent 3') # Home鍵

                time.sleep(1)
                d.app_clear("com.android.settings")
                time.sleep(5)

                d.shell("am start -n com.android.settings/.Settings\$MyDeviceInfoActivity") # set stay awake to true 
                time.sleep(5)


        # return p
           
        # os.system("adb -s %s shell am kill 'com.android.settings/.Settings\$MyDeviceInfoActivity'"%serial) # set stay awake to true 
        # d.app_start("com.android.settings",".Settings\$DevelopmentSettingsDashboardActivity") # d.app

        d.shell("am start -n com.android.settings/.Settings\$DevelopmentSettingsDashboardActivity") # set stay awake to true 
        
        # d(scrollable=True).scroll.to(text="Stay awake")
        # if d(text="Stay awake").exists:
        #     d(text="Stay awake").click()    # time.sleep(90)
    # print("sleep 90 sec")
        while True:
            print("serial=",serial)
            d.dump_hierarchy()
            d(scrollable=True).scroll.to(text="Allow Mock Modem")
            time.sleep(8)
            # d(text="Allow Mock Modem").wait(timeout=5.0)
            
            if d(text="Allow Mock Modem").exists:
                print("find the Allow Mock Modem and enabled ")
                d(text="Allow Mock Modem").click()
                d.press('home')
                p=2
                break

            else:
                print("cannot find Allow Mock Modem ")
                # os.system("adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X shell pm uninstall -k --user 0 com.github.uiautomator")
                # os.system("python3 -m uiautomator2 init  --serial %s"%dut)
                # print(dut +" devices refind llow Mock Modem again")
                # d = u2.connect(dut)
                # time.sleep(5)
                os.system('adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X shell input keyevent 3') # Home鍵
                d.app_clear("com.android.settings")
                time.sleep(5)
                d.shell("am start -n com.android.settings/.Settings\$DevelopmentSettingsDashboardActivity") # set stay awake to true 

                # os.system("adb -s %s shell am start -n 'com.android.settings/.Settings\$DevelopmentSettingsDashboardActivity'"%serial) # set stay awake to true 

                p=1
        # return p
                # os.system("adb -s %s shell am start -n 'com.android.settings/.Settings\$DevelopmentSettingsDashboardActivity'"%serial) # set stay awake to true 

                # # os.system("adb -s %s shell am kill 'com.android.settings/.Settings\$DevelopmentSettingsDashboardActivity'"%serial) # set stay awake to true 
                # os.system("adb -s %s shell am start -n 'com.android.settings/.Settings\$DevelopmentSettingsDashboardActivity'"%serial) # set stay awake to true 
                # print("cannot find Allow Mock Modem and try find it again")
                # d(scrollable=True).scroll.to(text="Allow Mock Modem")
                # d.dump_hierarchy()
                # time.sleep(8)
                
                # if d(text="Allow Mock Modem").exists:
                #     print("find the Allow Mock Modem and enabled ")
                #     d(text="Allow Mock Modem").click()
                #     d.press('home')
                
        os.system("adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X shell pm uninstall -k --user 0 com.github.uiautomator")
                #     return 2
                # else:
                #     print("cannot find Allow Mock Modem 2nd")
                #     p=rerun_Allow_Mock_Modem(serial)
                #     return p
        return p


        
    except:
        print('exception happen canot find anything')
        return 1
        # os.system("adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X shell pm uninstall -k --user 0 com.github.uiautomator")
        # os.system("./Factory_Reset.sh -s %s"%serial)
        # time.sleep(100)
        # start_element(serial)
#----------------------------------
def reset_devie_status(serial):
    os.system("./Factory_Reset.sh -s %s"%serial)
    time.sleep(100)
    k=start_element(serial)
    return k
# def start_element(serial):
#     os.system("python3 -m uiautomator2 init  --serial %s"%serial)
#     d = u2.connect(serial)
#     d.dump_hierarchy()
#     d.healthcheck()
#     print(d.info)
#     #main function
#     try:
#         # d(resourceId="com.google.android.setupwizard:id/start").wait()
#         # d(resourceId="com.google.android.setupwizard:id/start").click()
#         print('start')
#         time.sleep(2)
#         d(text="Start").click()
#         time.sleep(1)
#         if d(text='Skip').exists:
#             d(text="Skip").click()
#         time.sleep(1)
#         d(text="Set up offline").click()
#         time.sleep(1)
#         d(resourceId="android:id/button1").click()
#         time.sleep(5)
#         if d(text='Next').exists:
#             d(text="Next").click()
#         time.sleep(1)
#         for _ in range(2):
#             d(text="More").click()
#         time.sleep(1)
#         d(text="Accept").click()
#         time.sleep(4)
#         if d(text='Set a PIN').exists:
#             time.sleep(2)
#             d(text='Skip').click()
#             time.sleep(2)
#             d(text='Skip anyway').click()
#             time.sleep(5)
#         else:
#             d(resourceId="android:id/title", text="Not now").click()
#             d(resourceId="android:id/button1").click()
#             time.sleep(30)
#         os.system('adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X shell settings put global stay_on_while_plugged_in 3')
#         time.sleep(1)
#         d.app_start("com.android.settings",".Settings$WifiSettings2Activity")
#         time.sleep(1)
#         d(text="B13F-2Q05-GMS").click()
#         time.sleep(1)
#         # d.send_keys("8888800000")
#         d.shell("input text 8888800000")
#         time.sleep(1)
#         # d(text="CONNECT").click()
#         d.xpath('//*[@resource-id="com.google.android.inputmethod.latin:id/key_pos_ime_action"]/android.widget.FrameLayout[1]/android.widget.ImageView[1]').click()
#         time.sleep(10)
#         os.system("adb -s %s shell am start -n 'com.android.settings/.Settings\$MyDeviceInfoActivity'"%serial) # set stay awake to true 
#         time.sleep(1)
#         d(scrollable=True).scroll.to(text="Build number")
#         for _ in range(10):
#             d(text="Build number").click()
#         time.sleep(3)
#         os.system("adb -s %s shell am start -n 'com.android.settings/.Settings\$DevelopmentSettingsDashboardActivity'"%serial) # set stay awake to true 
#         # d(scrollable=True).scroll.to(text="Stay awake")
#         # if d(text="Stay awake").exists:
#         #     d(text="Stay awake").click()
#         d(scrollable=True).scroll.to(text="Allow Mock Modem")
#         if d(text="Allow Mock Modem").exists:
#             d(text="Allow Mock Modem").click()
#         d.press('home')
#         os.system("adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X shell pm uninstall -k --user 0 com.github.uiautomator")
#         time.sleep(10)
#         d.press('home')
#         os.system("adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X shell pm uninstall -k --user 0 com.github.uiautomator")
#     except:
#         print('waiting start button')
#         #start_element(serial)

if __name__ == "__main__":
    process_list = []
    serial_list = get_devices_serials()
    #reboot to check roboot times
    # os.system('adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X reboot')
    # time.sleep(45)
    #check txt
    with open('record_disconnect.txt','r') as f:
        for line in f:
            line=line.strip('\n')
            if len(line)!=0:
                dis_devices.append(line)
        print('txt dis_devices:',dis_devices)

    # for i in series:
    #     serial = i
    #     d_count=0
    #     disconnect=yaqing.disconnect(serial,d_count)
    #     print("disconnect devices:",disconnect)
    #     if disconnect != 32512:
    #         dis_devices.append(disconnect)
    # print(dis_devices)

    if dis_devices != None:
        for i in dis_devices:
            for j in serial_list:
                if (i==j):
                    f=open('record_disconnect.txt','a')
                    f.write('\n')
                    f.write(i)
                    serial_list.remove(i)
                    break

    # for index in range( len(serial_list) ):
    #     #創建子進程執行start_element()的函數
    #     p = Process( target=start_element, args=( serial_list[index],  ) )
    #     p.start()
    #     process_list.append(p)
    # for p in process_list:
    #     p.join()
    for index in range( len(serial_list) ):
        p=start_element(serial_list[index])

        while True:
            print('p=',p)
            print('factroty reset :',count ,'times to compelepte devices setup')

            count=count+1
            if p==1:
                # ans=input("factroy reset y/n ?")
                # if ans=="y":
                print("facrtory reset handel exception problem ")
                p=reset_devie_status(serial_list[0])
                # else:
                #     print('refind chrome icon')
                #     p=start_element(serial_list[0])
            if p==0:
                # ans=input("exception happen need to re-processing again y/n ?")
                # if ans=="y":
                #     # p=reset_devie_status(serial_list[0])
                p=reset_devie_status(serial_list[0])
                # else:
                #     print("terminate processing")
                #     break
            if p is None:
                break 
            if p==2:
                print('p=',p)
                print('factroty reset :',count ,'times to compelepte devices setup')

                break 
        print("all task done!")
    

