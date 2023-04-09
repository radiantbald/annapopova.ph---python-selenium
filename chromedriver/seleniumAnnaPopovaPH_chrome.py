# Импортируем необходимые библиотеки
import selenium
from selenium import webdriver # Вебдрайвер для управления браузерами
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
   driver.get('https://annapopovaph.ru/') # Зайти на сайт
   time.sleep(5)


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()