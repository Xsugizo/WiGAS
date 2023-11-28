#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

######################################################################################################## 

# 

# 隡惩��:��𧢲㦤id(adb devices�遬蝷箇���𧢲㦤id)   

# e.g:python call.py 4650150b 

# 

# V1.0 

# 2018/03/02 

# yink.liu 

######################################################################################################## 

import re 
import stat
import sys 

import os 

import time 

import subprocess 

from subprocess import call 

import argparse 

UsrName = subprocess.check_output('whoami')
UsrName = UsrName.decode().strip()
print("usernanme",UsrName)
parser = argparse.ArgumentParser() 

output_build_number=[] 

parser.add_argument('--name', type=str, default="") 

args = parser.parse_args() 

i= args.name 
print(i)
#output_build_number.append(os.system('adb -s %s getprop ro.vendor.build.fingerprint',i)) 

print(os.system('adb -s '+ i +' shell getprop ro.vendor.build.fingerprint')) 

 
 

os.system('adb -s '+ i +' shell svc power stayon true') # set stay awake to true 

os.system('adb -s '+ i +' shell locksettings set-disabled true') # set lock screen to none 

os.system('adb -s '+ i +' shell settings put global verifier_verify_adb_installs 0') #set verify apps over USB to disable 

os.system('adb -s '+ i +' shell am start -n com.android.chrome/com.google.android.apps.chrome.Main') # open GMS chrome 

os.system('adb -s '+ i +' shell am start -n org.chromium.chrome/com.google.android.apps.chrome.Main') # open non GMS chrome 

file_path = "/home/"+UsrName+"/Desktop/IMAGE/workspace/Pipeline_Testing_Cts/android-cts-media-1.5/"

print("print:",file_path)

os.chdir(file_path)
c = 'chmod u+x '+file_path+'copy_media.sh '
cc ='chmod u+x '+file_path+'copy_images.sh '
p = file_path+'copy_media.sh -s '
pp =file_path+'copy_images.sh -s '

os.system(c) 
os.system(cc) 
# os.system(f'chmod u+x {file_path}copy_media.sh') 
# os.system(f'chmod u+x {file_path}copy_images.sh') 

# subprocess.call("python3 cts_chrome_setup.py ", shell=True) 
subprocess.call(p + i,shell=True) 
subprocess.call(pp + i,shell=True) 
# subprocess.call(f'{file_path}/copy_media.sh -s ' + i,shell=True) 
# subprocess.call(f'{file_path}/copy_images.sh -s ' + i,shell=True) 


# os.system("gnome-terminal -e './copy_media.sh -s '" + i) 

# os.system("gnome-terminal -e './copy_images.sh -s '" + i) 

#os.system('python copy_media.sh -s'+ i) 

#os.system('python copy_images.sh -s'+ i) 

 
 
 
 
 
 

# devices = [] 

# output_build_number=[] 

# #device_re = re.compile("device") 

 
 

# adb_devices= subprocess.check_output(["adb", "devices"]) 

# #print(adb_devices) 

# for i in adb_devices.split(b"\tdevice"): 

#     for ii in i.split(b"\n"): 

#         if  ii !="" and ii not in "List of devices attached" : 

#             devices.append(ii) 

# for i in devices: 

#      print(i) 

#      #output_build_number.append(os.system('adb -s %s getprop ro.vendor.build.fingerprint',i)) 

#      print(os.system('adb -s '+ i +' shell getprop ro.vendor.build.fingerprint')) 

 
 

#      os.system('adb -s '+ i +' shell svc power stayon true') # set stay awake to true 

#      os.system('adb -s '+ i +' shell locksettings set-disabled true') # set lock screen to none 

#      os.system('adb -s '+ i +' shell settings put global verifier_verify_adb_installs 0') #set verify apps over USB to disable 

#      os.system('adb -s '+ i +' shell am start -n com.android.chrome/com.google.android.apps.chrome.Main') # open GMS chrome 

#      os.system('adb -s '+ i +' shell am start -n org.chromium.chrome/com.google.android.apps.chrome.Main') # open non GMS chrome 

#      os.system('chmod u+x copy_media.sh') 

#      os.system('chmod u+x copy_images.sh') 

#      #subprocess.call("python3 cts_chrome_setup.py", shell=True) 

#      subprocess.call("./copy_media.sh -s " + i,shell=True) 

#      subprocess.call("./copy_images.sh -s " + i,shell=True) 

#     # os.system("gnome-terminal -e './copy_media.sh -s '" + i) 

#     # os.system("gnome-terminal -e './copy_images.sh -s '" + i) 

#      #os.system('python copy_media.sh -s'+ i) 

#      #os.system('python copy_images.sh -s'+ i) 

 