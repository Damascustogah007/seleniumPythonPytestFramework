import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
driver.get('https://demo.automationtesting.in/Alerts.html')
driver.maximize_window()

driver.find_element(By.XPATH, '//div[@id="OKTab"]').click()
time.sleep(2)
#
# #Accept
driver.switch_to.alert.accept()
time.sleep(2)

#Cancel
driver.find_element(By.XPATH, '//a[@href="#CancelTab"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//div[@id="CancelTab"]').click()
time.sleep(2)

driver.switch_to.alert.dismiss()
time.sleep(2)

confirm = driver.find_element(By.XPATH, '//p[@id="demo"]')
confirm.is_displayed()


#Prompt
driver.find_element(By.XPATH, '//a[@href="#Textbox"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//div[@id="Textbox"]').click()
time.sleep(2)

text = driver.switch_to.alert.text
print(text)

driver.switch_to.alert.send_keys('Hello')
driver.switch_to.alert.accept()
verify_prompt = (driver.find_element(By.XPATH, '//p[@id="demo1"]'))
verify_prompt.is_displayed()
print('Test Passed Successfully!')