#! /usr/bin/env python3

import re
import sys
import os
import time
import subprocess
from subprocess import call
devices = []
check_devices=[]
check_image=[]
output_build_number=[]
#device_re = re.compile("device")

def check_product():
    adb_devices= subprocess.check_output(["adb", "devices"])
    #print(adb_devices)
    for i in adb_devices.split(b"\tdevice"):
        for ii in i.split(b"\n"):
            
            if  ii.decode('utf-8')  !=b"" and ii.decode('utf-8')  not in "List of devices attached" :
                devices.append(ii.decode('utf-8'))
    for i in devices:
        print(i)

    diff=0
    di_image=0
    p=0
    for iii in devices:
        product_name=subprocess.check_output(["adb", "-s", iii,"shell","getprop ro.product.device"])
        product_image=subprocess.check_output(["adb", "-s", iii,"shell","getprop ro.build.id"])
        product_name=product_name.decode('utf-8').replace("\n"," ")
        product_image=product_image.decode('utf-8').replace("\n"," ")
        print("product_name "+str(p+1)+"=",product_name)
        print("product_image "+str(p+1)+"=",product_image)
        if product_name not in check_devices and p>0:
            print("you have different product name is " + product_name)
            diff=1
        if product_image not in check_image and p>0:
            print("you have different product name is " + product_image)
            di_image=1
        check_devices.append(product_name)
        check_image.append(product_image)
        p=p+1
    
    print(str(diff)+"/"+str(di_image))
    if diff==1:
       print("diff_product_name")
       return "diff_product_name"
    if diff==0:
        print("same_product_name")
        return "same_product_name"
        
    
    # if di_image==1:
    #     print("diff_product_image")
    #     return "diff_product_image"
        
    # if di_image==0:
    #     print("same_product_image")
    #     return "same_product_image"
        
    
    print(check_devices)

# check_product()


