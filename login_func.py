import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from test import expected_title

driver= webdriver.Chrome()

driver.get("https://www.saucedemo.com/")
driver.maximize_window()

driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")

click_button= driver.find_element(By.ID,"login-button")
# verify the button is not disabled
assert click_button.is_enabled()
click_button.click()

act_title= driver.title
exp_title = "Swag Labs"

if act_title==exp_title:
    print("the test is pass")
else:
    print("the test is fail")

print(driver.current_url)

capture_name = driver.find_element(By.XPATH,"//*[@id='header_container']/div[2]/span")
print(capture_name.text)





time.sleep(2)