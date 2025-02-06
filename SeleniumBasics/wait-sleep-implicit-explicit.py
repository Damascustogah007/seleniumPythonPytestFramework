import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
driver.get('https://demo.automationtesting.in/')
driver.maximize_window()

input_email = driver.find_element(By.XPATH, '//input[@id="email"]')
input_email.send_keys('Test@gmail.com')

button = driver.find_element(By.XPATH, '//a[@href="Register.html"]/img')
button.click()

#wait sleep (Python wait)
# time.sleep(2)

#Wait implicit Wait - Implicitly waiting, WebDriver polls the DOM webpage
#Where are not available immediately and need some time to load
# driver.implicitly_wait(3)
#driver.find_element(By.XPATH, '//input[@placeholder="First Name"]').send_keys('Charles')

#Wait explicitly Wait - Hey allow your code to halt execution
#Or freeze the tread, until the condition you pass it resolves,
#The condition is called with a certain frequency until the timeout of the wait is elapsed
wait = WebDriverWait(driver, 5)
wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@placeholder="First Name"]'))).send_keys('Charles')

print('Test Passed!')