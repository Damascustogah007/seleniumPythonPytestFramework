import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
driver.get('https://demo.automationtesting.in/Windows.html')
driver.maximize_window()

#Parent Window
parentWindow = driver.current_window_handle

#All Window
driver.find_element(By.XPATH, '//a[@href="http://www.selenium.dev"]').click()
allWindows = driver.window_handles

#Getting the length of all tabs
print(len(allWindows))

# Switch to child window
driver.switch_to.window(allWindows[1])

# Alternatively
# for win in windows:
#     if win != parentWindow :
#         driver.switch_to.window(win)
time.sleep(2)

#Do action in child window
driver.find_element(By.XPATH, '//span[contains(text(), "Downloads")]').click()
pageHeading = driver.find_element(By.XPATH, '//h1[@class="d-1"]')
pageHeading.is_displayed()
time.sleep(2)

#Close current window
# driver.close()

#Switch back to parent window
driver.switch_to.window(parentWindow)
time.sleep(2)
siteHeader = driver.find_element(By.XPATH, '//h1[contains(text(), "Automation Demo Site ")]')
siteHeader.is_displayed()

print('Test Passed!')