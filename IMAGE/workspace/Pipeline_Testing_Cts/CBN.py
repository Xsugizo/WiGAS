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
import argparse 

parser = argparse.ArgumentParser() 
devices = []
output_build_number=[]
odm_file_list=[]
build_number=[]
parser.add_argument('--name', type=str, default="") 

args = parser.parse_args() 

i= args.name 
#device_re = re.compile("device")
adb_devices= subprocess.check_output(["adb", "devices"])
print(adb_devices)
# for i in adb_devices.split(b"\tdevice"):
#     for ii in i.split(b"\n"):
#         if  ii !="" and ii not in "List of devices attached" :
#             devices.append(ii)
# print('Device')
# print('')

temp=(os.popen('adb -s'+ i +' shell getprop ro.product.vendor.name').read()).rstrip()
print(temp)
print('')
print('Build fingerprint')
print('')

temp=(os.popen('adb -s'+ i +' shell getprop ro.vendor.build.fingerprint').read()).rstrip()
print(temp)    
print('')
print('Build number')
print('')

temp=(os.popen('adb -s'+ i +' shell getprop ro.build.fingerprint').read()).rstrip()
print(temp) 
print('')
print('Build Security Patch')
print('')

temp=(os.popen('adb -s'+ i +' shell getprop ro.build.version.security_patch').read()).rstrip()
print(temp) 
print('')
print('Vendor Security Patch')
print('')

temp=(os.popen('adb -s'+ i +' shell getprop ro.vendor.build.security_patch').read()).rstrip()
print(temp) 
