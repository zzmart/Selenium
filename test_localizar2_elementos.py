import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.maximize_window()
browser.get("https://demo.applitools.com/")

username = browser.find_element(By.ID, "username")
checkbox = browser.find_element(By.XPATH, "//*[@type='checkbox']")

print(username.is_displayed())
assert username.is_displayed()

print(username.is_enabled())
assert username.is_enabled()

print(checkbox.is_selected())
assert not checkbox.is_selected()

checkbox.click()

print(checkbox.is_selected())
assert checkbox.is_selected()
