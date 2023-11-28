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
    os.system ('gnome-terminal -- python3 multi_devices_setup_A13.sh %s' + serial)

if __name__ == "__main__":
    process_list = []
    serial_list = get_devices_serials()
    print(serial_list[0])
    print ("CBN check device info ")
    os.system ('python3 CBN.py --name ' + serial_list[0])
    print ("devices set up for cts testing ")
    os.system ('python3 multi_devices_setup_A13.py ' + serial_list[0])

    # time.sleep(15)
    
    # check =input('Please confirm all devices have completed multi_devices_setup_A13 [y/n] ...')
    # if check =='y':
    print ("set up chrome ")
    os.system ('python3 cts_device_setup_for_chrome_Jonathan.py ' + serial_list[0])
    # print( "push media ")
    # os.system ('python3 CAD_test.py --name ' + serial_list[0])


    # os.system(f'gnome-terminal -- google-chrome --remote-debugging-port=9222 --user-data-dir="{path}"')
    # for index in range( len(serial_list) ):
    #     #創建子進程執行start_element()的函數
    #     p = Process( target=start_element, args=( serial_list[index],  ) )
    #     p.start()
    #     process_list.append(p)
    # for p in process_list:
    #     p.join()
    print("all task done!")
    # os.system("python3 -m uiautomator2 init  --serial %s"%serial)
