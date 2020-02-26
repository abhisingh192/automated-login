from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

usernameStr = 'abhineetsingh192@gmail.com'
passwordStr = 'a1b9h9i7'


driver = webdriver.Chrome()
driver.get(('https://github.com/login'))

# fill in username and hit the next button
username = driver.find_element_by_id("login_field")
username.send_keys(usernameStr)

password = driver.find_element_by_id("password")
password.send_keys(passwordStr)
 
signInButton = driver.find_element_by_name('commit')
signInButton.submit()
