import time
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

browser = webdriver.Chrome()
browser.implicitly_wait(12)

browser.maximize_window()
browser.get("https://automationexercise.com/")
wait = WebDriverWait(browser, 30)

browser.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a').click()
textologin = browser.find_element(By.XPATH, '//*[@id="form"]/div/div/div[1]/div/h2').text
assert "Login to your account" == textologin

email = browser.find_element(By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/input[2]')
email.send_keys("12234@ifrs.com")
browser.find_element(By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/input[3]').send_keys("1234")

browser.find_element(By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/button').click()

textolegged = browser.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[10]/a').text
assert 'Logged in as jose' == textolegged

browser.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a').click()

textologin2 = browser.find_element(By.XPATH, '//*[@id="form"]/div/div/div[1]/div/h2').text
assert "Login to your account" == textologin2