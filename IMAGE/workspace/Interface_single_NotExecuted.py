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
from tkinter import messagebox

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
        if Retry.get()!='--':
            f.write('retry/')
        if NotExecutRetry.get()!='--':
            f.write('notexecutreset')
        if Reboot_Retry.get()!='--':
            f.write('reboot/')
        if factroy_Reset.get()!='--':
            f.write('factoryreset')
        

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
    tk.messagebox.askokcancel(title=None, message="請確認retry, reboot factoryRest and Not Executed 次數是否正確 retry_num="+retry_num+" reboot_num="+reboot_num+" reset_num="+reset_num+" notexecuteset_num="+notexecuteset_num)
    
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
                    os.system('./jen_single.sh')
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


def close_window():
    root.destroy()

root = tk.Tk()
root.title("WiGAS")
root.resizable(False, False)
root.geometry('500x400')
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
label = tk.Label(frame, text="GMS Auto Test w/ Single Test", font = ('Bahnschrift',20,'bold'),pady=10)
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

# 將 Checkbutton 水平置中
frame2.pack(side=tk.TOP, fill=tk.X)

# 設定每個 Checkbutton 寬度相等，以便置中
checkbutton1.config(width=12)
checkbutton2.config(width=12)
checkbutton3.config(width=12)
checkbutton4.config(width=12)



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

Retry = tk.StringVar()
checkbutton_Retry = tk.Checkbutton(frame3, text="",variable=Retry, onvalue='Retry', offvalue='--',pady=0)
checkbutton_Retry.pack(side=tk.LEFT)
checkbutton_Retry.deselect()


values_factory=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
values=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
label1 = tk.Label(frame3, text="Retry")
label1.pack()
ch11_var = tk.StringVar()
ch11_var.set(values[0])
ch11 = tk.OptionMenu(frame3, ch11_var, *values)
label1.pack(side=tk.LEFT)
ch11.pack(side=tk.LEFT)


NotExecutRetry = tk.StringVar()
checkbutton_NotExecurRetry = tk.Checkbutton(frame4, text="",variable=NotExecutRetry, onvalue='NotExecutRetry', offvalue='--',pady=0)
checkbutton_NotExecurRetry.pack(side=tk.LEFT)
checkbutton_NotExecurRetry.deselect()


label11 = tk.Label(frame4, text="NotExecutRetry")
label11.pack()
ch44_var = tk.StringVar()
ch44_var.set(values[0])
ch44 = tk.OptionMenu(frame4, ch44_var, *values)
label11.pack(side=tk.LEFT)
ch44.pack(side=tk.LEFT)

Reboot_Retry = tk.StringVar()
checkbutton_Reboot_Retry = tk.Checkbutton(frame3, text="",variable=Reboot_Retry, onvalue='RebootRetry', offvalue='--',pady=1)
checkbutton_Reboot_Retry.pack(side=tk.LEFT)
checkbutton_Reboot_Retry.deselect()



label2 = tk.Label(frame3, text="Reboot&Retry")
label2.pack()
ch22_var = tk.StringVar()
ch22_var.set(values[0])
ch22 = tk.OptionMenu(frame3, ch22_var, *values)
label2.pack(side=tk.LEFT)
ch22.pack(side=tk.LEFT)


factroy_Reset = tk.StringVar()
checkbutton_factroy_Reset = tk.Checkbutton(frame3, text="",variable=factroy_Reset, onvalue='factroyReset', offvalue='--',pady=1)
checkbutton_factroy_Reset.pack(side=tk.LEFT)
checkbutton_factroy_Reset.deselect()

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

root.mainloop()

