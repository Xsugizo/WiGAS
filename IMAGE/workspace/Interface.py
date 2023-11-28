# -*- coding: utf-8 -*-
import os
import tkinter as tk
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


    with open('runfre.txt','w')as f:       
        f.write(str(ch11_var.get())+'\n')
        f.write(str(ch22_var.get())+'\n')
        f.write(str(ch33_var.get()))
        f.close

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
                    os.system('./jen.sh')
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
label = tk.Label(frame, text="GMS Auto Test", font = ('Bahnschrift',20,'bold'),pady=10)
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
e_path1.place(x=50, y=130)

b_select1 = tk.Button(root, text='Select CtsTool', command=select_CtsTool, width=10)
b_select1.place(x=320, y=130)

f_path1 = tk.Entry(root, textvariable=var11, width=42)
f_path1.place(x=50, y=165)

c_select1 = tk.Button(root, text='Select CtsImage', command=select_CtsImage, width=10)
c_select1.place(x=320, y=165)




e_path2 = tk.Entry(root, textvariable=var2, width=42)
e_path2.place(x=50, y=200)

b_select2 = tk.Button(root, text='Select GtsTool', command=select_GtsTool, width=10)
b_select2.place(x=320, y=200)

f_path2 = tk.Entry(root, textvariable=var22, width=42)
f_path2.place(x=50, y=235)

c_select2 = tk.Button(root, text='Select GtsImage', command=select_GtsImage, width=10)
c_select2.place(x=320, y=235)

e_path3 = tk.Entry(root, textvariable=var3, width=42)
e_path3.place(x=50, y=270)

b_select3 = tk.Button(root, text='Select StsTool', command=select_StsTool, width=10)
b_select3.place(x=320, y=270)

f_path3 = tk.Entry(root, textvariable=var33, width=42)
f_path3.place(x=50, y=305)

c_select3 = tk.Button(root, text='Select StsImage', command=select_StsImage, width=10)
c_select3.place(x=320, y=305)

frame3 = tk.Frame(root,pady=10)
frame3.pack()
frame3.place(x=50, y=80)
values_factory=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
values=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
label1 = tk.Label(frame3, text="Retry")
label1.pack()
ch11_var = tk.StringVar()
ch11_var.set(values[0])
ch11 = tk.OptionMenu(frame3, ch11_var, *values)
label1.pack(side=tk.LEFT)
ch11.pack(side=tk.LEFT)

label2 = tk.Label(frame3, text="    Reboot&Retry")
label2.pack()
ch22_var = tk.StringVar()
ch22_var.set(values[0])
ch22 = tk.OptionMenu(frame3, ch22_var, *values)
label2.pack(side=tk.LEFT)
ch22.pack(side=tk.LEFT)

label3 = tk.Label(frame3, text="    factroy_Reset")
label3.pack()
ch33_var = tk.StringVar()
ch33_var.set(values_factory[1])
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

