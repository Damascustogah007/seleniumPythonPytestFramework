import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
driver.get('https://demo.automationtesting.in/Register.html')

#Radio Button
driver.find_element(By.XPATH, '//input[@value="FeMale"]').click()

#Checkboxes click multiple option and get_attribute
lst = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')
for ele in lst :
    val = ele.get_attribute('value')
    if val in ['Cricket', 'Movies']:
        ele.click()

time.sleep(10)