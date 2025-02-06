#Frame means a page inside a page

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
driver.get('https://demo.automationtesting.in/Frames.html')
driver.maximize_window()

#SwitchTo Frames Window
#Using index
#This is not recommended because if more frames are added the index of the frame changes
# driver.switch_to.frame(0)

#Using name or id
# driver.switch_to.frame('singleframe') #name
# driver.switch_to.frame('singleframe') #id

#Using web element
iframe = driver.find_element(By.XPATH, '//iframe[@id="singleframe"]')
driver.switch_to.frame(iframe)
text = driver.find_element(By.TAG_NAME, 'input')
text.send_keys('This is an Iframe example')
time.sleep(3)

#Return to home default
driver.switch_to.default_content()
time.sleep(2)
siteHeader = driver.find_element(By.XPATH, '//h1[contains(text(), "Automation Demo Site ")]')
siteHeader.is_displayed()

print("Test Passed!")