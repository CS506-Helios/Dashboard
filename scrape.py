#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 15:04:15 2017

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

driver.quit()
