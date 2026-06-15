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

browser.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[2]/a').click()
