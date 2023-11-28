#!/usr/bin/env python3
import uiautomator2 as u2
import time
import os
d=u2.connect_usb()
print('device connected')
d(resourceId="com.google.android.setupwizard:id/start").click()
d(text="Skip").click()
time.sleep(1)
d(text="Set up offline").click()
d(resourceId="android:id/button1").click()
time.sleep(5)
d(text="Next").click()
time.sleep(1)
for _ in range(2):
    d(text="More").click()
time.sleep(1)
d(text="Accept").click()
d(resourceId="android:id/title", text="Not now").click()
d(resourceId="android:id/button1").click()
time.sleep(30)
d.app_start("com.android.settings",".Settings$WifiSettings2Activity")
d(text="B13F-2Q05-GMS").click()
d.send_keys("8888800000")
d(text="CONNECT").click()
time.sleep(10)
os.system("adb shell pm uninstall -k --user 0 com.github.uiautomator")
