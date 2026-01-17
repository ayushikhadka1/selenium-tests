from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver= webdriver.Chrome()

driver.get("https://doggedit.ai/")

time.sleep(3)
driver.maximize_window()

#print(driver.title)
#verifying

actual_title= driver.title
expected_title = "DoggedIt - Live Streaming Reimagined"

if actual_title == expected_title:
    print("the test is pass")
else:
    print("the test is fail")

print(driver.current_url)


#driver.find_element(By.LINK_TEXT,"Download Now").click()
#time.sleep(3)

#original_tab = driver.current_window_handle
#driver.switch_to.window("original_tab")
#time.sleep(10)


driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/a[1]").click()
time.sleep(2)

driver.find_element(By.XPATH,"/html/body/nav/div/div[2]/a[2]").click()
time.sleep(2)

driver.find_element(By.XPATH,"/html/body/nav/div/div[2]/a[3]").click()
time.sleep(2)

driver.find_element(By.XPATH,"/html/body/nav/div/div[2]/a[4]").click()
time.sleep(2)


driver.find_element(By.XPATH,"/html/body/nav/div/div[1]/a/span").click()
time.sleep(3)

driver.find_element(By.LINK_TEXT,"Download Now").click()
time.sleep(3)



