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
CurrPath=os.getcwd()
ParenPath=os.path.dirname(CurrPath)


def initialize(): 
    # parser.add_argument('--s', nargs=3, help="Do stuff with all three arguments.")
    # args = parser.parse_args()
    global path
    # with open(f'/home/{UsrName}/Desktop/IMAGE/workspace/GtsToolPath.txt','r') as f:
    with open(f'{ParenPath}/CtsToolPath.txt','r') as f:
        path = f.read()
    path=path.replace("\\","/")
    # os.chdir(path.replace("\\","/"))
    print("Gts tool path="+path)



# import globalvar
# globalvar.initialize()
# dirpath = globalvar.path