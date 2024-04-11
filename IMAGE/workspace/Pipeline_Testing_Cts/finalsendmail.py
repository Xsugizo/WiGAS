#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import subprocess
import os
import chardet

import globalvar
globalvar.initialize()
dirpath = globalvar.path


# email title add retry_num  retry_num reboot_num notexecuteset_num
UsrName = subprocess.check_output('whoami')
UsrName = UsrName.decode().strip()

runfre = []
with open(f'/home/{UsrName}/Desktop/IMAGE/workspace/runfre.txt') as file:
    for line in file.readlines():
        runfre.append(int(line))
file.close()
retry_num=runfre[0]
reboot_num=runfre[1]
reset_num=runfre[2]
notexecuteset_num=runfre[3]
subjectcontent='WiGAS Final Report with retry_num='+retry_num+' reboot_num='+reboot_num+' notexecuteset_num='+ notexecuteset_num


# 設置SMTP伺服器地址和端口號
smtp_server = 'smtp.office365.com'
smtp_port = 587

# 設置發件人、收件人、主題
from_addr = 'Ian_H_Chang@wistron.com'
to_addr = ['Ian_H_Chang@wistron.com','Jonathan_Tung@wistron.com','Jany_Chen@wistron.com','Vicky_Chen@wistron.com']
subject = 'WiGAS Final Report'

# 創建MIMEMultipart對象，並設置發件人、收件人、主題
msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = ','.join(to_addr)
msg['Subject'] = subject

with open(f'{dirpath}/android-cts/output.html', 'rb') as f:
    html = f.read()
    result = chardet.detect(html)
    encoding = result['encoding']
    print(encoding)

# 讀取HTML文件
with open(f'{dirpath}/android-cts/output.html', 'r',encoding=encoding) as f:
    html = f.read()

# 將HTML文件轉換為MIMEText對象，並添加到MIMEMultipart對象中
html_part = MIMEText(html, 'html')
msg.attach(html_part)


# 登錄SMTP服務器
smtp_username = 'Ian_H_Chang@wistron.com'
smtp_password = 'Bk2Xt6jb333!'
smtp_obj = smtplib.SMTP(smtp_server, smtp_port)
smtp_obj.starttls()
smtp_obj.login(smtp_username, smtp_password)

# 發送郵件
smtp_obj.sendmail(from_addr, to_addr, msg.as_string())

# 關閉SMTP對象
smtp_obj.quit()
