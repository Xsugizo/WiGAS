#! /usr/bin/env python3

from re import X
import time
import os
from ctscheckY import test
from pyautogui import hotkey,click,typewrite,press
# from joblib import Parallel, delayed
import subprocess
import shutil
import yaqing
import yaqingtest
import globalvar
globalvar.initialize()
dirpath = globalvar.path

dis_devices=[]
devices = []
d_count=None
UsrName = subprocess.check_output('whoami')
UsrName = UsrName.decode().strip()
# get run cts command
def cts_command():
    adb_devices= subprocess.check_output(["adb", "devices"])
    for i in adb_devices.split(b"\tdevice"):
        for ii in i.split(b"\n"):
            if  ii != b"" and ii not in b"List of devices attached" :
                x = ii.decode("utf-8")
                devices.append(x)
                # devices= yaqingtest.renewdevices(devices)
    coun=str(len(devices)) 
    ii=0
    # case = "--abi arm64-v8a -m CtsCameraTestCases"
    case = ""
    for i in devices:
        if ii==0:
            cmd= "run cts "+case+" --shard-count "+coun+ " -s "+ str(i)
            ii=ii+1
        else:
            cmd=cmd+" -s "+ str(i)
    return cmd
cts = cts_command()

# get retry command
def retry_command():
    with open(f'/home/{UsrName}/Desktop/IMAGE/workspace/Pipeline_Testing_Cts/retry1.sh') as file:
        r1 = file.read().replace('\n', '')
    file.close()
    return r1

# Auto GUI to enter tradefed mode and run cts
def first(cts):
    hotkey('ctrl','alt','t')
    time.sleep(1)
    hotkey('alt','F10')
    time.sleep(3)
    click(button='left')
    time.sleep(2)
    # typewrite('cd /home/logo113/Desktop/IMAGE/workspace/Pipeline_Testing/11_r10/android-cts-11_r10-linux_x86-arm/android-cts/tools')
    typewrite(f'cd {dirpath}/android-cts/tools')
    press('enter')
    time.sleep(3)
    typewrite('./cts-tradefed')
    press('enter')
    time.sleep(1)
    # typewrite('run cts -m CtsPermission2TestCases -t android.permission2.cts.NoReceiveSmsPermissionTest#testAppSpecificSmsToken')
    # typewrite('run cts --abi arm64-v8a -m CtsCameraTestCases --shard-count 2 -s 212555225E0089 -s 212555225E0147')
    typewrite(cts)
    press('enter')
    time.sleep(10)




def clean():
    directory = f"{dirpath}/android-cts/results"
    # directory = "/home/logo113/Desktop/IMAGE/workspace/Pipeline_Testing/11_r10/android-cts-11_r10-linux_x86-arm/android-cts/results"
    folder=sorted([os.path.join(directory,d) for d in os.listdir(directory)],key=os.path.getctime)
    for i in folder:
        if i == f"{dirpath}/android-cts/results/latest":
            folder.remove(f"{dirpath}/android-cts/results/latest")
        elif i == f"{dirpath}/android-cts/results/temp":
            folder.remove(f"{dirpath}/android-cts/results/temp")
        # if i == "/home/logo113/Desktop/IMAGE/workspace/Pipeline_Testing/11_r10/android-cts-11_r10-linux_x86-arm/android-cts/results/latest":
        #     folder.remove("/home/logo113/Desktop/IMAGE/workspace/Pipeline_Testing/11_r10/android-cts-11_r10-linux_x86-arm/android-cts/results/latest")
        # elif i == "/home/logo113/Desktop/IMAGE/workspace/Pipeline_Testing/11_r10/android-cts-11_r10-linux_x86-arm/android-cts/results/temp":
        #     folder.remove("/home/logo113/Desktop/IMAGE/workspace/Pipeline_Testing/11_r10/android-cts-11_r10-linux_x86-arm/android-cts/results/temp")
    target = f"{dirpath}/android-cts/results/temp"
    # target = "/home/logo113/Desktop/IMAGE/workspace/Pipeline_Testing/11_r10/android-cts-11_r10-linux_x86-arm/android-cts/results/temp"
    for i in folder:    
        if i != folder[-1]:
            shutil.move(i, target)   

# retry command after finishing CTS0
def retry_time(r1):
    typewrite(r1)
    press('enter')
    time.sleep(10)    

#reboot command and retry
def reboot_time(r1):
    os.system('adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X reboot')
    time.sleep(60)
    typewrite(r1)
    press('enter')
    time.sleep(10)

#set up after factory reset
def factory_reset_time_setup(id):
    time.sleep(60)
    os.system('python3 multi_devices_setup3.py '+str(id))
    os.system('python CAD_test.py --name '+str(id))
    os.system('python3 cts_device_setup_for_chrome.py '+str(id))

#retry command after factory reset
def factory_reset(r1):
    typewrite(r1)
    press('enter')
    time.sleep(10)

def checkfolder():
    check = False
    directory = f'{dirpath}/android-cts/results'
    # directory = '/home/logo113/Desktop/IMAGE/workspace/Pipeline_Testing/11_r10/android-cts-11_r10-linux_x86-arm/android-cts/results'
    latest=sorted([os.path.join(directory,d) for d in os.listdir(directory)],key=os.path.getctime)
    for i in latest:
        print(i)
        if i == f'{dirpath}/android-cts/results/latest':
            latest.remove(f'{dirpath}/android-cts/results/latest') 
        # if i == '/home/logo113/Desktop/IMAGE/workspace/Pipeline_Testing/11_r10/android-cts-11_r10-linux_x86-arm/android-cts/results/latest':
        #     latest.remove('/home/logo113/Desktop/IMAGE/workspace/Pipeline_Testing/11_r10/android-cts-11_r10-linux_x86-arm/android-cts/results/latest') 
    print(latest[-1])
    latestfolder=latest[-1]

#Automatically exit after finishing CTS 
def exit():
    # catch latest test result report
    check = False
    latestfolder=""
    checkfolder = False
    directory = dirpath+'/android-cts/results'
    # directory = '/media/logo007/1TBHD/IMAGE/workspace/Pipeline_Testing/11_r10/android-cts-11_r10-linux_x86-arm/android-cts/results'
    latest=sorted([os.path.join(directory,d) for d in os.listdir(directory)],key=os.path.getctime)
    for i in latest:
        if i == dirpath+'/android-cts/results/latest':
            latest.remove(dirpath+'/android-cts/results/latest') 
        #   if i == '/media/logo007/1TBHD/IMAGE/workspace/Pipeline_Testing/11_r10/android-cts-11_r10-linux_x86-arm/android-cts/results/latest':
        #     latest.remove('/media/logo007/1TBHD/IMAGE/workspace/Pipeline_Testing/11_r10/android-cts-11_r10-linux_x86-arm/android-cts/results/latest')  
    latestfolder=latest[-1] 
    # print("latestfolder="+latest[-1])  
    while checkfolder == False:
        latest=sorted([os.path.join(directory,d) for d in os.listdir(directory)],key=os.path.getctime)
        for i in latest:
            if i == dirpath+'/android-cts/results/latest':
                latest.remove(dirpath+'/android-cts/results/latest')
            # if i == '/media/logo007/1TBHD/IMAGE/workspace/Pipeline_Testing/11_r10/android-cts-11_r10-linux_x86-arm/android-cts/results/latest':
            #     latest.remove('/media/logo007/1TBHD/IMAGE/workspace/Pipeline_Testing/11_r10/android-cts-11_r10-linux_x86-arm/android-cts/results/latest')
        if(latest[-1]!=latestfolder):
            checkfolder=True
        print("new latestfolder="+latest[-1])
        print("latestfolder="+latestfolder) 

    while check == False: 
        check = os.path.exists(latest[-1]+"/test_result_failures_suite.html")
        print(check)
        print(latest[-1])
        time.sleep(10)


        

runfre = []
with open(f'/home/{UsrName}/Desktop/IMAGE/workspace/Pipeline_Testing_Cts/runfre.txt') as file:
    for line in file.readlines():
        runfre.append(int(line))
file.close()
retry_num=runfre[0]
reboot_num=runfre[1]
reset_num=runfre[2]

#set factory reset command
devices = []
reset_command1 = ''
reset_command = ''
adb_devices= subprocess.check_output(["adb", "devices"])
for i in adb_devices.split(b"\tdevice"):
    for ii in i.split(b"\n"):
        if  ii != b"" and ii not in b"List of devices attached" :
            x = ii.decode("utf-8")
            devices.append(x)
            with open('record_disconnect.txt','r') as f:
                for line in f:
                    line=line.strip('\n')
                    if len(line)!=0:
                        dis_devices.append(line)
                print('disconnect devices(.txt):',dis_devices)

            if dis_devices != None:
                for i in dis_devices:
                    for j in devices:
                        if (i==j):
                            with open('record_disconnect.txt','a')as f:
                                f.write('\n')
                                f.write(i)
                            devices.remove(i)
                            print("new devices:",devices)

            #
            reset_command1 = reset_command1 + "./Factory_Reset.sh -s "
            reset_command1 = reset_command1 + str(x) + " | "
size = len(reset_command1)
reset_command = reset_command1[:size - 2]
print(reset_command)          

#retry or not: yes=1, no=0
retry = 1
count = 0
r1 = ''

while (retry==1):
    print(count)
    os.chdir(f'/home/{UsrName}/Desktop/IMAGE/workspace/Pipeline_Testing_Cts') #ensure the path is correct
    if (count<retry_num+reboot_num+1): #retry+reboot time
        if (count == 0): #run cts first time
            first(cts)
            exit()
            clean() #clean past directory
            time.sleep(30)
            retry = test()
            r1 = retry_command()
        elif (count < reboot_num+1): #retry before reboot
            retry_time(r1)
            exit()
            time.sleep(30)
            retry = test()
            r1 = retry_command()
        else: #reboot and retry
            reboot_time(r1)
            exit()
            time.sleep(30)
            retry = test()
            r1 = retry_command()
    elif (count<retry_num+reboot_num+reset_num+1): #factory reset and retry
        # action=input("factory reset continue or not [y/n]...")
        # action=action.lower()
        # if action=='y':
        #     hotkey('alt','F6')
        #     time.sleep(3)
        #reboot to check roboot times
        print("reboot to check roboot times")
        os.system('adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X reboot')
        time.sleep(60)
        #check txt
        # with open('record_disconnect.txt','r') as f:
        #     data = f.read()
        #     for line in f:
        #         line=line.strip('\n')
        #         if len(line)!=0:
        #             dis_devices.append(line)
        #     print('txt dis_devices:',dis_devices)

        # for i in devices:
        #     serial = i
        #     d_count=0
        #     disconnect=yaqing.disconnect(serial,d_count)
        #     print("disconnect device:",disconnect)
        #     if disconnect != 32512:
        #         dis_devices.append(disconnect)
        # print(dis_devices)

        # if dis_devices != None:
        #     for i in dis_devices:
        #         for j in devices:
        #             if (i==j):
        #                 devices.remove(i)
        #                 print("devices:",devices)
        #                 break
        devices= yaqingtest.renewdevices(devices)
        # check='y'
        # devices,check= yaqingtest.renewdevices(devices,check)
        # while check == 'n':
        #     devices,check= yaqingtest.renewdevices(devices,check)

        # input("reset continue or not [y/n]...")
        try:
            # d = u2.connect(serial)
            os.system(reset_command)
        except Exception as e:
            print('Error!: {c},Message, {m}'.format(c=type(e).__name__,m=str(e)))
        # time.sleep(60)

        # input("multi_devices_setup4 continue or not [y/n]...")
        os.system('python3 multi_devices_setup4.py')

        # input("cts_device_setup_for_chrome_Jonathan4 continue or not [y/n]...")
        os.system('python3 cts_device_setup_for_chrome_Jonathan4.py')

        # input("CTS_All_devices_setting4 continue or not [y/n]...")
        os.system('python CTS_All_devices_setting4.py')

        #Parallel(n_jobs=-1)(delayed(factory_reset_time_setup)(c) for c in devices)
        
        # action1=input("final continue or not [y/n]...")
        # action1=action1.lower()
        # if action1=='y':
        #     hotkey('alt','F6')
        #     time.sleep(3)
        factory_reset(r1)
        exit()
        time.sleep(30)
        retry = test()
        r1 = retry_command()
        
    else: #exit after factory reset 15 times
        retry = 0
     
    count = count + 1
    print(retry)

os.chdir(f'/home/{UsrName}/Desktop/IMAGE/workspace/Pipeline_Testing')
os.system('python3 latestfolder.py')
os.chdir(f'/home/{UsrName}/Desktop/IMAGE/workspace/Pipeline_Testing')
# os.system('python3 Auto_login.py')
os.system('python3 finalsendmail.py')

# with open(f'/home/{UsrName}/Desktop/IMAGE/workspace/RecordOption.txt','r')as f:
#     r = f.read().split('/')
# if 'gts' in r:
#     dirpath = f'/home/{UsrName}/Desktop/IMAGE/'
#     for root,dirs,files in os.walk(dirpath):
#         for dir in dirs:
#             print(os.path.join(root,dir))
#             dirpath = os.path.join(root,dir)
#             os.chdir(dirpath)
#             os.system('./jen.sh')
# elif 'sts' in r:
#     dirpath = f'/home/{UsrName}/Desktop/IMAGE/'
#     for root,dirs,files in os.walk(dirpath):
#         for dir in dirs:
#             print(os.path.join(root,dir))
#             dirpath = os.path.join(root,dir)
#             os.chdir(dirpath)
#             os.system('./jen.sh')



# os.environ['DISPLAY'] = ':0'





# check = False
# import shutil







# shutil.copyfile(latest[-1]+'/test_result_failures_suite.html','/home/logo007/Desktop/IMAGE/workspace/Pipeline_Testing/11_r10/android-cts-11_r10-linux_x86-arm/android-cts/results/latest_test_result.html')
# shutil.copyfile(latest[-1]+'/compatibility_result.css','/home/logo007/Desktop/IMAGE/workspace/Pipeline_Testing/11_r10/android-cts-11_r10-linux_x86-arm/android-cts/results/compatibility_result.css')