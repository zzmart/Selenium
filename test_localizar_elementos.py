import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.maximize_window()
browser.get("https://www.saucedemo.com/")

username = browser.find_element(By.ID, "user-name")
password = browser.find_element(By.ID, "password")
loginbutton = browser.find_element(By.ID, "login-button")

username.send_keys("standard_user")
password.send_keys("secret_sauce")
time.sleep(2)
#loginbutton.click()  #para apertar um botão click
time.sleep(5)

auth_fields = browser.find_elements(By.XPATH, "//*[@class='input_error form_input']")

print(auth_fields)

print(len(auth_fields))

assert len(auth_fields) == 2, "O numero de elementos é diferente do esperado"

browser.quit()
