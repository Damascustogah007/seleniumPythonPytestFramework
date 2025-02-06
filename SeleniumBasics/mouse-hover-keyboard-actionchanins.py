import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains, Keys

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
driver.get('https://magento.softwaretestingboard.com/')
driver.maximize_window()

#ActionChains - mouse movements, mouse button actions, keypress, and context menu interactions
#MouseHover

action = ActionChains(driver)

womanNavTab = driver.find_element(By.XPATH, '//a[@id="ui-id-4"]')
action.move_to_element(womanNavTab).perform()

topsNavTab = driver.find_element(By.XPATH, '//a[@id="ui-id-9"]')
action.move_to_element(topsNavTab).perform()

hoodiesNavTab = driver.find_element(By.XPATH, '//a[@id="ui-id-12"]')
action.click(hoodiesNavTab).perform()

wait = WebDriverWait(driver, 5)
wait.until(ec.visibility_of_element_located((By.XPATH, '//h1[@id="page-title-heading"]'))).is_displayed()

#Keyboard Actions
ser_tab = driver.find_element(By.XPATH, '//input[@id="search"]')
action.click(ser_tab).key_down(Keys.SHIFT).send_keys('test').key_up(Keys.SHIFT).perform()
time.sleep(5)
