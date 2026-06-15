from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()

browser.maximize_window()
browser.get("https://the-internet.herokuapp.com/tables")
wait = WebDriverWait(browser, 10)


# percorrer linhas
tabela = browser.find_element(By.ID, "table1")
linhas = tabela.find_elements(By.TAG_NAME, "tr")
print("Percorrendo linhas:")
for linha in linhas:
    print(linha.text)
print("========================================")

# percorrer linhas/colunas
tabela2 = browser.find_element(By.ID, "table1")
tbody = tabela2.find_element(By.TAG_NAME, "tbody")
linhas2 = tbody.find_elements(By.TAG_NAME, "tr")

# ou assim
#linhas2 = browser.find_elements(By.XPATH,"//table[@id='table1']/tbody/tr")

print("Percorrendo linhas e colunas:")
for linha2 in linhas2:
    colunas = linha2.find_elements(By.TAG_NAME, "td")
    sobrenome = colunas[0].text
    nome = colunas[1].text
    email = colunas[2].text
    valor = colunas[3].text
    print(sobrenome, nome, email, valor)

# pegar uma célula específica
celula = browser.find_element(
    By.XPATH,
    "//table[@id='table1']/tbody/tr[3]/td[2]"
)
print("Célula: ",celula.text)


# encontrar uma linha pelo conteúdo
linhas = browser.find_elements(By.XPATH,"//table[@id='table1']/tbody/tr")

for linha in linhas:
    colunas = linha.find_elements(By.TAG_NAME, "td")
    if colunas[0].text == "Doe":
        print("Encontrado")
        print("Nome:", colunas[1].text)
        print("Email:", colunas[2].text)


# clicar no Edit de uma linha específica
linhas = browser.find_elements(By.XPATH,"//table[@id='table1']/tbody/tr")

for linha in linhas:
    colunas = linha.find_elements(By.TAG_NAME, "td")

    if colunas[0].text == "Doe":
        linha.find_element(By.LINK_TEXT,"edit").click()

# ou assim direto
# browser.find_element(
#     By.XPATH,
#     "//td[text()='Doe']/following-sibling::td[5]/a[text()='edit']"
# ).click()


browser.quit()



