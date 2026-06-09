import time

from selenium import webdriver
from selenium.webdriver.common import alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 30)
browser.get('https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver')

browser.find_element(By.ID, 'alert').click()
wait.until(EC.alert_is_present())
time.sleep(2)

alerta = browser.switch_to.alert
print(alerta.text)
alerta.accept()
time.sleep(2)


browser.find_element(By.ID, 'populate-text').click()
wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="h2"]'), "Selenium Webdriver"))

target_text = browser.find_element(By.XPATH, '//*[@id="h2"]').text
assert target_text == "Selenium Webdriver"

browser.find_element(By.ID, 'display-other-button').click()
wait.until(EC.element_to_be_clickable((By.ID, "hidden")))
time.sleep(2)

browser.find_element(By.ID, 'enable-button').click()
wait.until(EC.element_to_be_clickable((By.ID, "disable")))
time.sleep(2)


browser.find_element(By.ID, 'checkbox').click()
wait.until(EC.element_to_be_selected(browser.find_element(By.ID, 'ch')))
time.sleep(2)

browser.quit()