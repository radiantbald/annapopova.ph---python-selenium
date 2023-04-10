# Импортируем необходимые библиотеки
import selenium
from selenium import webdriver # Вебдрайвер для управления браузерами
from selenium.webdriver.common.by import By 
import pytest
import time # Библиотека для управления ожиданиями

# Опции
options =  webdriver.ChromeOptions() # Опции для GoogleChrome

# Отключить режим вебдрайвера до версии 79.0.3945.16
# options.add_experimental_option('excludeSwitches', ['enable-automation'])
# options.add_experimental_option('useAutomationExtention', False)

# Отключить режим вебрайвера для версии после 79.0.3945.16
options.add_argument('--disable-blink-features=AutomationControlled')

options.add_argument('--incognito') # Заходим через режим инкогнито

driver = webdriver.Chrome(
    executable_path='/Users/radiantbald/QA/Selenium/chromedriver/chromedriver', # Определение вебдрайвера
    options=options # Определение опций
)

try:
#    driver.get('https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')
   driver.get('https://www.google.com/')
   input_google = driver.find_element(By.XPATH, "//*[@name='q']") # Поиск по XPATH
   input_google.send_keys('annapopovaph.ru \n')
   input_google = driver.find_element(By.XPATH, "//a[@href='https://annapopovaph.ru/']").click()

   time.sleep(5)
#    driver.get('https://annapopovaph.ru/') # Зайти на сайт

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()