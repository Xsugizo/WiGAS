#! /usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################################################
#
# 传入:手机id(adb devices显示的手机id)  
# e.g:python call.py 4650150b
#
# V1.0
# 2018/03/02
# yink.liu
########################################################################################################
import re
import sys
import os
import time
import subprocess
from subprocess import call
devices = []
output_build_number=[]
d_count=None
dis_devices=[]
#device_re = re.compile("device")

# adb_devices= subprocess.check_output(["adb", "devices"])
#print(adb_devices)
# for i in adb_devices.split(b"\tdevice"):
#     for ii in i.split(b"\n"):
#         if  ii !="" and ii not in "List of devices attached" :
#             devices.append(ii)
fd = os.popen("adb devices")
devices_list_src = fd.readlines()#返回list
fd.close()
for device in devices_list_src:
    if "device\n" in device:
        device = device.replace("\tdevice\n","")
        devices.append(device)

#reboot to check roboot times
# os.system('adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X reboot')
# time.sleep(45)

with open('record_disconnect.txt','r') as f:
    for line in f:
        line=line.strip('\n')
        if len(line)!=0:
            dis_devices.append(line)
    print('txt dis_devices:',dis_devices)

# for i in devices:
#     serial = i
#     d_count=0
#     disconnect=yaqing.disconnect(serial,d_count)
#     print("disconnect device:",disconnect)
#     if disconnect != 32512:
#         dis_devices.append(disconnect)
# print(dis_devices)

if dis_devices != None:
    for i in dis_devices:
        for j in devices:
            if (i==j):
                f=open('record_disconnect.txt','a')
                f.write('\n')
                f.write(i)
                devices.remove(i)
                break
for i in devices:
     print(i)
     #output_build_number.append(os.system('adb -s %s getprop ro.vendor.build.fingerprint',i))
     print(os.system('adb -s '+ i +' shell getprop ro.vendor.build.fingerprint'))
     os.system('adb -s '+ i +' shell svc power stayon true') # set stay awake to true
     os.system('adb -s '+ i +' shell locksettings set-disabled true') # set lock screen to none
     os.system('adb -s '+ i +' shell settings put global verifier_verify_adb_installs 0') #set verify apps over USB to disable
    #  os.system('adb -s '+ i +' shell am start -n com.android.chrome/com.google.android.apps.chrome.Main') # open GMS chrome
    #  os.system('adb -s '+ i +' shell am start -n org.chromium.chrome/com.google.android.apps.chrome.Main') # open non GMS chrome
     
     file_path = "/home/logo113/Desktop/IMAGE/workspace/Pipeline_Testing/android-cts-media-1.5/"

     os.chdir(file_path)

     os.system('chmod u+x copy_media.sh')
     os.system('chmod u+x copy_images.sh')
     #subprocess.call("python3 cts_chrome_setup.py", shell=True)
     subprocess.call("/home/logo113/Desktop/IMAGE/workspace/Pipeline_Testing/android-cts-media-1.5/copy_media.sh -s " + i,shell=True)
     subprocess.call("/home/logo113/Desktop/IMAGE/workspace/Pipeline_Testing/android-cts-media-1.5/copy_images.sh -s " + i,shell=True)
    # os.system("gnome-terminal -e './copy_media.sh -s '" + i)
    # os.system("gnome-terminal -e './copy_images.sh -s '" + i)
     #os.system('python copy_media.sh -s'+ i)
     #os.system('python copy_images.sh -s'+ i)
