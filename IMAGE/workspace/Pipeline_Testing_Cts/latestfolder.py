#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

import os
from pyexpat import features
import shutil
import bs4
import io
import globalvar
globalvar.initialize()
dirpath = globalvar.path
# catch latest test result report

directory = dirpath+'/android-cts/results'
# directory = '/media/logo007/1TBHD/IMAGE/workspace/Pipeline_Testing/11_r10/android-cts-11_r10-linux_x86-arm/android-cts/results'
latest=sorted([os.path.join(directory,d) for d in os.listdir(directory)],key=os.path.getmtime)
latest.remove(dirpath+'/android-cts/results/latest')
latest.remove(dirpath+"/android-cts/results/temp")
# latest.remove('/media/logo007/1TBHD/IMAGE/workspace/Pipeline_Testing/11_r10/android-cts-11_r10-linux_x86-arm/android-cts/results/latest')
# latest.remove("/media/logo007/1TBHD/IMAGE/workspace/Pipeline_Testing/11_r10/android-cts-11_r10-linux_x86-arm/android-cts/results/temp")
print(latest[-1])
shutil.copyfile(latest[-1]+'/test_result_failures_suite.html',dirpath+'/android-cts/latest_test_result.html')
shutil.copyfile(latest[-1]+'/compatibility_result.css',dirpath+'/android-cts/compatibility_result.css')
# shutil.copyfile(latest[-1]+'/test_result_failures_suite.html','/media/logo007/1TBHD/IMAGE/workspace/Pipeline_Testing/11_r10/android-cts-11_r10-linux_x86-arm/android-cts/latest_test_result.html')
# shutil.copyfile(latest[-1]+'/compatibility_result.css','/media/logo007/1TBHD/IMAGE/workspace/Pipeline_Testing/11_r10/android-cts-11_r10-linux_x86-arm/android-cts/compatibility_result.css')


#generate inline css
with open(dirpath+"/android-cts/latest_test_result.html",encoding='UTF-8') as inf:
# with open("/media/logo007/1TBHD/IMAGE/workspace/Pipeline_Testing/11_r10/android-cts-11_r10-linux_x86-arm/android-cts/latest_test_result.html",encoding='UTF-8') as inf:
    txt = inf.read()
    soup = bs4.BeautifulSoup(txt,'html.parser')

new_link = soup.new_tag("link", rel="stylesheet", href=dirpath+"/android-cts/compatibility_result.css")
# new_link = soup.new_tag("link", rel="stylesheet", href="/media/logo007/1TBHD/IMAGE/workspace/Pipeline_Testing/11_r10/android-cts-11_r10-linux_x86-arm/android-cts/compatibility_result.css")
soup.head.append(new_link)

with open(dirpath+"/android-cts/latest_test_result.html", "w",encoding='UTF-8') as outf:
# with open("/media/logo007/1TBHD/IMAGE/workspace/Pipeline_Testing/11_r10/android-cts-11_r10-linux_x86-arm/android-cts/latest_test_result.html", "w",encoding='UTF-8') as outf:
    outf.write(str(soup))

soup = bs4.BeautifulSoup(open(dirpath+"/android-cts/latest_test_result.html",encoding='UTF-8').read())
# soup = bs4.BeautifulSoup(open("/media/logo007/1TBHD/IMAGE/workspace/Pipeline_Testing/11_r10/android-cts-11_r10-linux_x86-arm/android-cts/latest_test_result.html",encoding='UTF-8').read())
stylesheets = soup.findAll("link", {"rel": "stylesheet"})
for s in stylesheets:
    t = soup.new_tag('style')
    c = bs4.element.NavigableString(open(s["href"]).read())
    t.insert(0,c)
    t['type'] = 'text/css'
    s.replaceWith(t)
open(dirpath+"/android-cts/output.html", "w",encoding='UTF-8').write(str(soup))
# open("/media/logo007/1TBHD/IMAGE/workspace/Pipeline_Testing/11_r10/android-cts-11_r10-linux_x86-arm/android-cts/output.html", "w",encoding='UTF-8').write(str(soup))

