from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.facebook.com')



email = driver.find_element(By.XPATH, '//*[@id="email"]') # email kiritish joyini topish
email.send_keys('blah@gmail.com') # email kiritish joyiga email kiritish

password = driver.find_element(By.XPATH, '//*[@id="pass"]') # password kiritish joyini topish
password.send_keys('blah12121') # password kiritish joyiga password kiritish

time.sleep(2) # login va password kiritilganligini ko'rish uchun kodimizni 2 sekundga to'xtatib turish

loginbtn = driver.find_element(By.NAME, 'login') # login tugmasini topish
loginbtn.click() # email va password kiritilgandan keyin ularni jo'natish uchun login tugmasini bosish

time.sleep(10) # natijani ko'rish uchun kodimizni 10 sekundga to'xtatib turish
driver.close()