# from selenium import webdriver
from seleniumwire import webdriver
import time
import random
from fake_useragent import UserAgent
from proxy_auth_data import login, password

# url = 'https://annapopovaph.ru/'

# user_agents_list = [
#     'hello_world',
#     'best_of_the_best',
#     'python_today'
# ]

options = webdriver.ChromeOptions()

# useragent = UserAgent()

# options.add_argument(f'user-agent={random.choice(user_agents_list)}')
# options.add_argument(f'user-agent={useragent.ie}')
# options.add_argument('--proxy-server=138.128.91.63:8000')

proxy_options = {
    'proxy': {
        'https': f'http//{login}:{password}@138.128.91.63:8000'
    }
}

driver = webdriver.Chrome(executable_path = '/Users/radiantbald/QA/Selenium/chromedriver/chromedriver', 
                          seleniumwire_options = proxy_options
                          )

try:
     # driver.get(url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent/')
     # driver.save_screenshot('annapopova.png')
     driver.get('https://2ip.ru')
     time.sleep(20)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()