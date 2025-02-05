import time
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
driver.get('https://demo.automationtesting.in/Register.html')
driver.maximize_window()


#Select class declaration with webelement
ele = driver.find_element(By.ID, 'Skills')
sel = Select(ele)

#select by index
sel.select_by_index(5)

#select by value
sel.select_by_value('AutoCAD')

#select by visible text
sel.select_by_visible_text('Client Server')
print(driver.current_url)

#navigate different url
driver.get('https://www.google.com')
print(driver.current_url)

#back
driver.back()

#refresh
driver.refresh()

#forward
driver.forward()

time.sleep(10)

driver.quit()