#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: ying
"""

import requests

# The selenium module
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# The Beautiful Soup module
from bs4 import BeautifulSoup

import time

# Start the WebDriver and load the page
timeout = 60
url = 'https://www.solarweb.com/PvSystems/PvSystem?pvSystemId=712bb5f3-b4f6-4d2d-9c57-8b7e7c5d2f06'

page = requests.get(url,timeout=60)
print page.content
driver = webdriver.Chrome()
driver.get(url, timeout=60)

# Scrape data in every 10 minutes
while True:
    WebDriverWait(driver).until(EC.visibility_of_element_located((By.ID, "the-element-id")))
    page = driver.page_source
    soup = BeautifulSoup(page, 'lxml')
    divs = soup.find_all('div', class_='live-plot-header')
    for div in divs:
# Add error handling
        try:            
            name = div.title.text
            kwh = div.find('div', class_='pull-left').text
            print(name + kwh)
        except AttributeError:
            continue
        else:
            break
    
    time.sleep(600)



#Importing Unit Test Case
import unittest
from django.test import Client
newcl = Client()
testerreq = c.get('/PvSystems/PvSystem?pvSystemId=712bb5f3-b4f6-4d2d-9c57-8b7e7c5d2f06')
if tester.status_code == 200:
  self.assertEqual(page, testerreq.content)
else:
  self.fail("The server did not successfully answer to the http request")
  
driver.quit()
