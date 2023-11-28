#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

from selenium import webdriver
#from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

chrome_options=Options()

chrome_options.add_argument('--headless')
#chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')


browser = webdriver.Chrome()
browser.maximize_window()
browser.implicitly_wait(5)
browser.get('http://192.168.50.7:8080')
#print(browser.title)

time.sleep(2)

#username = browser.find_element_by_name('j_username')
username = browser.find_element(By.NAME, 'j_username')
username.send_keys('DXOUser')
#password = browser.find_element_by_name('j_password')
password = browser.find_element(By.NAME, 'j_password')
password.send_keys('dxo55555')

time.sleep(2)

#button = browser.find_element_by_class_name('submit-button.primary.')
button = browser.find_element(By.CLASS_NAME, 'submit-button.primary')
button.click()

time.sleep(2)

#button = browser.find_element(By.ID, "job_Pipeline_Testing")
#button.click()

browser.get('http://192.168.50.7:8080/job/send email/')

run = browser.find_element(By.LINK_TEXT, 'Build Now')
run.click()