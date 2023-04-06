import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Подход №1 когда перед каждым тестом нужно инициализировать браузер

# @pytest.fixture()
# def set_up():
#     print("Start test")
#     service_obj = Service('D:\\Projects\\resourceForPython\\chromedriver.exe')
#     driver = webdriver.Chrome(service=service_obj)
#     url = 'https://www.saucedemo.com/'
#     self.driver.get(self.url)
#     self.driver.maximize_window()
#
#     yield
#     driver.quit()
#     print("Finish test")

# Подход №2

@pytest.fixture()
def set_up():
    print("Start test")
    yield
    print("Finish test")

@pytest.fixture(scope='module')
def set_group():
    print("Enter System")
    yield
    print("Exit System")
