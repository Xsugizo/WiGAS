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
CurrPath=os.getcwd()
ParetPath=os.path.dirname(CurrPath)
print("CheckY CurrPath="+str(CurrPath)+"CheckY ParetPath="+str(ParetPath))


def test():

    #init
    # print("Start Count")
    print("globalvar.path="+dirpath)
    path = dirpath+"/android-cts/tools"
    image ='adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X shell getprop ro.odm.build.fingerprint'
    #change cmd path 
    os.chdir(path)

    dut = []
    adb_devices= subprocess.check_output(["adb", "devices"])
    print(adb_devices)
    for i in adb_devices.split(b"\tdevice"):
        for ii in i.split(b"\n"):
            ii=ii.decode('utf-8')
            if  ii !=" " and ii not in "List of devices attached" :
                dut.append(ii)

    #save result from l r into test.csv
    def save_and_read():
        test_session =[]
        test_fail =[]
        test_pass =[]
        test_Moudle =[]
        test_result =[]
        test_image =[]
        test_devices = []
        output = os.popen('./cts-tradefed l r').read()
        file = open("test_file.csv","w")
        file.write(output)
        file.close()
        row=""
        length=0

        #delete top 10 gts-intro lines 
        with open('test_file.csv','r') as f:
            data = f.readlines()

        #save as test_file.csv 
        with open('test_file.csv','w')as f:
            for count, line in enumerate(data):
                line  = re.sub('\s+',',',line)
                # if(count>=11):
                # if(count>=12):
                #     f.write(line+'\n')
                if("Session" in line ):
                    row=count

                if(row!=""):
                    f.write(line+'\n')

        #Read Pass and Fail number and calculate the rate
        with open('test_file.csv','r')as file_obj:
            reader_obj = csv.reader(file_obj)
            
            for lines in reader_obj:
                length = len(lines)
                #print(lines)
                #cleaning lines
                try:
                    # test = lines[0]+" "+lines[2]+" "+lines[11]+" "+lines[12]
                    test = lines[0]+" "+lines[1]+" "+lines[2]+" "+lines[3]+" "+lines[5]+" "+lines[length-3]+" "+lines[length-2]
                    print(test)
                    # if(lines[11]==""):
                    if(lines[length-3]==""):
                        #print("image error")
                        continue
                    
                except:
                    #print("no data in lines")
                    continue
                
                #save as new list and check data type
                try:
                    test_session.append(int(lines[0])) 
                    test_fail.append(int(lines[2]))
                    test_pass.append(int(lines[1]))
                    test_Moudle.append(int(lines[3]))
                    test_result.append(int(lines[5]))
                    # test_image.append(lines[11])
                    # test_devices.append(lines[12])
                    test_image.append(lines[length-3])
                    test_devices.append(lines[length-2])

                except:
                    #print("data type error")
                    continue
        print("test_session="+str(test_session)+"test_fail="+str(test_fail)+"test_image="+str(test_image)+"test_Moudle="+str(test_Moudle)+"test_Result="+str(test_result)+"test_devices="+str(test_devices)+"test_pass="+str(test_pass) )    
        #print("l r Saving...") 
        return test_session,test_fail,test_image,test_devices,test_pass,test_Moudle,test_result

    #print(test_pass,test_fail,test_image,test_devices)

    test_count = []
    project_count = []
    project_num =0 
    ans = 0
    count_num =1
    fail_gap = []

    #counting the list
    def counting(image, devices, fail,session,test_pass):
        test_count = []
        project_count = []
        pro_num =0 
        count_num =1
        fail_num =[]
        pass_num =[]
        s_num = []

        
        productname= subprocess.check_output(["adb","-s",dut[0],"shell","getprop","ro.product.name"])
        finngerprint= subprocess.check_output(["adb","-s",dut[0],"shell","getprop","ro.system.build.id"])
        productname=productname.split(b"\n")
        productname=productname[0].decode("utf-8")
        finngerprint=finngerprint.split(b"\n")
        finngerprint=finngerprint[0].decode("utf-8")
        print("productname="+productname,"finngerprint"+finngerprint)
        target=finngerprint+"_"+productname
        print("target="+target)
        print(len(image))
        #count the project and image in l r list
        for i in range(len(image)-1,0,-1):
            project_name = image[i]+"_"+devices[i]
            # print("project_name="+project_name)
            if(project_name==target):
                test_count.insert(pro_num,image[i]+"_"+devices[i])
                project_count.insert(pro_num,count_num)
                fail_num.insert(pro_num,fail[i])
                pass_num.insert(pro_num,test_pass[i])
                s_num.insert(pro_num,session[i])
                break
            else:
                continue
        for i in range(len(image)-1,0,-1):
            project_name = image[i]+"_"+devices[i]

            # if(len(test_count)==0):
            #     test_count.insert(pro_num,project_name)
            #     project_count.insert(pro_num,count_num)
            #     fail_num.insert(pro_num,fail[i])
            #     pass_num.insert(pro_num,test_pass[i])
            #     s_num.insert(pro_num,session[i])
            #     pro_num +=1
            #     continue

            if(len(test_count)==0):
                # test_count.insert(pro_num,image[-1]+"_"+devices[-1])
                # project_count.insert(pro_num,count_num)
                # fail_num.insert(pro_num,fail[-1])
                # pass_num.insert(pro_num,test_pass[-1])
                # s_num.insert(pro_num,session[-1])
                # pro_num +=1
                continue

            for j in range(len(test_count)):
                if(project_name==test_count[j]):
                    project_count[j] += 1

                    # if(fail[i]<=fail_num[j]):
                    if(test_pass[i]>=pass_num[j]):
                        fail_num[j] = fail[i]
                        pass_num[j] = test_pass[i]
                        s_num[j] = session[i]
                        
                    break


                # elif(j == len(test_count)-1):
                #     test_count.insert(pro_num,project_name)
                #     project_count.insert(pro_num,count_num)
                #     fail_num.insert(pro_num,fail[i])
                #     pass_num.insert(pro_num,test_pass[i])
                #     s_num.insert(pro_num,session[i])
                #     pro_num +=1   

        print("test_count="+str(test_count)+"project_count="+str(project_count)+"fail_num="+str(fail_num)+"s_num="+str(s_num)+"pass_num="+str(pass_num))
        return test_count,project_count,fail_num,s_num,pass_num
                
    def fail_gap(t_count,fail,image,devices):
        fail_gap = []
        fail_num = -1
        for i in range(len(t_count)):
            
            for j in range(len(fail)):
                if(image[j]+"_"+devices[j] == t_count[i]):
                    
                    if(fail_num==-1):
                        fail_gap.insert(i,fail[j])
                        fail_num = fail[j]
                        continue
                    else:
                        if(fail_num>fail[j]):
                            fail_gap[i] = fail_num - fail[j]
                            fail_num = fail[j]
                if(j == len(fail)-1):
                    fail_num =-1
                                            
        #print(fail_gap)
        return fail_gap
    
    def retry_or_not_retry(fail,test_moudle,test_result,image,devices):

        productname= subprocess.check_output(["adb","-s",dut[0],"shell","getprop","ro.product.name"])
        finngerprint= subprocess.check_output(["adb","-s",dut[0],"shell","getprop","ro.system.build.id"])
        productname=productname.split(b"\n")
        productname=productname[0].decode("utf-8")
        finngerprint=finngerprint.split(b"\n")
        finngerprint=finngerprint[0].decode("utf-8")
        target=finngerprint+"_"+productname
        
        for i in range(len(image)-1,0,-1):

            project_name = image[i]+"_"+devices[i]
            # print("retry_or_not_retry project_name="+project_name)

            # print("test_moudle[-1]="+str(test_moudle[-1])+"test_result[-1]="+str(test_result[-1])+"fail="+str(fail[-1]))
            if(project_name==target):
                if (test_moudle[i]==test_result[i] and fail[i]==0):
                    print("stop_retry")
                    return "stop_retry"
                else:
                    print("keep_retry")
                    return "keep_retry"
                break
            else:
                continue



    #save l r result and read into list to count
    session,test_fail,test_image,test_devices,test_pass,test_moudle,test_result = save_and_read()
    print("session="+str(session)+"test_fail="+str(test_fail)+"test_image="+str(test_image)+"test_devices="+str(test_devices))

    #counting the list
    #project_count index:project_num, obj:count_num
    #test_count index:project_num, obj:project_name
    t_count,p_count,f_count,s_num,pass_num = counting(test_image,test_devices,test_fail,session,test_pass)
    print("t_count="+str(t_count)+"p_count="+str(p_count)+"f_count="+str(f_count)+"s_num="+str(s_num)+"pass_num="+str(pass_num))

    gap = fail_gap(t_count,test_fail,test_image,test_devices)
    goornogo = retry_or_not_retry(test_fail,test_moudle,test_result,test_image,test_devices)

    print("gap="+str(gap))

    def compare(s_sum,gap,f_num):
        image_num = 0
        ans = 0
        out_image = os.popen(image).read()
        #print(out_image)
        out_image = out_image.split('/')
        image_device = out_image[3]+"_"+out_image[1]
        print("image_device="+image_device)
        for i in range(len(t_count)):
            if(image_device == t_count[i]):
                image_num = i
                break
        if(gap[image_num]>=10):
            ans = 1
        elif(f_num[image_num] >= 5):
            ans = 1
        # print(s_sum[image_num],ans)
        # ans = 1 is ruuuuuun
        

        return s_sum[image_num],ans
    
    def compare_countiune(s_sum,goornogo):
        image_num = -1
        ans = 0
        # out_image = os.popen(image).read()
        # #print(out_image)
        # out_image = out_image.split('/')
        # image_device = out_image[3]+"_"+out_image[1]
        # print("image_device="+image_device)

        if(goornogo=="keep_retry"):
            ans = 1
        if(goornogo=="stop_retry"):
            ans = 0
        # print(s_sum[image_num],ans)
        # ans = 1 is ruuuuuun
        

        return s_sum[image_num],ans
    


    # session,ans = compare(s_num,gap,f_count)
    session,ans = compare_countiune(s_num,goornogo)
    print("session="+str(session)+"ans="+str(ans))

    def retry(session,action):
        devices = []

        adb_devices= subprocess.check_output(["adb", "devices"])
        for i in adb_devices.split(b"\tdevice"):
            for ii in i.split(b"\n"):
                if  ii != b"" and ii not in b"List of devices attached" :
                    x = ii.decode("utf-8")
                    devices.append(x)
        coun=str(len(devices))

        # 
        ii=0
        for i in devices:
            if ii==0:
                cmd= "--shard-count "+coun+ " -s "+ str(i)
                ii=ii+1
            else:
                cmd=cmd+" -s "+ str(i)

        print("cmd="+cmd)
        # if coun=='1' or action!='y':
        #     if coun=='1':
        #         send_mail('Ian_H_Chang@wistron.com,Jonathan_Tung@wistron.com', 'WiGAS retry setting', 'Error! Please check device Qty.')
        #     action=input("Continue or not [y/n]...")
        #     action=action.lower()
        #     if action=='y':
        #         retry(session,action)
        #         hotkey('alt','F6')
        #         time.sleep(3)
        #         # with open('/home/logo113/Desktop/IMAGE/workspace/Pipeline_Testing/retry.sh','w')as f:       
        #         #     f.write("#!/bin/bash"+'\n')
        #         #     f.write(f"cd {dirpath}/android-cts/tools"+'\n')
        #         #     f.write("./cts-tradefed run retry --retry "+str(session)+" "+cmd+'\n')
        #         # f.close()
        #     else:
        #         retry(session,action)
        # else:
        with open(f'{ParetPath}/ExcludefilterOption.txt','r')as f:
            ExcludefilterOption = f.read().split('/')
            print("ExcludefilterOption= "+str(ExcludefilterOption))
        
        if 'exfilter' in ExcludefilterOption[0]:
            print("add exfilter cmd")
            with open(f'{ParetPath}/exclude_filter.txt') as file:
                 ex_filter= file.read().replace('\n', '')
            with open(f'{CurrPath}/retry1.sh','w')as f:       
                f.write("run retry --retry "+str(session)+" "+cmd+" "+ex_filter+'\n')
            f.close()
            with open(f'{CurrPath}/notexecutretry1.sh','w')as f:       
                f.write("run retry --retry "+str(session)+" "+"--retry-type NOT_EXECUTED "+cmd+" "+ex_filter+'\n')
            f.close()
        else:    
            with open(f'{CurrPath}/retry1.sh','w')as f:       
                f.write("run retry --retry "+str(session)+" "+cmd+'\n')
            f.close()
            with open(f'{CurrPath}/notexecutretry1.sh','w')as f:       
                f.write("run retry --retry "+str(session)+" "+"--retry-type NOT_EXECUTED "+cmd+'\n')
            f.close()
        


    retry(session,'y')
    return ans




