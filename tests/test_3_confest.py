import time

import pytest

from pages.cart_page import Cart_page
from pages.client_info_page import Client_info_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.main_page import Main_page
from pages.payment_page import Payment_page


@pytest.mark.run(order=3)
def test_buy_product_1(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    service_obj = Service('D:\\Projects\\resourceForPython\\chromedriver.exe')
    driver = webdriver.Chrome(service=service_obj, chrome_options=options)

    print("Start test_1")

    # Авторизовываемся и проверяем что попали на главную страницу
    login = Login_page(driver=driver)
    login.authorization()

    # Выбираем товар и кладем в корзину
    mp = Main_page(driver)
    mp.select_product_1()

    # Нажимаем кнопку checkout в корзине
    cp = Cart_page(driver)
    cp.product_confirmation()

    # Заполняем информацию о клиенте и жмем кнопку продолжить
    cip = Client_info_page(driver)
    cip.input_information()

    # На форме оплаты кликаем кнопку финишь
    pp = Payment_page(driver)
    pp.payment()

    # Делаем скриншот
    fp = Finish_page(driver)
    fp.finish()

    print("Finish test_1")
    time.sleep(5)
    driver.quit()

@pytest.mark.run(order=1)
def test_buy_product_2(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    service_obj = Service('D:\\Projects\\resourceForPython\\chromedriver.exe')
    driver = webdriver.Chrome(service=service_obj, chrome_options=options)

    print("Start test_2")

    # Авторизовываемся и проверяем что попали на главную страницу
    login = Login_page(driver=driver)
    login.authorization()

    # Выбираем товар и кладем в корзину
    mp = Main_page(driver)
    mp.select_product_2()

    # Нажимаем кнопку checkout в корзине
    cp = Cart_page(driver)
    cp.product_confirmation()

    print("Finish test_2")
    time.sleep(5)
    driver.quit()

@pytest.mark.run(order=2)
def test_buy_product_3(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    service_obj = Service('D:\\Projects\\resourceForPython\\chromedriver.exe')
    driver = webdriver.Chrome(service=service_obj, chrome_options=options)

    print("Start test_3")

    # Авторизовываемся и проверяем что попали на главную страницу
    login = Login_page(driver=driver)
    login.authorization()

    # Выбираем товар и кладем в корзину
    mp = Main_page(driver)
    mp.select_product_3()

    # Нажимаем кнопку checkout в корзине
    cp = Cart_page(driver)
    cp.product_confirmation()

    print("Finish test_3")
    time.sleep(5)
    driver.quit()

