import time
from idlelib.autocomplete import TRY_A

from selenium import webdriver
from selenium.webdriver.common.by import By

viewports =[(1024,768),(768,1024),(375,667),(414,896)] #array of lists for sizes which are width and height


driver= webdriver.Chrome()
driver.get("https://www.google.com/")
time.sleep(2)

# to set a window size
#using a loop to test with all the numbers from above

try:
    for width, height in viewports:
        driver.set_window_size(width, height)
        time.sleep(5)
finally:
    driver.close()
