import time

from selenium import webdriver


browser = webdriver.Chrome()

browser.maximize_window()

browser.get("https://www.google.com")
# time.sleep(5) fecha o codigo depois de um tempo

#atualizar pagina
browser.refresh()

time.sleep(2)

browser.get("https://www.saucedemo.com")
time.sleep(2)

browser.back()
time.sleep(2)

browser.forward()
time.sleep(2)

browser.switch_to.new_window("tab")
browser.switch_to.new_window("tab")
time.sleep(2)

#fecha janela ativa
browser.close()



# para finalizar codigo
browser.quit()