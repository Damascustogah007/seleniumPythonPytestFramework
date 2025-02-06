import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains, Keys

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
driver.get('https://www.redbus.com/')
driver.maximize_window()

action = ActionChains(driver)
selected_date = '20-2-2025'
date = selected_date.split('-')
print(date)

departure_date = driver.find_element(By.XPATH, '//input[@id="onward_cal"]')
action.click(departure_date).perform()
time.sleep(5)

dates = driver.find_elements(By.XPATH, '//span[@class="DayTiles__CalendarDaysSpan-sc-14em0t0-1 xaHaF"]')
for d in dates :
    if d.text == date[0] :
        d.click()
        break

time.sleep(10)
