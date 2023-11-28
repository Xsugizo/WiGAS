 
 #! /usr/bin/env python
import time
import os
import csv
import re
import sys
import subprocess
import array
 

 
output = os.popen('./cts-tradefed l r').read()
file = open("test_file.csv","w")
file.write(output)
file.close()