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
    

count=0
def start_element(serial):
    global count
    
    os.system("adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X shell pm uninstall -k --user 0 com.github.uiautomator")
    print("multi_devices_setup_A13")
    os.system("python3 -m uiautomator2 init  --serial %s"%serial)
    print(serial +" devices setup begin")
    d = u2.connect(serial)
    print(d.info)

    try:
        d.shell("am start -n com.android.settings/.Settings\$DevelopmentSettingsDashboardActivity") # set stay awake to true 
        
    except:
        print('exception happen canot find anything')





if __name__ == "__main__":
    process_list = []
    serial_list = get_devices_serials()

    start_element(serial_list[0])


    print("all task done!")

