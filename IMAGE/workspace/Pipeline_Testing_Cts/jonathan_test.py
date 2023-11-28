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
# command = ["adb", "-s", "212555225E0147", "shell", "dumpsys", "connectivity", "|", "grep", '"mNetworkActive"']
# command = ["gnome-terminal", "--","bash","-c","./install_Athena_1vN.sh", "212895225E0056", "106", "E0CD6EF0",">","A13.txt"]
# command_list = [cts_command, "run", "cts", "--shard-count", shard_count]
# def sh(command):
#     p = subprocess.Popen(command, shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#     print p.stdout.read()
# result = subprocess.Popen(command, capture_output=True, text=True)
# print(result.stdout)
# wfi=result.stdout
# # wfi.decode('UTF-8')
# wfi = wfi.split(" ")
# print("wfi"+wfi[2])
# if wfi[2] == "mNetworkActive=true\n" :
#     print("wifi connected")
# else:
#     # print(wfi)
#     print("wifi disconnected")
# stdout, stderr = p.communicate()
# print (stdout,stderr)

# result = subprocess.run(["dir"],shell=True,capture_output=True,text=True)
# print(result.stdout)
os.system("gnome-terminal -- bash -c './install_Athena_1vN.sh 212895225E0056 106 E0CD6EF0 > A13.txt'")



 