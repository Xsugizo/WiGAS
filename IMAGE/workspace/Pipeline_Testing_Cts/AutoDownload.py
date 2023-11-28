import os
print('Update/Upgrade')
os.system('sudo apt-get update')
os.system('sudo apt-get upgrade')

print('Download python3.9')
os.system('sudo apt install software-properties-common')
os.system('sudo add-apt-repository ppa:deadsnakes/ppa')
os.system('sudo apt-get install python3.9')
os.system('sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 1')

print('Download pip3')
os.system('curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py')
os.system('python3.9 get-pip.py')

print('Download setuptools')
os.system('pip3 install --upgrade pip setuptools')

print('Download UI2')
os.system('pip3 install --no-cache-dir uiautomator2')

print('Download GUI')
os.system('pip3 install --force-reinstall pyautogui')

print('Download tkinter')
os.system('sudo apt install python3.9-tk')

os.system('python3.9 -m pip install beautifulsoup4')
os.system('python3.9 -m pip install chardet')
os.system('python3.9 -m pip install pandas')

print('All download done')