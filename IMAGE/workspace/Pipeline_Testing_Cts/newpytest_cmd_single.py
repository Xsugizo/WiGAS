#! /usr/bin/env python3

from re import X
import time
import os
import signal
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
command_list=[]
d_count=None
coun=""
pid=""
process_name=""
UsrName = subprocess.check_output('whoami')
UsrName = UsrName.decode().strip()

#list to string
def listToString(s):
    # initialize an empty string
    str1 = ""
    i=0
    # traverse in the string
    for ele in s:
        if(i==0):
            str1 += ele
        else:
            str1 += " "+ ele
        # print(ele)
        i=i+1
    # return string
    return str1
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
print("count="+str(len(devices)))



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

def firstII(cts):
    android_home = dirpath
    cts_command = android_home + "/android-cts/tools/cts-tradefed"
    shard_count = str(len(devices))
    command_list = [cts_command, "run", "cts", "--shard-count", shard_count]
    # command_list = [cts_command, "run", "cts --abi arm64-v8a -m CtsCameraTestCases", "--shard-count", shard_count]
    # command_list = [cts_command, "run", "cts --abi arm64-v8a -m CtsThemeHostTestCases", "--shard-count", shard_count]
    # command_list = [cts_command, "run", "cts --abi arm64-v8a -m CtsAppUsageHostTestCases", "--shard-count", shard_count]
    for serial_number in devices:
        command_list += ["-s", serial_number]
    # subprocess.run(f"gnome-terminal -- bash -c '{command_list}'", shell=True)
    print(listToString(command_list))
    # check =input('Please comfirm all devices have entered fastboot mode [y/n] ...')
    p=subprocess.Popen(f"gnome-terminal -- bash -c '{listToString(command_list)}'", shell=True)
    p_pid=p.pid
    time.sleep(5)
    p_pid = subprocess.check_output(f"pgrep -l -u '{UsrName}'| grep cts-tradefed | tail -1", shell=True) # get the process id
    p_id=p_pid.decode("utf-8").split()
    pid=int(p_id[0])
    print(p_id[0])
    return pid



def clean():
    print("Enter clean() ...")
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
    print("Over clean() ...")
# retry command after finishing CTS0
def retry_time(r1):
    typewrite(r1)
    press('enter')
    time.sleep(10)

def retry_timeII(r1):
    print("retry_timeII")
    android_home = dirpath
    gts_command = android_home + "/android-cts/tools/cts-tradefed"
    r1=gts_command +" "+r1
    print("r="+r1)
    # check =input('Please comfirm all devices have entered fastboot mode [y/n] ...')
    pp=subprocess.Popen(f"gnome-terminal -- bash -c '{r1}'", shell=True)
    pp_pid=pp.pid
    time.sleep(5)
    pp_pid = subprocess.check_output(f"pgrep -l -u '{UsrName}'| grep cts-tradefed | tail -1", shell=True) # get the process id
    pp_id=pp_pid.decode("utf-8").split()
    ppid=int(pp_id[0])
    print(pp_id[0])
    return ppid


#reboot command and retry
def reboot_time(r1):
    os.system('adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X reboot')
    time.sleep(60)
    typewrite(r1)
    press('enter')
    time.sleep(10)

def reboot_timeII(r1):
    os.system('adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X reboot')
    time.sleep(60)
    android_home = dirpath
    gts_command = android_home + "/android-cts/tools/cts-tradefed"
    r1=gts_command +" "+r1
    # subprocess.run(f"gnome-terminal -- bash -c '{command_list}'", shell=True)
    print("r="+r1)
    # check =input('Please comfirm all devices have entered fastboot mode [y/n] ...')
    pp=subprocess.Popen(f"gnome-terminal -- bash -c '{r1}'", shell=True)
    pp_pid=pp.pid
    time.sleep(5)
    pp_pid = subprocess.check_output(f"pgrep -l -u '{UsrName}' | grep cts-tradefed | tail -1", shell=True) # get the process id
    pp_id=pp_pid.decode("utf-8").split()
    ppid=int(pp_id[0])
    print(pp_id[0])
    return ppid

#set up after factory reset
def factory_reset_time_setup(id):
    time.sleep(60)
    os.system('python3 multi_devices_setup3.py '+str(id))
    os.system('python CAD_test.py --name '+str(id))
    os.system('python3 cts_device_setup_for_chrome.py '+str(id))

def get_latestfolder():
    check = False
    # latestfolder=""
    checkfolder = False
    directory = dirpath+'/android-cts/results'
    flagg=0
    # directory = '/media/logo007/1TBHD/IMAGE/workspace/Pipeline_Testing/11_r10/android-cts-11_r10-linux_x86-arm/android-cts/results'
    latest=sorted([os.path.join(directory,d) for d in os.listdir(directory)],key=os.path.getctime)
    for i in latest:
        if i == dirpath+'/android-cts/results/latest':
            latest.remove(dirpath+'/android-cts/results/latest') 
        #   if i == '/media/logo007/1TBHD/IMAGE/workspace/Pipeline_Testing/11_r10/android-cts-11_r10-linux_x86-arm/android-cts/results/latest':
        #     latest.remove('/media/logo007/1TBHD/IMAGE/workspace/Pipeline_Testing/11_r10/android-cts-11_r10-linux_x86-arm/android-cts/results/latest')  
    latestfolder=latest[-1]
    print("lastfolder"+latestfolder)
    return latestfolder

#retry command after factory reset
def factory_reset(r1):
    typewrite(r1)
    press('enter')
    time.sleep(10)
def factory_resetII(r1):
    android_home = dirpath
    gts_command = android_home + "/android-cts/tools/cts-tradefed"
    r1=gts_command +" "+r1
    # subprocess.run(f"gnome-terminal -- bash -c '{command_list}'", shell=True)
    print("r="+r1)
    # check =input('Please comfirm all devices have entered fastboot mode [y/n] ...')
    pp=subprocess.Popen(f"gnome-terminal -- bash -c '{r1}'", shell=True)
    pp_pid=pp.pid
    time.sleep(5)
    pp_pid = subprocess.check_output(f"pgrep -l -u '{UsrName}' | grep cts-tradefed | tail -1", shell=True) # get the process id
    pp_id=pp_pid.decode("utf-8").split()
    ppid=int(pp_id[0])
    print(pp_id[0])
    return ppid
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
    # latestfolder=""
    checkfolder = False
    directory = dirpath+'/android-cts/results'
    flagg=0
    # # directory = '/media/logo007/1TBHD/IMAGE/workspace/Pipeline_Testing/11_r10/android-cts-11_r10-linux_x86-arm/android-cts/results'
    # latest=sorted([os.path.join(directory,d) for d in os.listdir(directory)],key=os.path.getctime)
    # for i in latest:
    #     if i == dirpath+'/android-cts/results/latest':
    #         latest.remove(dirpath+'/android-cts/results/latest') 
    #     #   if i == '/media/logo007/1TBHD/IMAGE/workspace/Pipeline_Testing/11_r10/android-cts-11_r10-linux_x86-arm/android-cts/results/latest':
    #     #     latest.remove('/media/logo007/1TBHD/IMAGE/workspace/Pipeline_Testing/11_r10/android-cts-11_r10-linux_x86-arm/android-cts/results/latest')  
    # latestfolder=latest[-1] 
    # print("latestfolder="+latest[-1])
    print("latestfolder="+latestfolder)  
    while checkfolder == False:
        latest=sorted([os.path.join(directory,d) for d in os.listdir(directory)],key=os.path.getctime)
        flagg=flagg+1
        for i in latest:
            if i == dirpath+'/android-cts/results/latest':
                latest.remove(dirpath+'/android-cts/results/latest')
            # if i == '/media/logo007/1TBHD/IMAGE/workspace/Pipeline_Testing/11_r10/android-cts-11_r10-linux_x86-arm/android-cts/results/latest':
            #     latest.remove('/media/logo007/1TBHD/IMAGE/workspace/Pipeline_Testing/11_r10/android-cts-11_r10-linux_x86-arm/android-cts/results/latest')
        # if(latest[-1]!=latestfolder):
        #     checkfolder=True
        # if flagg==0:
        #     print("new latestfolder="+latest[-1])
        #     print("latestfolder="+latestfolder)
        # if checkfolder==True:
        #     print("new latestfolder="+latest[-1])
        #     print("latestfolder="+latestfolder)
        if(latest[-1]!=latestfolder):
            checkfolder=True
        if flagg==0:
            print("flagg new latestfolder="+latest[-1])
            print("flagg latestfolder="+latestfolder) 
        if checkfolder==True:
            print("checkfolder new latestfolder="+latest[-1])
            print("checkfolder latestfolder="+latestfolder) 
        flag=0
    while check == False: 
        check = os.path.exists(latest[-1]+"/test_result_failures_suite.html")
        if flag==0:
            print(check)
            print(latest[-1])
            print("pid="+str(pid))
            print("process_name="+str(process_name))
            if r1=="":
                print("command="+str(command_list))
            else:
                print("command="+r1)
            print("count="+str(count)+" retry_num="+str(retry_num)+" reboot_num="+str(reboot_num) + " retry=" +str(retry))
            flag=flag+1
        if check == True:
            print(check)
            print(latest[-1])
            print("pid="+str(pid))
            print("command="+r1)
            print("process_name="+str(process_name))
            print("count="+str(count)+" retry_num="+str(retry_num)+" reboot_num= "+str(reboot_num) + " retry=" +str(retry))
            time.sleep(10)


        

runfre = []
with open(f'/home/{UsrName}/Desktop/IMAGE/workspace/runfre.txt') as file:
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
with open(f'/home/{UsrName}/Desktop/IMAGE/workspace/RecordTestOption.txt','r')as f:
    testoption = f.read().split('/')
print("testoption= "+str(testoption))
if 'retry' in testoption:
    count = 1
elif 'reboot' in testoption:
    count = 1
elif 'factoryreset' in testoption:
    count = 1
else:
    count = 0
if(count==1): # gen cmd for retry for retry, reboot and   
    print("test")
    retry = test()
    print("retry_command")
    r1 = retry_command()
    print("r1=" +r1)
else:
    r1 = ''

while (retry==1):

    os.chdir(f'/home/{UsrName}/Desktop/IMAGE/workspace/Pipeline_Testing_Cts') #ensure the path is correct
    print("count="+str(count)+" retry_num="+str(retry_num)+" reboot_num="+str(reboot_num)+" reset_num="+ str(reset_num))

    if (count<retry_num+reboot_num+1): #retry+reboot time
        if (count == 0): #run cts first time
            # first(cts)
            print("get_latestfolder")
            latestfolder=get_latestfolder()
            print("first try processs")
            process_name="first try process"
            pid=firstII(cts)
            print("exit")
            exit()
            
            print("clean")
            clean() #clean past directory
            time.sleep(30)
            print("test")
            retry = test()
            print("retry_command")
            r1 = retry_command()
            os.kill(pid, signal.SIGTERM)
            print(" count="+str(count)+" retry_num="+str(retry_num)+" reboot_num="+str(reboot_num))
        elif (count < retry_num+1): # check retry run how many times
            # retry_time(r1)
            print("get_latestfolder")
            latestfolder=get_latestfolder()
            print("retry process")
            process_name="retry process"
            pid=retry_timeII(r1)
            exit()
            time.sleep(30)
            print("test")
            retry = test()
            r1 = retry_command()
            os.kill(pid, signal.SIGTERM)
            print(" count="+str(count)+" retry_num="+str(retry_num)+" reboot_num="+str(reboot_num))
        else: #check reboot run how many times 
            # reboot_time(r1)
            print("get_latestfolder")
            latestfolder=get_latestfolder()
            print("reboot process")
            process_name="reboot process"
            pid=reboot_timeII(r1)
            exit()
            time.sleep(30)
            print("test")
            retry = test()
            r1 = retry_command()
            os.kill(pid, signal.SIGTERM)
            print(" count="+str(count)+" retry_num="+str(retry_num)+" reboot_num="+str(reboot_num))

    elif (count<retry_num+reboot_num+reset_num+1): #factory reset and retry
        # action=input("factory reset continue or not [y/n]...")
        # action=action.lower()
        # if action=='y':
        #     hotkey('alt','F6')
        #     time.sleep(3)
        #reboot to check roboot times
        print("reboot to check roboot times")
        process_name="reboot to check roboot times"
        os.system('adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X reboot')
        print("sleep 60 sec wait for factroty reset")
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
        print(" count="+str(count)+" retry_num="+str(retry_num)+" reboot_num="+str(reboot_num))
        print("sleep 90 sec wait for factroty reset")
        time.sleep(90)

        # input("cts_device_setup_for_chrome_Jonathan4 continue or not [y/n]...")
        print("run multi_session_device_setup_factory_rest")
        os.system('python3 multi_session_device_setup_factory_rest.py')# os.system('python3 cts_device_setup_for_chrome_Jonathan4.py')

        # input("CTS_All_devices_setting4 continue or not [y/n]...")
        # os.system('python CTS_All_devices_setting4.py')

        #Parallel(n_jobs=-1)(delayed(factory_reset_time_setup)(c) for c in devices)
        
        # action1=input("final continue or not [y/n]...")
        # action1=action1.lower()
        # if action1=='y':
        #     hotkey('alt','F6')
        #     time.sleep(3)
        # factory_reset(r1)
        print("get_latestfolder")
        latestfolder=get_latestfolder()
        print("factory_reset process")
        process_name="factory_reset process"
        pid=factory_resetII(r1)
        exit()
        time.sleep(30)
        print("test")
        retry = test()
        r1 = retry_command()
        os.kill(pid, signal.SIGTERM)
        print("count="+str(count)+" retry="+str(retry)+" reboot_num"+str(reboot_num))
        
    else: #exit after factory reset 15 times
        retry = 0
     
    count = count + 1
    print("retry="+str(retry))

os.chdir(f'/home/{UsrName}/Desktop/IMAGE/workspace/Pipeline_Testing_Cts')
os.system('python3 latestfolder.py')
os.chdir(f'/home/{UsrName}/Desktop/IMAGE/workspace/Pipeline_Testing_Cts')
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