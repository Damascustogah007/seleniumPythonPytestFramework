import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
action = ActionChains(driver)

driver.get('https://demo.guru99.com/test/simple_context_menu.html')
driver.maximize_window()

# Right click
btn = driver.find_element(By.XPATH, '//span[@class="context-menu-one btn btn-neutral"]')
action.context_click(btn).perform()

editBtn = driver.find_element(By.XPATH, '//span[contains(text(), \'Edit\')]')
action.click(editBtn).perform()

driver.switch_to.alert.accept()
time.sleep(3)

# Double click
btn = driver.find_element(By.XPATH, '//button[contains(text(),\'Double-Click Me To See Alert\')]')
action.double_click(btn).perform()

driver.switch_to.alert.accept()
time.sleep(3)

print('Passed!')