import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec


driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
action = ActionChains(driver)

driver.get('https://www.yatra.com/')
driver.maximize_window()


destination = driver.find_element(By.XPATH, '//p[contains(text(),\'DEL, Indira Gandhi International\')]')
time.sleep(1)
destination.screenshot(".\\seleniumPythonPytestFramework\\SeleniumBasics\\Screenshots\\test.png")


