#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import os
import yaqing
dis_devices=[]
# devices=['212555225E0089','212555225E0147','212555225E0182','213405225E0339']
# print("reboot to check roboot times")
# os.system('adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X reboot')
# time.sleep(45)
# print("devices:",devices)

# with open('record_disconnect.txt','r+') as a:
#     a.truncate(0)

def renewdevices(devices):
    with open('record_disconnect.txt','r') as f:
        for line in f:
            line=line.strip('\n')
            if len(line)!=0:
                dis_devices.append(line)
        print('disconnect devices(.txt):',dis_devices)


    for i in devices:
        serial = i
        print("device serial number:",serial)
        disconnect=yaqing.disconnect(serial)
        print("disconnect devices detect done !")
        print("disconnect device:",disconnect)
        if disconnect != '32512':
            dis_devices.append(disconnect)
    print(dis_devices)

    if dis_devices != None:
        for i in dis_devices:
            for j in devices:
                if (i==j):
                    with open('record_disconnect.txt','a')as f:
                        f.write('\n')
                        f.write(i)
                    devices.remove(i)
                    print("new devices:",devices)
                    break
    # check = input("check .txt (y/n) : ")
    return devices

