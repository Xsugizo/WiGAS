#! /usr/bin/env python
import time
import os
import csv
import re
import sys
import subprocess
import array
from pyautogui import hotkey,click,typewrite,press
from sendmail import send_mail
import globalvar
globalvar.initialize()
dirpath = globalvar.path


import concurrent.futures
from uiautomator2 import Device
MAX_RETRIES = 3

def get_connected_devices():
    # Run adb command to get connected device serial numbers
    output = subprocess.check_output(['adb', 'devices']).decode('utf-8')
    lines = output.strip().split('\n')[1:]
    devices = [line.split('\t')[0] for line in lines if '\tdevice' in line]
    print(devices)
    return devices


def run_wizard_setup_on_device(device_serial):
    retries = 0
#------------------------------------------------------------------------------------------------------

    print("CBN")
    temp=(os.popen('adb -s'+ device_serial +' shell getprop ro.product.vendor.name').read()).rstrip()
    print(temp)
    print('')
    print('Build fingerprint')
    print('')

    temp=(os.popen('adb -s'+ device_serial +' shell getprop ro.vendor.build.fingerprint').read()).rstrip()
    print(temp)    
    print('')
    print('Build number')
    print('')

    temp=(os.popen('adb -s'+ device_serial +' shell getprop ro.build.fingerprint').read()).rstrip()
    print(temp) 
    print('')
    print('Build Security Patch')
    print('')

    temp=(os.popen('adb -s'+ device_serial +' shell getprop ro.build.version.security_patch').read()).rstrip()
    print(temp) 
    print('')
    print('Vendor Security Patch')
    print('')

    temp=(os.popen('adb -s'+ device_serial +' shell getprop ro.vendor.build.security_patch').read()).rstrip()
    print(temp) 
#-----------------------------------------------------------------------------------------------------------------#
    
    while retries < MAX_RETRIES:
        try :
            print("device_serial="+str(device_serial))
            d = Device(device_serial)            
            d.HTTP_TIMEOUT = 90 # 默认值60s, http默认请求超时时间
            d.screen_on()
            # os.system('adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X shell input keyevent 3') # Home鍵

            # d(resourceId="com.google.android.setupwizard:id/start").wait()
            # d(resourceId="com.google.android.setupwizard:id/start").click()
            time.sleep(5)
            # for _ in range(10):
            #     d(text="Start").click()
            # time.sleep(1)
            if d(text='Start').exists:
                print('find Start')
                d(text="Start").click()
            else:
                print('ignore Start')
            # else:
            #     os.system("./Factory_Reset.sh -s %s"%serial)
            #     time.sleep(100)
            #     start_element(serial)
            
            # # d(text='Start', className='android.widget.Button').click()
            # time.sleep(1)
            # if d(text="Start").exists:
            #     d(text="Start").click()
            # time.sleep(1)
            time.sleep(2)
            if d(text='Skip').exists:
                print('push Skip')
                d(text="Skip").click()
            else:
                print('ignore skip')
            time.sleep(3)
            if d(text='Set up offline').exists:
                print('Set up offline')
                d(text="Set up offline").click()
            else:
                print('ignore set up offline')
            time.sleep(2)
            if d(resourceId="android:id/button1").exists:
                print('push button')
                d(resourceId="android:id/button1").click()
            else:
                print('ignore push button')
            time.sleep(5)
            if d(text='Next').exists:
                print('push next')
                d(text="Next").click()
            else:
                print('ignore push next')
            time.sleep(2)
            # while d(text='More').exists:
                # print('Finded !')
                # d(text="More").click()
            for _ in range(2):
                if d(text="More").exists:
                    print('push More')
                    d(text="More").click()
                else:
                    print('ignore push More')
                    break
            time.sleep(1)
            if d(text="Accept").exists:
                print('push Accept')
                d(text="Accept").click()
            else:
                print('ignore Accepet')
            time.sleep(4)
            if d(text='Set a PIN').exists:
                time.sleep(2)
                if d(text='Skip').exists:
                    print('push skip')
                    d(text='Skip').click()
                else:
                    print('ignore Skip')
                time.sleep(2)
                if d(text='Skip anyway').exists:
                    print('push skip anyway')
                    d(text='Skip anyway').click()
                else:
                    print('ignore Skip anyway')
                time.sleep(5)
            else:
                if d(resourceId="android:id/title", text="Not now").exists:
                    print('push not now')
                    d(resourceId="android:id/title", text="Not now").click()
                else:
                    print('ignore push not now')
                if d(resourceId="android:id/button1").exists:
                    print('push button')
                    d(resourceId="android:id/button1").click()
                else:
                    print('ignore push button')
                time.sleep(30)
            os.system('adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X shell settings put global stay_on_while_plugged_in 3')
            time.sleep(2)
            # time.sleep(2)
            print("wifi-setting")
            # print(serial)
            # command = ["adb", "-s", serial, "shell", "dumpsys", "connectivity", "|", "grep", '"mNetworkActive"']
            command = ["adb", "-s", device_serial, "shell", "dumpsys", "wifi", "|", "grep", '"handleConnectionStateChanged"']

            result = subprocess.run(command, capture_output=True, text=True)
            # print(result.stdout)
            wfi=result.stdout
            wfi = wfi.split("\n")
            # print(wfi[-2])
            if "state=connected" in wfi[-2]:     
                print("Wi-Fi is Connected")
            else:
                d.app_start("com.android.settings",".Settings$WifiSettings2Activity")
                time.sleep(5)
                d(scrollable=True).scroll.to(text="B13F-2Q05-GMS")
                if d(text="B13F-2Q05-GMS").exists:
                    d(text="B13F-2Q05-GMS").click()
                    time.sleep(1)
                    # d.send_keys("8888800000")
                    print("input password")
                    d.shell("input text 8888800000")
                    time.sleep(1)
                    print("enter")
                    d.press("enter")
                    # d.xpath('//*[@resource-id="com.google.android.inputmethod.latin:id/key_pos_ime_action"]/android.widget.FrameLayout[1]/android.widget.ImageView[1]').click()
                    time.sleep(5)
                    d.app_clear("com.android.settings")
                else:
                    print('skip wifi-setting')
            break
        except Exception as e:
            print(f"Connection error with device {device_serial}: {e}")
            if retries < MAX_RETRIES - 1:
                print(f"Attempting to reconnect to device {device_serial}...")
                retries += 1
                time.sleep(5)  # Wait for a few seconds before retrying
            else:
                print(f"Max retries reached. Unable to reconnect to device {device_serial}. Test aborted.")

    # d(text="CONNECT").click()

    print(device_serial)
    print("Development Settings Enabled")
    os.system("adb -s %s shell settings put global development_settings_enabled 1"%device_serial) # set stay awake to true 
    time.sleep(10)
    print("get in System ")
    d.shell("am start -n com.android.settings/.Settings\$SystemDashboardActivity") # set stay awake to true 
    time.sleep(3)

    d.shell("am start -n com.android.settings/.Settings\$DevelopmentSettingsDashboardActivity") # set stay awake to true 
    time.sleep(5)
    

    print("Enable Allow Mock Modem ")
    d.shell("am start -n com.android.settings/.Settings\$DevelopmentSettingsDashboardActivity") # go to Development seeting page

    while True:
            d(scrollable=True).scroll.to(text="Allow Mock Modem")
            time.sleep(8)

            if d(text="Allow Mock Modem").exists:
                print("find the Allow Mock Modem and enabled ")
                d(text="Allow Mock Modem").click()
                d.press('home')
                break
                
                
    os.system("adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X shell pm uninstall -k --user 0 com.github.uiautomator")              
    #----------------------------------------------------------------------------------------------------------------------------#
    print ("push Chrome")
    os.system('adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X shell settings put global stay_on_while_plugged_in 3')
    time.sleep(1)
    if d(resourceId="com.android.chrome:id/fre_logo").exists:
        print('in chrome setting page')
    elif d(resourceId="com.android.chrome:id/image").exists:
        print('in chrome setting page')
    else:
        print ("screen on")
        d.screen_on()
        time.sleep(1)
        print (" home key")
        os.system('adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X shell input keyevent 3') # Home鍵
        
        time.sleep(2)
        print ("push Chrome")
        # d(text='Chrome').wait()
        if d(text='Chrome').exists:
            print ("push Chrome icon")
            d(text='Chrome').click()
            print("waiting for chrome ready")
            time.sleep(20)
        else:
            print ("adb cmd enable Chrome")
            os.system('adb -s %s shell am start -n com.android.chrome/com.google.android.apps.chrome.Main'%device_serial) # open GMS chrome 
            print("waiting for chrome ready")
            time.sleep(20)
    # time.sleep(20)
    
    if d(resourceId="com.android.chrome:id/signin_fre_dismiss_button").exists:
        # d(resourceId="com.android.chrome:id/terms_accept").wait(timeout=8.0)
        d(resourceId="com.android.chrome:id/signin_fre_dismiss_button").click()

    elif d(resourceId="com.android.chrome:id/signin_fre_continue_button").exists: #push Add account to device
        # d(resourceId="com.android.chrome:id/fre_bottom_group").wait(timeout=8.0)
        d(resourceId="com.android.chrome:id/signin_fre_continue_button").click()
            
    elif d(resourceId="com.android.chrome:id/fre_bottom_group").exists:
        # d(resourceId="com.android.chrome:id/fre_bottom_group").wait(timeout=8.0)
        d(resourceId="com.android.chrome:id/fre_bottom_group").click()

    else:
        # d.dump_hierarchy()
        print('Cannot find accept or Add account to device button ')
        # return 1
    # global count
    # count=count+1
    # print('count:',count)
    # if count>=1:
    #     ans = input('do you wnat to factory reset  y or n')
    #     print (ans)
    #     if ans == "y":
    #         print (ans)

            # reset_devie_status(serial)
    time.sleep(3)
    if d(resourceId="com.android.chrome:id/negative_button").exists:
        print("push negative_button")
        d(resourceId="com.android.chrome:id/negative_button").click()
        time.sleep(3)
        #d.press('home')
        os.system('adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X shell input keyevent 3') #home鍵
        time.sleep(3)
        os.system("adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X shell pm uninstall -k --user 0 com.github.uiautomator")



def push_chrome_on_device(device_serial):
    global count
    d = Device(device_serial)
    # d = Device.connect(device_serial)
    d.HTTP_TIMEOUT = 90 # 默认值60s, http默认请求超时时间

    # d.dump_hierarchy()
    # d.healthcheck()
    #main function

    os.system('adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X shell settings put global stay_on_while_plugged_in 3')
    time.sleep(1)
    if d(resourceId="com.android.chrome:id/fre_logo").exists:
        print('in chrome setting page')
    elif d(resourceId="com.android.chrome:id/image").exists:
        print('in chrome setting page')
    else:
        print ("screen on")
        d.screen_on()
        time.sleep(1)
        print (" home key")
        os.system('adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X shell input keyevent 3') # Home鍵
        
        time.sleep(2)
        print ("push Chrome")
        time.sleep(10)
        # d(text='Chrome').wait()
        if d(text='Chrome').exists:
            d(text='Chrome').click()
            time.sleep(10)
        else:
            os.system('adb -s %s shell am start -n com.android.chrome/com.google.android.apps.chrome.Main'%device_serial) # open GMS chrome 
    time.sleep(10)
    

    d.dump_hierarchy()
    d.dump_hierarchy()
    if d(resourceId="com.android.chrome:id/signin_fre_dismiss_button").exists:
        # d(resourceId="com.android.chrome:id/terms_accept").wait(timeout=8.0)
        d(resourceId="com.android.chrome:id/signin_fre_dismiss_button").click()

    elif d(resourceId="com.android.chrome:id/signin_fre_continue_button").exists: #push Add account to device
        # d(resourceId="com.android.chrome:id/fre_bottom_group").wait(timeout=8.0)
        d(resourceId="com.android.chrome:id/signin_fre_continue_button").click()
            
    elif d(resourceId="com.android.chrome:id/fre_bottom_group").exists:
        # d(resourceId="com.android.chrome:id/fre_bottom_group").wait(timeout=8.0)
        d(resourceId="com.android.chrome:id/fre_bottom_group").click()

    else:
        d.dump_hierarchy()
        print('Cannot find accept or Add account to device button ')
        return 1
        # global count
        # count=count+1
        # print('count:',count)
        # if count>=1:
        #     ans = input('do you wnat to factory reset  y or n')
        #     print (ans)
        #     if ans == "y":
        #         print (ans)

                # reset_devie_status(serial)

    time.sleep(3)
    if d(resourceId="com.android.chrome:id/negative_button").exists:
        print("push negative_button")
        d(resourceId="com.android.chrome:id/negative_button").click()
        time.sleep(3)
        #d.press('home')
        os.system('adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X shell input keyevent 3') #home鍵
        time.sleep(3)
        os.system("adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X shell pm uninstall -k --user 0 com.github.uiautomator")


if __name__ == '__main__':
    devices = get_connected_devices()

    # Create a ProcessPoolExecutor with the number of devices
    with concurrent.futures.ProcessPoolExecutor(len(devices)) as executor:
        # Submit the run_test_on_device function for each device
        future_to_device = {executor.submit(run_wizard_setup_on_device, device_serial): device_serial for device_serial in devices}

        # Wait for all tasks to complete
        for future in concurrent.futures.as_completed(future_to_device):
            device_serial = future_to_device[future]
            try:
                # Get the result from the completed future (if any)
                result = future.result()
                print(f"Test on device {device_serial} wizard setup completed successfully.")
            except Exception as e:
                print(f"Test on device {device_serial} wizard setup  raised an exception: {e}")
                



