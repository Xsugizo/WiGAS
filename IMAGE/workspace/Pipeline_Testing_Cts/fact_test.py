import os
import time
def test():
    os.system('adb devices')
    os.system('adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X reboot bootloader')
    time.sleep(20)
    os.system('fastboot devices')
    os.system('fastboot devices |  cut -sf 1 | xargs -IX fastboot -s X oem sku')
    os.system('fastboot devices |  cut -sf 1 | xargs -IX fastboot -s X reboot')
    #time.sleep(30)
#test()
#make a string to add behind setup.py
def device_str():
    try:
        de_str =""
        device = os.popen('adb devices').read()
        device = device.split()
        for i in range(len(device)):
            if(i>=4 and i%2 ==0):
                de_str += device[i]+" "
        return de_str
    except:
        print("error to make devices string")
str_de = device_str()
print(str_de)