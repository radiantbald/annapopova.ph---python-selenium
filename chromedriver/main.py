from selenium import webdriver
import time

url = 'https://annapopovaph.ru/'
driver = webdriver.Chrome(executable_path='/Users/radiantbald/QA/Selenium/chromedriver/chromedriver')

try:
    driver.get(url=url)
    driver.save_screenshot('annapopova.png')
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()