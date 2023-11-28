#! /usr/bin/env python3

import time
import os
from ctscheck import test
from pyautogui import hotkey,click,typewrite,press
from joblib import Parallel, delayed
import subprocess
import shutil
import globalvar
globalvar.initialize()
dirpath = globalvar.path

# check = False
directory = dirpath+'/android-cts/results'
latest=sorted([os.path.join(directory,d) for d in os.listdir(directory)],key=os.path.getmtime)
for i in latest:
    if i == dirpath+'/android-cts/results/latest':
        print ("remove")
        latest.remove(dirpath+'/android-cts/results/latest') 
    
    print(i)
# while check == False: 
#         #check = os.path.exists(latest[-1]+"/test_result_failures_suite.html")
#         check = os.path.exists(latest[-1])
#         print(check)
#         time.sleep(10)