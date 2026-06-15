#Fluxo E2E 2 — Compra com login antes do checkout
#Fluxo E2E 9 — Compra com quantidades diferentes
#Fluxo E2E 11 — Conta de usuário

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

#registrar usuario
browser.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a').click()
textoNewUser = browser.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/h2').text
assert "New User Signup!" == textoNewUser

name = browser.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/input[2]')
name.send_keys("jose")
email = browser.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/input[3]')
email.send_keys("12234@ifrs.com")
time.sleep(2)
browser.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/button').click()

textoConfirma = browser.find_element(By.XPATH, '//*[@id="form"]/div/div/div/div[1]/h2/b').text
assert 'ENTER ACCOUNT INFORMATION' == textoConfirma

browser.find_element(By.ID, 'id_gender1').click()

browser.find_element(By.ID, 'password').send_keys("1234")

dropdown_day = Select(browser.find_element(By.ID, 'days'))
dropdown_day.select_by_visible_text('12')

dropdown_month = Select(browser.find_element(By.ID, 'months'))
dropdown_month.select_by_visible_text('July')

dropdown_day = Select(browser.find_element(By.ID, 'years'))
dropdown_day.select_by_visible_text('1999')

browser.find_element(By.ID, 'newsletter').click()

browser.find_element(By.ID, 'optin').click()

browser.find_element(By.ID, 'first_name').send_keys("jose")
browser.find_element(By.ID, 'last_name').send_keys("silva")
browser.find_element(By.ID, 'company').send_keys("qualquer")
browser.find_element(By.ID, 'address1').send_keys("Street address, P.O. Box, Company name")
dropdown_country = Select(browser.find_element(By.ID, 'country'))
dropdown_country.select_by_visible_text('India')
browser.find_element(By.ID, 'state').send_keys("qualquer")
browser.find_element(By.ID, 'city').send_keys("qualquer")
browser.find_element(By.ID, 'zipcode').send_keys("41234234")
browser.find_element(By.ID, 'mobile_number').send_keys("000000000")
time.sleep(2)
browser.find_element(By.XPATH, '//*[@id="form"]/div/div/div/div[1]/form/button').click()

textoCadastrado = browser.find_element(By.XPATH, '//*[@id="form"]/div/div/div/h2/b').text
assert 'ACCOUNT CREATED!' == textoCadastrado
time.sleep(2)
browser.find_element(By.XPATH, '//*[@id="form"]/div/div/div/div/a').click()

textolegged = browser.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[10]/a').text
assert 'Logged in as jose' == textolegged
time.sleep(2)
browser.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[5]/a').click()
textoDeletado = browser.find_element(By.XPATH, '//*[@id="form"]/div/div/div/h2/b').text
assert 'Account Deleted!' == textoDeletado
time.sleep(2)
browser.find_element(By.XPATH, '//*[@id="form"]/div/div/div/div/a').click()
time.sleep(2)