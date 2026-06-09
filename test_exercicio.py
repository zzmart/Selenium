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
loginbutton.click()
time.sleep(5)
addtocartsaucelabsbackpack = browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

shopping_cart_link = browser.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a").click()

checkout = browser.find_element(By.ID, "checkout").click()
time.sleep(5)

firstname = browser.find_element(By.ID, "first-name")
firstname.send_keys("Gabs")
lastname = browser.find_element(By.ID, "last-name")
lastname.send_keys("Luis")
postalcode = browser.find_element(By.ID, "postal-code")
postalcode.send_keys("12345")
time.sleep(5)
continuee = browser.find_element(By.ID, "continue").click()

checkout_summary_container = browser.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[8]").click() #mostra total
print(checkout_summary_container)

finish = browser.find_element(By.ID, "finish").click()


browser.quit()