#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import uiautomator2 as u2
dis_devices=[]

def disconnect(serial):
    try:
        #connect to uiautomator
        os.system("python3 -m uiautomator2 init  --serial %s"%serial)
        d = u2.connect(serial)
        #Start to detect blue screen
        print('Start to detect blue screen')
        time.sleep(1)
        if d(text='START').exists:
            print("No reboot times serial number:",serial)
            return serial
        else:
            return '0'
    except:
        return serial




