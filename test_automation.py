import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 60)
browser.get('https://leogcarvalho.github.io/test-automation-practice/')

dropdown_options = Select(browser.find_element(By.ID, 'dropdown'))
dropdown_options.select_by_visible_text('Option 2')
time.sleep(2)

dropdown_options.select_by_visible_text('Option 3')
time.sleep(2)

dropdown_options.select_by_value('option1')
time.sleep(2)

dropdown_options.select_by_index(2)
time.sleep(2)


browser.find_element(By.XPATH, '/html/body/div/section[4]/label[2]/input').click()
time.sleep(2)
browser.find_element(By.XPATH, '/html/body/div/section[4]/label[4]/input').click()
time.sleep(2)

actions = ActionChains(browser)

browser.find_element(By.ID, 'single-click-btn').click()
time.sleep(2)
doubleClick = browser.find_element(By.ID, 'double-click-btn')
actions.double_click(doubleClick)
time.sleep(2)
rightClick = browser.find_element(By.ID, 'right-click-btn')
actions.context_click(rightClick)
time.sleep(2)
shiftClick = browser.find_element(By.ID, 'shift-click-btn')
actions.key_down(Keys.SHIFT).click(shiftClick).key_up(Keys.SHIFT).perform()
time.sleep(2)

campo_data = browser.find_element(By.XPATH, "//*[@id='date-picker']")
time.sleep(2)
campo_data.send_keys("25-02-2026")
time.sleep(2)

browser.find_element(By.XPATH, '/html/body/div/section[11]/div[1]/button[1]').click()
time.sleep(2)
browser.find_element(By.XPATH, '/html/body/div/section[11]/div[1]/button[2]').click()
time.sleep(2)
browser.find_element(By.XPATH, '/html/body/div/section[11]/div[1]/button[3]').click()
textoJapan = browser.find_element(By.XPATH, '//*[@id="japan-tab"]')
print(textoJapan.text)
time.sleep(2)



browser.quit()
