#!/usr/bin/env python
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
#device_re = re.compile("device")

adb_devices= subprocess.check_output(["adb", "devices"])
#print(adb_devices)
for i in adb_devices.split(b"\tdevice"):
    for ii in i.split(b"\n"):
        if  ii !="" and ii not in "List of devices attached" :
            devices.append(ii)
for i in devices:
    print("run multi_devices_setup_A13_setup")
# os.system ('gnome-terminal -- ./Factory_Reset.sh -s ' + i)
# time.sleep(100)
    os.system ('gnome-terminal -- python3 multi_devices_setup_A13_setup.py ' + i)
# os.system ('gnome-terminal -- python3 multi_devices_setup_A13_Run_setup.py ')

    # print ("devices set up for cts testing ")
    # os.system ('gnome-terminal -- python3 multi_devices_setup_A13.py ' + i)
    time.sleep(90)
    print("sleep 90 sec")
     #output_build_number.append(os.system('adb -s %s getprop ro.vendor.build.fingerprint',i))
    #  print(os.system('adb -s '+ i +' shell getprop ro.vendor.build.fingerprint'))

    #  os.system('adb -s '+ i +' shell svc power stayon true') # set stay awake to true
    #  os.system('adb -s '+ i +' shell locksettings set-disabled true') # set lock screen to none
    #  os.system('adb -s '+ i +' shell settings put global verifier_verify_adb_installs 0') #set verify apps over USB to disable
    #  os.system('adb -s '+ i +' shell am start -n com.android.chrome/com.google.android.apps.chrome.Main') # open GMS chrome
    #  os.system('adb -s '+ i +' shell am start -n org.chromium.chrome/com.google.android.apps.chrome.Main') # open non GMS chrome
    #  os.system('chmod u+x copy_media.sh')
    #  os.system('chmod u+x copy_images.sh')
    #  #subprocess.call("python3 cts_chrome_setup.py", shell=True)
    #  subprocess.call("./copy_media.sh -s " + i,shell=True)
    #  subprocess.call("./copy_images.sh -s " + i,shell=True)
    # os.system("gnome-terminal -e './copy_media.sh -s '" + i)
    # os.system("gnome-terminal -e './copy_images.sh -s '" + i)
     #os.system('python copy_media.sh -s'+ i)
     #os.system('python copy_images.sh -s'+ i)
