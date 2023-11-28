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

parser = argparse.ArgumentParser() 
# parser.add_argument('--name', type=str, default="") 

# args = parser.parse_args() 

# i= args.name 

parser.add_argument('--s', nargs=3, help="Do stuff with all three arguments.")
  # https://docs.python.org/3/library/argparse.html#nargs
args = parser.parse_args()

# if args.s:
#     print(len(args.s), "arguments:")
#     print(args.s) # will contain a list
#     print(args.s[0])

i=args.s[0]+" "+args.s[1]+" "+args.s[2]


print("i="+i)

os.chdir("/home/logo113/Desktop/IMAGE/TC53/athena_A13_user_GMS_RelKey_2023-05-30-1722_main_SE/Images")
# os.system ('cd /home/logo007/Desktop/IMAGE/TC53/athena_A13_user_GMS_RelKey_2023-03-16-0632_wave1_SE/Images && ls')
os.system ('pwd')
# print ("install_Athena_1vN.sh "+i)
# os.system ("gnome-terminal -- 'ls'")
# os.system ('gnome-terminal -- ./install_Athena_1vN.sh ' + i)
os.system (f"gnome-terminal -- bash -c './install_Athena_1vN.sh {i} >> {args.s[0]}.txt'")


