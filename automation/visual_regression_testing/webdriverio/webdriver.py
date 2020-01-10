from selenium import webdriver
import time
# import argparse
from tkinter import *

driver = webdriver.Chrome()
driver.get('https://sandhillglobaladvisors.com')
time.sleep(2)
driver.save_screenshot('test1.png')
driver.get_screenshot_as_png()
driver.execute_script('window.scrollBy(0, 500)')
time.sleep(2)
driver.save_screenshot('test2.png')
driver.get_screenshot_as_png()

# Function that takes a picture of the two websites

# Function that compares the two images (pixel by pixel comparison)

# Graphical Interface
