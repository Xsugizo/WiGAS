#! /usr/bin/env python
import time
import os
import csv
import re
import subprocess
import globalvar
globalvar.initialize()
dirpath = globalvar.path
###vscode must install Code Runner to excute the special sign in path.###

#init
path = dirpath+"/android-cts/tools"
get_image ='adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X shell getprop ro.odm.build.fingerprint'
runcode ='/home/logo113/Desktop/IMAGE/workspace/Pipeline_Testing/'
setup = '/home/logo113/Desktop/IMAGE/workspace/CTS_All_devices_setting/'

run_turn  = 87
run_reboot = 1
run_factory = 1

#change cmd path 
os.chdir(path)

#get image and run shell
def run_code(image,runcode):
    #get image name
    out_image = os.popen(image).read()
    #print(out_image)
    out_image = out_image.split('/')

    #run shell
    os.chdir(runcode)
    os.system('sh runcts.sh')
    #shellscript = subprocess.Popen(runcode,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    print("wait for run...")

    # returncode = shellscript.wait()
    # for line in shellscript.stdout:
    #     print(line.rstrip())
    # returncode +=""
    try:
        return(out_image[3]+"_"+out_image[1])
    except:
        return("error: no devices/emulators found")

#save result from l r into test.csv
def save_and_read():
    test_pass =[]
    test_fail =[]
    test_image =[]
    test_devices = []
    output = os.popen('./cts-tradefed l r').read()
    file = open("test_file.csv","w")
    file.write(output)
    file.close()

    #delete top 10 gts-intro lines 
    with open('test_file.csv','r') as f:
        data = f.readlines()

    #save as test_file.csv 
    with open('test_file.csv','w')as f:
        for count, line in enumerate(data):
            line  = re.sub('\s+',',',line)
            if(count>=11):
                f.write(line+'\n')

    #Read Pass and Fail number and calculate the rate
    with open('test_file.csv','r')as file_obj:
        reader_obj = csv.reader(file_obj)
        for lines in reader_obj:
            
            #cleaning lines
            try:
                test = lines[1]+" "+lines[2]+" "+lines[9]+" "+lines[10]
                if(lines[9]==""):
                    print("image error")
                    continue
                
            except:
                #print("no data in lines")
                continue
            
            #save as new list and check data type
            try:
                test_pass.append(int(lines[1])) 
                test_fail.append(int(lines[2]))
                test_image.append(lines[9])
                test_devices.append(lines[10])

            except:
                #print("data type error")
                continue

    print("l r Saving...") 
    return test_pass,test_fail,test_image,test_devices

#print(test_pass,test_fail,test_image,test_devices)

test_count = []
project_count = []
project_num =0 
count_num =1
#project_count index:project_num, obj:count_num
#test_count index:project_num, obj:project_name

#counting the list
def counting(image, devices, fail):
    test_count = []
    project_count = []
    pro_num =0 
    count_num =1
    fail_num =[]

    #count the project and image in l r list
    for i in range(len(image)):
        project_name = image[i]+"_"+devices[i]

        if(len(test_count)==0):
            test_count.insert(pro_num,project_name)
            project_count.insert(pro_num,count_num)
            fail_num.insert(pro_num,fail[i])
            pro_num +=1
            continue

        for j in range(len(test_count)):
            if(project_name==test_count[j]):
                project_count[j] += 1

                if(fail_num[j] > fail[i]):
                    fail_num [j] =fail_num[j]-fail[i]
                break

            elif(j == len(test_count)-1):
                test_count.insert(pro_num,project_name)
                project_count.insert(pro_num,count_num)
                fail_num.insert(pro_num,fail[i])
                pro_num +=1   

    print(test_count,project_count,fail_num)
    return test_count,project_count,fail_num
            
#insert element(new image) to list        
def count_insert(num,name):
    test_count.insert(num,name)
    project_count.insert(num,count_num)

#check if device is available
def device_check():
    try:
        device = os.popen('adb devices').read()
        device = device.split()
        check = device[4]
        print(check)
        
    except:
        time.sleep(5)
        device_check()

#factory reset all devices
def factory_re():
    os.system('adb devices')
    os.system('adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X reboot bootloader')
    time.sleep(20)
    os.system('fastboot devices')
    os.system('fastboot devices |  cut -sf 1 | xargs -IX fastboot -s X erase userdata')
    os.system('fastboot devices |  cut -sf 1 | xargs -IX fastboot -s X reboot')

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

#run turns >> num == run turn, num2 == reboot turn, num3 == factory reset turn
def run_cts(num,num2,num3,device_image,t_count,p_count,f_count):
    
    for i in range(len(t_count)):
        
        if(device_image == t_count[i]):
            while(p_count[i]<num):
                #run turn
                device_image = run_code(get_image,runcode)
                test_pass,test_fail,test_image,test_devices = save_and_read()
                print("Finish turns >>")
                t_count,p_count,f_count= counting(test_image,test_devices,test_fail)

                if f_count[i]<=10:
                    print("test fail <=10 than last test")
                    print("End Test")
                    break                

            while(p_count[i]<num+num2):
                #run reboot 
                print("go reboot round...")
                os.system('adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X reboot')
                device_check()
                device_image = run_code(get_image,runcode)
                test_pass,test_fail,test_image,test_devices = save_and_read()
                t_count,p_count,f_count= counting(test_image,test_devices,test_fail)

                if f_count[i]<=10:
                    print("test fail <=10 than last test (Reboot)")
                    print("End Reboot Test")
                    break
            
            # while(p_count[i]<num+num2+num3):
            #     #finish round to reboot >> factory reset
            #     print("go factory reset round...")
            #     factory_re()
            #     os.chdir(setup)
            #     device_check()
            #     str_de = device_str()
            #     os.system('python3 multi_devices_setup2.py '+str_de)
            #     os.chdir(path)
               
            #     device_image = run_code(get_image,runcode)
            #     test_pass,test_fail,test_image,test_devices = save_and_read()
            #     t_count,p_count,f_count= counting(test_image,test_devices,test_fail)

            #     if f_count[i]<=10:
            #         print("test fail <=10 than last test (Factory)")
            #         print("End Factory Test")
            #         break

#save l r result and read into list to count
test_pass,test_fail,test_image,test_devices = save_and_read()

#counting the list
t_count,p_count,f_count = counting(test_image,test_devices,test_fail)
print("Before Turns >>")

#run code and return list include image
if(len(t_count)==0):
    device_image = run_code(get_image,runcode)
    device_image = run_code(get_image,runcode)
else:
    device_image = run_code(get_image,runcode)

#save l r result and read into list to count
test_pass,test_fail,test_image,test_devices = save_and_read()

#counting the list
t_count,p_count,f_count = counting(test_image,test_devices,test_fail)

#run_cts(reboot num,factory num)
run_cts(run_turn,run_reboot,run_factory,device_image,t_count,p_count,f_count)


