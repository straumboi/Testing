#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 0 9:35:39 2020
@author: sbhargava
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.theice.com/marketdata/reports/114")
driver.get("https://www.google.com")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("https://www.theice.com/marketdata/reports/114")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()

