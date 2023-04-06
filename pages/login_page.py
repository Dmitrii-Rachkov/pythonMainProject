from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

from base.base_class import Base
from utilities.logger import Logger


# Добавим в класс Login_page наш url
# Также передадим классу Login_page наш базовый класс Base, таким образом,
# класс Login_page станет потомком класса Base

class Login_page(Base):

    url = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        # указываем super() который будет указывать что это наш потомок класса
        super().__init__(driver)
        self.driver = driver


    # Locators - наши локаторы

    user = "//input[@id='user-name']"
    password = "//input[@id='password']"
    login_button = "//input[@id='login-button']"
    main_word = "//span[@class='title']"


    # Getters - обращение к нашим локаторам

    def get_user(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))


    # Actions - действия с нашими локаторами

    def input_user(self, user):
        self.get_user().send_keys(user)
        print("Input user")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login_button")


    # Methods

    def authorization(self):
        with allure.step("Authorization"):
            Logger.add_start_step(method="authorization")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.input_user("standard_user")
            self.input_password("secret_sauce")
            self.click_login_button()
            self.assert_word(self.get_main_word(), "PRODUCTS")
            Logger.add_end_step(url=self.driver.current_url, method="authorization")

