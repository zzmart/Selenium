from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
browser.implicitly_wait(5)

browser.maximize_window()
browser.get("https://leogcarvalho.github.io/test-automation-practice/")
wait = WebDriverWait(browser, 10)

# exemplo 3
try:

    # ********
    # Login Form and button click
    # ********
    username = browser.find_element(By.ID, "username")
    password = browser.find_element(By.ID, "password")
    username.send_keys("admin")
    password.send_keys("1234")
    botaoLog = browser.find_element(By.ID, "login-button2")
    botaoLog.click()

except Exception:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    browser.save_screenshot(f"screenshot/test_login1_{timestamp}.png")

    raise

finally:
    browser.quit()

# exemplo 1
try:
    assert 1==2

except Exception:
    browser.save_screenshot(f"screenshot/test_login1.png")

    raise

finally:
    browser.quit()

#exemplo 2
try:
    assert 1==2

except Exception:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    browser.save_screenshot(f"screenshots/test_login1_{timestamp}.png")
#screenshot vem com data e hora
    raise

finally:
    browser.quit()

