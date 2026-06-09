from selenium import webdriver

browser = webdriver.Chrome()

browser.get("https://www.saucedemo.com/")

print("pagina: ", browser.title)
print("url: ", browser.current_url)
print("page source: ", browser.page_source)

