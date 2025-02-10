import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="module")
def launchBrowser() :
    global driver
    driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield
    driver.quit()

@pytest.fixture(scope="class")
def launchBrowserClass(request) :
    request.cls.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
    request.cls.driver.maximize_window()
    yield
    request.cls.driver.quit()

def test_goToUrl(launchBrowser) :
    driver.get('https://www.redbus.in/')


def test_getTitle(launchBrowser) :
    print(driver.title)

@pytest.mark.usefixtures("launchBrowserClass")
class Test_site:
    def test_enterUrl(self):
        self.driver.get("https://www.redbus.in/")