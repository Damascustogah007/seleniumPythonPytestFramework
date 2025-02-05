from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
# driver.get('https://demo.automationtesting.in/')
driver.get('https://www.google.com/')
print(driver.title)

'''
Locators

By.ID
By.NAME
By.CLASS_NAME
By.TAG_NAME
By.LINK_TEXT
By.PARTIAL_LINK_TEXT
By.CSS_SELECTOR
By.XPATH
'''

# inputField = driver.find_element(By.ID, 'email')
# inputField.send_keys('test@gmail.com')
# send_button = driver.find_element(By.ID, 'enterimg')
# send_button.click()


# send_button = driver.find_element(By.PARTIAL_LINK_TEXT, 'About')
# send_button.click()

driver.quit()