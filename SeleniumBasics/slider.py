import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
action = ActionChains(driver)

driver.get('https://www.snapdeal.com/products/mobiles-featured-phones?sort=plrty')
driver.maximize_window()

left_handle = driver.find_element(By.XPATH, '//a[contains(@class, "left-handle")]')
right_handle = driver.find_element(By.XPATH, '//a[contains(@class, "right-handle")]')

#First option
# action.drag_and_drop_by_offset(left_handle, 60, 0).perform()

#Second option
# action.click_and_hold(left_handle).pause(1).move_by_offset(50, 0).release().perform()
# time.sleep(4)

#Third Option
action.move_to_element(left_handle).pause(1).click_and_hold(left_handle).move_by_offset(80, 0).release().perform()