
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

usernameStr = 'username'
passwordStr = 'password'


driver = webdriver.Chrome()
driver.get(('https://coursehunters.online/'))

driver.implicitly_wait(10)

signInButton = driver.find_element_by_xpath('//*[@id="ember6"]/header/div/div/div[2]/span/button[2]')
signInButton.click()

driver.implicitly_wait(5)

# fill in username and hit the next button
username = driver.find_element_by_id("login-account-name")
username.send_keys(usernameStr)

password = driver.find_element_by_id("login-account-password")
password.send_keys(passwordStr)

#driver.find_element_by_class_name("EdgeButtom--medium").click()
#driver.implicitly_wait(10)

logInButton = driver.find_element_by_xpath('/html/body/section/div/div[3]/div/div/div/div[3]/div[2]/button[1]')
logInButton.click()



