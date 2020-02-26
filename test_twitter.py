
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

usernameStr = '8951247621'
passwordStr = 'a1b9h9i7'


driver = webdriver.Chrome()
driver.get(('https://twitter.com/login'))

driver.implicitly_wait(20)

# fill in username and hit the next button
username = driver.find_element_by_name("session[username_or_email]")
username.send_keys(usernameStr)

password = driver.find_element_by_name("session[password]")
password.send_keys(passwordStr)

#driver.find_element_by_class_name("EdgeButtom--medium").click()
driver.implicitly_wait(10)

signInButton = driver.find_element_by_xpath('/html/body/div/div/div/div/main/div/div/form/div/div[3]/div')
signInButton.submit()


