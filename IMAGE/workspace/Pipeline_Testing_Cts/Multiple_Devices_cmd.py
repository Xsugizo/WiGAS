#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
import os
import time
import subprocess
from subprocess import call

import globalvar
globalvar.initialize()
dirpath = globalvar.path
def d_number():
    devices = []
    
    cmd = ""
    #device_re = re.compile("device")

    adb_devices= subprocess.check_output(["adb", "devices"])
    #print(adb_devices)
    for i in adb_devices.split(b"\tdevice"):
        for ii in i.split(b"\n"):
            if  ii !="" and ii not in "List of devices attached" :
                devices.append(ii)
    coun=str(len(devices)) 
    ii=0
    for i in devices:
        if ii==0:
            cmd= "--shard-count "+coun+ " -s "+i
            ii=ii+1
        else:
            cmd=cmd+" -s "+i
    return devices,cmd

devices,cmd = d_number()

def test(cmd):

    with open('/home/logo113/Desktop/IMAGE/workspace/Pipeline_Testing/runcts.sh','w')as f:
        
        f.write("#!/bin/bash"+'\n')
        f.write(f"cd {dirpath}/android-cts/tools"+'\n')
        f.write("./cts-tradefed run cts -m CtsCameraTestCases "+cmd+'\n')
        f.write("./cts-tradefed l r")
    f.close()

test(cmd)
