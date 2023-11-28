#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import uiautomator2 as u2
from multiprocessing import Process
import sys


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



def start_element(serial):
    os.system("python3 -m uiautomator2 init  --serial %s"%serial)
    d = u2.connect(serial)
    #main function
    try:
        d(resourceId="com.google.android.setupwizard:id/start").wait()
        d(resourceId="com.google.android.setupwizard:id/start").click()
        print('start')
        time.sleep(1)
        if d(text='Skip').exists:
            d(text="Skip").click()
        time.sleep(1)
        d(text="Set up offline").click()
        time.sleep(1)
        d(resourceId="android:id/button1").click()
        time.sleep(5)
        if d(text='Next').exists:
            d(text="Next").click()
        time.sleep(1)
        # while d(text='More').exists:
            # print('Finded !')
            # d(text="More").click()
        for _ in range(2):
            d(text="More").click()
        time.sleep(1)
        d(text="Accept").click()
        time.sleep(4)
        if d(text='Set screen lock').exists:
            time.sleep(2)
            d(text='Skip').click()
            time.sleep(2)
            d(text='Skip anyway').click()
            time.sleep(5)
        else:
            d(resourceId="android:id/title", text="Not now").click()
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
        d(text="CONNECT").click()
        time.sleep(10)
        d.press('home')
        os.system("adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X shell pm uninstall -k --user 0 com.github.uiautomator")
    except:
        print('waiting start button')
        start_element(serial)


if __name__ == "__main__":
    process_list = []
    serial_list = get_devices_serials()
    for index in range( len(serial_list) ):
        #創建子進程執行start_element()的函數
        p = Process( target=start_element, args=( serial_list[index],  ) )
        p.start()
        process_list.append(p)
    for p in process_list:
        p.join()
    print("all task done!")

