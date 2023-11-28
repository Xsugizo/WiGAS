#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import re
import sys
import os
import time
import subprocess
from subprocess import call
import argparse 
UsrName = subprocess.check_output('whoami')
UsrName = UsrName.decode().strip()
parser = argparse.ArgumentParser() 
# parser.add_argument('--name', type=str, default="") 

# args = parser.parse_args() 

# i= args.name 
parser.add_argument('--s', nargs=3, help="Do stuff with all three arguments.")
  # https://docs.python.org/3/library/argparse.html#nargs
args = parser.parse_args()
with open(f'/home/{UsrName}/Desktop/IMAGE/workspace/CtsImagePath.txt','r') as f:
    CtsImagePath = f.read()

# if args.s:
#     print(len(args.s), "arguments:")
#     print(args.s) # will contain a list
#     print(args.s[0])

i=args.s[0]+" "+args.s[1]+" "+args.s[2]
# i=args.s[0]


print("i="+i)
print("CtsImagePath="+CtsImagePath.replace("\\","/"))
os.chdir(CtsImagePath.replace("\\","/"))
# os.chdir(f"/home/{UsrName}/Desktop/IMAGE/TC53/helios_Android13_user_GMS_Rel_Key_release_2023-06-20-1804__SE")
# os.chdir(CtsImagePath)
# os.chdir(f"/home/{UsrName}/Desktop/IMAGE/TC53/athena_A13_userdebug_GMS_RelKey_2023-05-30-1716_main_SE/Images")


# os.system ('cd /home/logo007/Desktop/IMAGE/TC53/athena_A13_user_GMS_RelKey_2023-03-16-0632_wave1_SE/Images && ls')
os.system ('pwd')
print ("install_Athena_1vN.sh "+i+" -f "+args.s[0]+".txt")
# os.system ("gnome-terminal -- 'ls'")
# os.system ('gnome-terminal -- ./install_Athena_1vN.sh ' + i +' >> '+args.s[0]+'.txt 2>&1')Install_Helios_Linux_WLAN_ONLY_1vN
# os.system (f"gnome-terminal -- bash -c './install_Athena_1vN.sh {i} >> {args.s[0]}.txt'")
# os.system (f"gnome-terminal -- bash -c './Install_Helios_Linux_1VN.sh {i} >> {args.s[0]}.txt'")
# os.system (f"gnome-terminal -- bash -c './Install_Helios_Linux_WLAN_ONLY_1vN.sh {i} >> {args.s[0]}.txt'")
os.system ('gnome-terminal -- ./install_Athena_1vN.sh ' + i)






