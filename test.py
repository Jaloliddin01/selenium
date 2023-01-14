from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get('https://www.techwithtim.net/')

print(driver.title)

sr = driver.find_element(By.NAME, 's')
sr.send_keys('test')
sr.send_keys(Keys.RETURN)

time.sleep(5)

driver.quit()
