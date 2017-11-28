#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 14:46:53 2017

@author: ying
"""
import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import WebDriverWait

# get path of phantomjs
dir = os.path.dirname(__file__)
executable_path=dir + '/phantomjs-2.1.1-macosx/bin/phantomjs'

# create a new session
driver = webdriver.PhantomJS(executable_path)
driver.implicitly_wait(15)
driver.maximize_window()

# navigate to the sunpower login page
url="https://sunpowermonitor.com/partner/partner.aspx#"
driver.get(url)
driver.implicitly_wait(15)

# sign in to the account 
username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")

username.send_keys("beihoff@wisc.edu")
password.send_keys("sunpower1")

login = driver.find_element_by_name("signin")
login.submit()

driver.implicitly_wait(15)
#print driver.current_url
#driver.close()

# click the address to open up the energy production page
menu = driver.find_element_by_css_selector(".nav")
address = driver.find_element_by_css_selector(".nav #submenu1")
ActionChains(driver).move_to_element(menu).click(address).perform()

driver.implicitly_wait(15)

# download the csv file
system = driver.find_element_by_name("select components or system")
ActionChains(driver).context_click(system)
cumulative = driver.find_element_by_name("select parameter")
ActionChains(driver).context_click(cumulative)

graph = driver.find_element_by_name("graph now")
graph.click()

download = driver.find_element_by_name("download")
download.click()



