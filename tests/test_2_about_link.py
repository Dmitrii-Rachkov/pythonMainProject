import time

from pages.cart_page import Cart_page
from pages.client_info_page import Client_info_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from pages.main_page import Main_page
from pages.payment_page import Payment_page


def test_about_link():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    service_obj = Service('D:\\Projects\\resourceForPython\\chromedriver.exe')
    driver = webdriver.Chrome(service=service_obj, chrome_options=options)

    print("Start test")

    # Авторизовываемся и проверяем что попали на главную страницу
    login = Login_page(driver=driver)
    login.authorization()

    # Выбираем товар и кладем в корзину
    mp = Main_page(driver)
    mp.select_menu_about()


    print("Finish test")
    time.sleep(5)
    driver.quit()

