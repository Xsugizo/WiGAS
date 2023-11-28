#! /usr/bin/env python

import os
os.system('adb devices |  tail -n +2 |  cut -sf 1 |  xargs -IX adb -s X reboot')