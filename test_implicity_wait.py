
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.implicitly_wait(10) # para carregar a pagina

browser.get('https://the-internet.herokuapp.com/dynamic_loading/2')
button = browser.find_element(By.XPATH, "//*[@id='start']/button").click()

text = browser.find_element(By.XPATH, "//*[@id='finish']/h4").text

print(text)

browser.quit()