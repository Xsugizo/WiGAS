# -*- coding: utf-8 -*-
import os
import subprocess

UsrName = subprocess.check_output('whoami')
UsrName = UsrName.decode().strip()

def Process():
    dirpath = f'/home/{UsrName}/Desktop/IMAGE/'
    for root,dirs,files in os.walk(dirpath):
        for dir in dirs:
            if dir.find("Pipeline_Testing_Cts")!=-1:
                print(os.path.join(root,dir))
                dirpath = os.path.join(root,dir)
                os.chdir(dirpath)
                os.system('./jen.sh')
                
            if dir.find("Pipeline_Testing_Gts")!=-1:
                print(os.path.join(root,dir))
                dirpath = os.path.join(root,dir)
                os.chdir(dirpath)
                os.system('./jen.sh')
            if dir.find("Pipeline_Testing_Sts")!=-1:
                print(os.path.join(root,dir))
                dirpath = os.path.join(root,dir)
                os.chdir(dirpath)
                os.system('./jen.sh')


