from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')

driver_path = "./chromedriver-win32/chromedriver.exe"

service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://www.google.co.jp')
search_bar = driver.find_element(By.NAME, value="q")
search_bar.send_keys("金沢工業大学")
search_bar.submit()

for elem_h3 in driver.find_elements(By.XPATH, value="//a/h3"):
    elem_a = elem_h3.find_element(By.XPATH, value="..")
    print(elem_h3.text)
    print(elem_a.get_attribute('href'))

driver.close()