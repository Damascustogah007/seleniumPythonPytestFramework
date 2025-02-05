from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
driver.get('https://demo.automationtesting.in/Register.html')

# Xpath

# Syntax
# //tagname[@attribute='value'] or //*[@attribute='value']
# //input[@placeholder="First Name"]
# //*[@placeholder="First Name"]

# text
# //label[text()="Full Name*"]

# contains
# //label[contains(text(), 'Full Name')]

# index
# (//label)[1]

# OR & AND
# //input[@placeholder="First Name" or ng-model="FirstName"]
# //input[@placeholder="First Name" and ng-model="FirstName"]

# parent - Child - ancestor
# //form[@id ="basicBootstrapForm"]/child::div[1]
# //form[@id ="basicBootstrapForm"]/parent::div
# //form[@id ="basicBootstrapForm"]/ancestor::div

#following - sibling - preceding
# //input[@id='checkbox1']//following-sibling::label