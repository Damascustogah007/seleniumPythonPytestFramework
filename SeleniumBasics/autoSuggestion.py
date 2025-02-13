import time
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
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
action.click(destination).perform()
action.send_keys('Kol').perform()
time.sleep(3)

new_dest = driver.find_elements(By.XPATH, '//div[@class="fw-600 mb-0"]')
for city in new_dest:
    if 'Kolkata, (CCU)' in city.text:
        city.click()
    break

wait = WebDriverWait(driver, 5, 1, ignored_exceptions=[ElementClickInterceptedException])
wait.until(ec.visibility_of_element_located((By.XPATH, '//p[contains(text(),\'kolkata\')]'))).is_displayed()

print('Test passed!')

