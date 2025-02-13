import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
action = ActionChains(driver)

driver.get('https://jqueryui.com/droppable')
driver.maximize_window()

iframe = driver.find_element(By.XPATH, '//iframe[@class="demo-frame"]')
driver.switch_to.frame(iframe)

draggable = driver.find_element(By.XPATH, '//div[@id="draggable"]')
droppable = driver.find_element(By.XPATH, '//div[@id="droppable"]')
action.drag_and_drop(draggable, droppable).perform()

time.sleep(4)