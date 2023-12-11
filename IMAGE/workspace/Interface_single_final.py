# -*- coding: utf-8 -*-
import os
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter.filedialog import askdirectory
from tkinter import filedialog as fd
from time import sleep
from tqdm import tqdm
from alive_progress import alive_bar
import subprocess
import time
from tkinter import messagebox
from github import Github
import requests
from optparse import OptionParser
import re

UsrName = subprocess.check_output('whoami')
UsrName = UsrName.decode().strip()


# try : 
#     os.remove('path.txt')
# except:
#     print()

# Select path
def select_CtsTool():
    path = askdirectory(title ='Select CtsTool')
    path = path.replace('/','\\')
    var1.set(path)
    with open('CtsToolPath.txt', 'w') as f:
        f.write(path)

def select_CtsImage():
    path = askdirectory(title ='Select CtsImage')
    path = path.replace('/','\\')
    var11.set(path)
    if 'userdebug' in path:
        messagebox.showinfo("Warning","Ni how bun !")
    with open('CtsImagePath.txt', 'w') as f:
        f.write(path)

# Select path
def select_GtsTool():
    path = askdirectory(title ='Select GtsTool')
    path = path.replace('/','\\')
    var2.set(path)
    with open('GtsToolPath.txt', 'w') as f:
        f.write(path)

def select_GtsImage():
    path = askdirectory(title ='Select GtsImage')
    path = path.replace('/','\\')
    var22.set(path)
    with open('GtsImagePath.txt', 'w') as f:
        f.write(path)

# Select path
def select_StsTool():
    path = askdirectory(title ='Select StsTool')
    path = path.replace('/','\\')
    var3.set(path)
    with open('StsToolPath.txt', 'w') as f:
        f.write(path)

def select_StsImage():
    path = askdirectory(title ='Select StsImage')
    path = path.replace('/','\\')
    var33.set(path)
    with open('StsImagePath.txt', 'w') as f:
        f.write(path)


def start():
    
    with open(f'/home/{UsrName}/Desktop/IMAGE/workspace/RecordOption.txt','w')as f:
        if cts.get()!='--':
            f.write('cts/')
        if gts.get()!='--':
            f.write('gts/')
        if sts.get()!='--':
            f.write('sts')
    with open(f'/home/{UsrName}/Desktop/IMAGE/workspace/RecordTestOption.txt','w')as f:
        if Single_Test.get()!='--':
            f.write('est')

        

    with open('runfre.txt','w')as f:       
        f.write(str(ch11_var.get())+'\n')
        f.write(str(ch22_var.get())+'\n')
        f.write(str(ch33_var.get())+'\n')
        f.write(str(ch44_var.get())+'\n')
        f.close
        
    runfre = []
    with open(f'/home/{UsrName}/Desktop/IMAGE/workspace/runfre.txt') as file:
        for line in file.readlines():
            runfre.append(int(line))
    file.close()
    retry_num=runfre[0]
    reboot_num=runfre[1]
    reset_num=runfre[2]
    notexecuteset_num=runfre[3]
    com=tk.messagebox.askokcancel(title=None, message="請確認retry, reboot factoryRest and Not Executed 次數是否正確 retry_num="+str(retry_num)+" reboot_num="+str(reboot_num)+" reset_num="+str(reset_num)+" notexecuteset_num="+str(notexecuteset_num))
    print(com)
    if (com==True):
        print ("start test")
        with open('record_disconnect.txt','r+') as a:
            a.truncate(0)
            # root.destroy()
        with open(f'/home/{UsrName}/Desktop/IMAGE/workspace/RecordOption.txt','r')as f:
            r = f.read().split('/')
        print(r)
        if 'cts' in r:
            dirpath = f'/home/{UsrName}/Desktop/IMAGE/'
            for root,dirs,files in os.walk(dirpath):
                for dir in dirs:
                    if dir.find("Pipeline_Testing_Cts")!=-1:
                        print(os.path.join(root,dir))
                        dirpath = os.path.join(root,dir)
                        print(dirpath)
                        os.chdir(dirpath)
                        os.system('./jen_single_final.sh')
        elif 'gts' in r:
            dirpath = f'/home/{UsrName}/Desktop/IMAGE/'
            for root,dirs,files in os.walk(dirpath):
                for dir in dirs:
                    if dir.find("Pipeline_Testing_Gts")!=-1:
                        print(os.path.join(root,dir))
                        dirpath = os.path.join(root,dir)
                        print(dirpath)
                        os.chdir(dirpath)
                        os.system('./jen.sh')
        elif 'sts' in r:
            dirpath = f'/home/{UsrName}/Desktop/IMAGE/'
            for root,dirs,files in os.walk(dirpath):
                for dir in dirs:
                    if dir.find("Pipeline_Testing_Sts")!=-1:
                        print(os.path.join(root,dir))
                        dirpath = os.path.join(root,dir)
                        print(dirpath)
                        os.chdir(dirpath)
                        os.system('./jen.sh')
    else:
        pass


    # with open(f'/home/{UsrName}/Desktop/IMAGE/workspace/RecordTestOption.txt','r')as f:
    #     r = f.read().split('/')
    # print(r)
    # if 'retry' in r:

    # elif 'reboot' in r:

    # elif 'factoryreset' in r:


# def show():
#     # download()
#     os.system(f'python pipeline.py')
#     with alive_bar(16000) as bar:
#         for _ in range(16000):
#             time.sleep(.001)
#             bar()
def check_github_status():


    # GitHub repository details
    repo_owner = 'Xsugizo'  # Replace with the repository owner's username
    repo_name = 'WiGAs'  # Replace with the repository name
    file_path = f'/home/{UsrName}/Desktop/IMAGE/'  # Replace with the path to the file in the repository
    api_url="https://api.github.com/repos/Xsugizo/WiGAS"

    all_info=requests.get(api_url).json()
    last_updated=time.mktime(time.strptime(all_info["pushed_at"],"%Y-%m-%dT%H:%M:%SZ"))


    # # GitHub access token (optional but might be needed for private repositories or to avoid rate limits)
    # access_token = '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'  # Replace with your GitHub access token

    # # Initialize Github object
    # if access_token:
    #     g = Github(access_token)
    # else:
    #     g = Github()

    # # Get the repository
    # # repo = g.get_repo(f"{repo_owner}/{repo_name}")


    # last_updated = repo.pushed_at


    path = f"/home/{UsrName}/Desktop/git/IMAGE/workspace/"
 
    ti_m = os.path.getmtime(path)
    
    
    m_ti = time.ctime(ti_m)
    ml_ti = time.ctime(last_updated)
    
    # Using the timestamp string to create a 
    # time object/structure
    t_obj = time.strptime(m_ti)
    la_obj = time.strptime(ml_ti)
    # Transforming the time object to a timestamp 
    # of ISO 8601 format
    T_stamp = time.strftime("%Y-%m-%d %H:%M:%S", t_obj)
    L_stamp = time.strftime("%Y-%m-%d %H:%M:%S", la_obj)
    print(f"The file located at the path {path} was last modified at {T_stamp}")
    print(f"Github Last updated: {L_stamp}")
    if L_stamp>T_stamp:
        print("update")
        return "update"
        
    else:
        print("no_update")
        return "no_update"
    


def update_code():
    cwd = os.getcwd()
    cwd=cwd.split('/workspace')
    command = 'git stash'
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, cwd=cwd[0])    
    command = 'git pull https://github.com/Xsugizo/WiGAS.git'
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, cwd=cwd[0])
    output, unused_err = process.communicate()
    print(output)
    root.destroy()

def close_window():
    root.destroy()

root = tk.Tk()
root.title("WiGAS")
root.resizable(False, False)
root.geometry('590x400')
try:
    with open('CtsToolPath.txt','r') as f:
        CtsToolPath = f.read()
except:
        CtsToolPath = ""

try:
    with open('GtsToolPath.txt','r') as f:
        GtsToolPath = f.read()
except:
        GtsToolPath = ""
try:
    with open('StsToolPath.txt','r') as f:
        StsToolPath = f.read()
except:
        StsToolPath = ""
try:
    with open('CtsImagePath.txt','r') as f:
        CtsImagePath = f.read()
except:
        CtsImagePath = ""
try:
    with open('GtsImagePath.txt','r') as f:
        GtsImagePath = f.read()
except:
        GtsImagePath = ""
try:
    with open('CtsImagePath.txt','r') as f:
        StsImagePath = f.read()
except:
        StsImagePath = ""
var1 = tk.StringVar(value=CtsToolPath)
var2 = tk.StringVar(value=GtsToolPath)
var3 = tk.StringVar(value=StsToolPath)
var11 = tk.StringVar(value=CtsImagePath)
var22 = tk.StringVar(value=GtsImagePath)
var33 = tk.StringVar(value=StsImagePath)

# 創建一個框架
frame = tk.Frame(root)
frame.pack()

# 創建標籤並添加到框架中
label = tk.Label(frame, text="GMS Auto Test w/ Single Test V1", font = ('Bahnschrift',20,'bold'),pady=10)
label.pack(side=tk.TOP)

# 創建一個框架
frame2 = tk.Frame(root)
frame2.pack()

# 創建三個 Checkbutton
cts = tk.StringVar()
checkbutton1 = tk.Checkbutton(frame2, text="CTS",variable=cts, onvalue='CTS', offvalue='--',pady=1)
checkbutton1.pack(side=tk.LEFT)
checkbutton1.deselect()

gts = tk.StringVar()
checkbutton2 = tk.Checkbutton(frame2, text="GTS",variable=gts, onvalue='GTS', offvalue='--',pady=1)
checkbutton2.pack(side=tk.LEFT)
checkbutton2.deselect()

sts = tk.StringVar()
checkbutton3 = tk.Checkbutton(frame2, text="STS",variable=sts, onvalue='STS', offvalue='--',pady=1)
checkbutton3.pack(side=tk.LEFT)
checkbutton3.deselect()

vts = tk.StringVar()
checkbutton4 = tk.Checkbutton(frame2, text="VTS",variable=vts, onvalue='VTS', offvalue='--',pady=1)
checkbutton4.pack(side=tk.LEFT)
checkbutton4.deselect()

Single_Test = tk.StringVar()
checkbutton_Single_Test = tk.Checkbutton(frame2, text="Enable Single Test",variable=Single_Test, onvalue='Enable Single Test', offvalue='--',pady=1)
checkbutton_Single_Test.pack(side=tk.LEFT)
checkbutton_Single_Test.deselect()

# 將 Checkbutton 水平置中
frame2.pack(side=tk.TOP, fill=tk.X)

# 設定每個 Checkbutton 寬度相等，以便置中
checkbutton1.config(width=9)
checkbutton2.config(width=9)
checkbutton3.config(width=9)
checkbutton4.config(width=9)
checkbutton_Single_Test.config(width=15)




e_path1 = tk.Entry(root, textvariable=var1, width=42)
e_path1.place(x=50, y=180)

b_select1 = tk.Button(root, text='Select CtsTool', command=select_CtsTool, width=10)
b_select1.place(x=320, y=180)

f_path1 = tk.Entry(root, textvariable=var11, width=42)
f_path1.place(x=50, y=210)

c_select1 = tk.Button(root, text='Select CtsImage', command=select_CtsImage, width=10)
c_select1.place(x=320, y=210)

e_path2 = tk.Entry(root, textvariable=var2, width=42)
e_path2.place(x=50, y=240)

b_select2 = tk.Button(root, text='Select GtsTool', command=select_GtsTool, width=10)
b_select2.place(x=320, y=240)

f_path2 = tk.Entry(root, textvariable=var22, width=42)
f_path2.place(x=50, y=270)

c_select2 = tk.Button(root, text='Select GtsImage', command=select_GtsImage, width=10)
c_select2.place(x=320, y=270)

e_path3 = tk.Entry(root, textvariable=var3, width=42)
e_path3.place(x=50, y=300)

b_select3 = tk.Button(root, text='Select StsTool', command=select_StsTool, width=10)
b_select3.place(x=320, y=300)

f_path3 = tk.Entry(root, textvariable=var33, width=42)
f_path3.place(x=50, y=330)

c_select3 = tk.Button(root, text='Select StsImage', command=select_StsImage, width=10)
c_select3.place(x=320, y=330)



frame3 = tk.Frame(root,pady=10)
frame3.pack()
frame3.place(x=20, y=80)

frame4 = tk.Frame(root,pady=10)
frame4.pack()
frame4.place(x=20, y=120)


values_factory=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
values=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
label1 = tk.Label(frame3, text="Retry")
label1.pack()
ch11_var = tk.StringVar()
ch11_var.set(values[0])
ch11 = tk.OptionMenu(frame3, ch11_var, *values)
label1.pack(side=tk.LEFT)
ch11.pack(side=tk.LEFT)


# NotExecutRetry = tk.StringVar()
# checkbutton_NotExecurRetry = tk.Checkbutton(frame4, text="",variable=NotExecutRetry, onvalue='NotExecutRetry', offvalue='--',pady=0)
# checkbutton_NotExecurRetry.pack(side=tk.LEFT)
# checkbutton_NotExecurRetry.deselect()


label11 = tk.Label(frame3, text="NotExecutRetry")
label11.pack()
ch44_var = tk.StringVar()
ch44_var.set(values[0])
ch44 = tk.OptionMenu(frame3, ch44_var, *values)
label11.pack(side=tk.LEFT)
ch44.pack(side=tk.LEFT)

# Reboot_Retry = tk.StringVar()
# checkbutton_Reboot_Retry = tk.Checkbutton(frame3, text="",variable=Reboot_Retry, onvalue='RebootRetry', offvalue='--',pady=1)
# checkbutton_Reboot_Retry.pack(side=tk.LEFT)
# checkbutton_Reboot_Retry.deselect()



label2 = tk.Label(frame3, text="Reboot&Retry")
label2.pack()
ch22_var = tk.StringVar()
ch22_var.set(values[0])
ch22 = tk.OptionMenu(frame3, ch22_var, *values)
label2.pack(side=tk.LEFT)
ch22.pack(side=tk.LEFT)


# factroy_Reset = tk.StringVar()
# checkbutton_factroy_Reset = tk.Checkbutton(frame3, text="",variable=factroy_Reset, onvalue='factroyReset', offvalue='--',pady=1)
# checkbutton_factroy_Reset.pack(side=tk.LEFT)
# checkbutton_factroy_Reset.deselect()

label3 = tk.Label(frame3, text="factroy_Reset")
label3.pack()
ch33_var = tk.StringVar()
ch33_var.set(values_factory[0])
ch44 = tk.OptionMenu(frame3, ch33_var, *values_factory)
label3.pack(side=tk.LEFT)
ch44.pack(side=tk.LEFT)


# bar = ttk.Progressbar(root, mode='determinate',length=380)
# bar.pack(side=tk.LEFT)
# bar.place(x = 50, y = 238)




# 創建一個新的框架用於包含按鈕
button_frame = tk.Frame(root)
button_frame.pack(side=tk.BOTTOM)
# 創建兩個按鈕並添加到新的框架中
button1 = tk.Button(button_frame, text="Start",command=start, width=9)
button1.pack(side=tk.LEFT)

button2 = tk.Button(button_frame, text="Quit",command=close_window, width=9)
button2.pack(side=tk.LEFT)

update_status=check_github_status()
button3 = tk.Button(button_frame, text="Update",command=update_code, width=9)
if update_status=="update":
    button3.pack(side=tk.LEFT)
else:
    button3.pack_forget()

button4 = tk.Button(button_frame, text="check",command=check_github_status, width=9)
# button4.pack(side=tk.LEFT)
button4.pack_forget()


root.mainloop()

