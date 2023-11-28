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
    # os.system ('gnome-terminal -- python3 multi_devices_setup_A13.sh %s' + serial)
    os.system("python3 -m uiautomator2 init  --serial %s"%serial)
    print(serial +" devices setup begin")
    d = u2.connect(serial)
    time.sleep(4)
    d.press("back")
    os.system('adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X shell input keyevent 3') # Home鍵
    d.app_clear("com.android.settings")
    time.sleep(4)
    # d.app_start("com.android.settings",".Settings$WifiSettings2Activity")
    # time.sleep(7)
    # os.system("adb -s %s shell am start -n 'com.android.settings/.Settings\$MyDeviceInfoActivity'"%serial) 
    # d.shell("am start -n com.android.settings/.Settings\$MyDeviceInfoActivity") 
    d.shell("am start -n com.android.settings/.Settings\$DevelopmentSettingsDashboardActivity") # set stay awake to true 

    # d.app_start("com.android.settings",".Settings$MyDeviceInfoActivity") # d.app
    time.sleep(7)

    os.system("python3 -m uiautomator2 --serial %s screenshot %s_screenshot.jpg  "%(serial,serial) )
    print(d.info)


if __name__ == "__main__":
    process_list = []
    serial_list = get_devices_serials()
    
    # print ("CBN check device info ")
    # start_element(serial_list[0])
    # os.system ('gnome-terminal -- python3 multi_devices_setup_A13_setup.py ' + serial_list[0])
    # os.system ('python3 multi_devices_setup_A13_setup.py ' + serial_list[0])

    # os.system(f'gnome-terminal -- google-chrome --remote-debugging-port=9222 --user-data-dir="{path}"')
    for index in range( len(serial_list) ):
        print('device=',serial_list[index])
    #     #創建子進程執行start_element()的函數
        os.system ('python3 multi_devices_setup_A13_setup.py ' + serial_list[index])
    #     p = Process( target=start_element, args=( serial_list[index],  ) )
    #     p.start()
    #     process_list.append(p)
    # for p in process_list:
    #     p.join()
    print("all task done!")
    # os.system("python3 -m uiautomator2 init  --serial %s"%serial)
