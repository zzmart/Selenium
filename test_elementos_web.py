import time
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.implicitly_wait(12)

browser.maximize_window()
browser.get("https://leogcarvalho.github.io/test-automation-practice/")
wait = WebDriverWait(browser, 30)

# ********
# Login Form and button click
# ********
username = browser.find_element(By.ID,"username")
password = browser.find_element(By.ID,"password")
username.send_keys("admin")
password.send_keys("1234")
botaoLog = browser.find_element(By.ID,"login-button")
botaoLog.click()
time.sleep(3)

# ==========================
# Modal Window
# ==========================

browser.find_element(By.ID,'open-modal').click()
modal = WebDriverWait(browser, 10).until( #espera o modal estar aparecendo na tela
    EC.visibility_of_element_located((By.ID, "modal"))
)
assert modal.is_displayed()#verifica se o modal realmente esta sendo mostrado

texto = browser.find_element(By.CSS_SELECTOR,"#modal .modal-content p").text
print(texto) #print no modal (pega o texto dele)


browser.find_element(By.ID, "close-modal").click() #fecha modal

# ********
# File upload
# ********
arquivo = r"C:\Users\aluno\Documents\Selenium Martina\testeUpload.txt"
upload = browser.find_element(By.ID, "file-upload")
upload.send_keys(arquivo)
assert "testeUpload.txt" in upload.get_attribute("value")

# ********
# Drag and drop
# ********
origem = browser.find_element(By.ID, "drag-source")
destino = browser.find_element(By.ID, "drop-target")
ActionChains(browser).drag_and_drop(origem, destino).perform() #ação segura e larga a partir dos parametros origem e destino
time.sleep(3)

# equivalente
ActionChains(browser).click_and_hold(origem).move_to_element(destino).release().perform()
time.sleep(5)


time.sleep(3)
browser.quit()

