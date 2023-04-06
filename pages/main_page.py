from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger
import allure


class Main_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators - наши локаторы

    add_product_1 = "//button[@id='add-to-cart-sauce-labs-backpack']"
    add_product_2 = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    add_product_3 = "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
    cart = "//div[@id='shopping_cart_container']"
    menu = "//button[@id='react-burger-menu-btn']"
    link_about = "//a[@id='about_sidebar_link']"


    # Getters - обращение к нашим локаторам

    def get_add_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_product_1)))

    def get_add_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_product_2)))

    def get_add_product_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_product_3)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu)))

    def get_link_about(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_about)))


    # Actions - действия с нашими локаторами

    def click_add_product_1(self):
        self.get_add_product_1().click()
        print("Click add_product_1")

    def click_add_product_2(self):
        self.get_add_product_2().click()
        print("Click add_product_2")

    def click_add_product_3(self):
        self.get_add_product_3().click()
        print("Click add_product_3")

    def click_cart(self):
        self.get_cart().click()
        print("Click cart")

    def click_menu(self):
        self.get_menu().click()
        print("Click menu")

    def click_link_about(self):
        self.get_link_about().click()
        print("Click about")


    # Methods

    # Выбор продукта и переход в корзину
    def select_product_1(self):
        with allure.step("Select product 1"):
            Logger.add_start_step(method="select_product_1")
            self.get_current_url()
            self.click_add_product_1()
            self.click_cart()
            Logger.add_end_step(url=self.driver.current_url, method="select_product_1")

    def select_product_2(self):
        with allure.step("Select product 2"):
            Logger.add_start_step(method="select_product_2")
            self.get_current_url()
            self.click_add_product_2()
            self.click_cart()
            Logger.add_end_step(url=self.driver.current_url, method="select_product_2")

    def select_product_3(self):
        with allure.step("Select product 3"):
            Logger.add_start_step(method="select_product_3")
            self.get_current_url()
            self.click_add_product_3()
            self.click_cart()
            Logger.add_end_step(url=self.driver.current_url, method="select_product_3")

    # Переход в меню и нажатие about
    def select_menu_about(self):
        with allure.step("Select menu about"):
            Logger.add_start_step(method="select_menu_about")
            self.get_current_url()
            self.click_menu()
            self.click_link_about()
            self.assert_url("https://saucelabs.com/")
            Logger.add_end_step(url=self.driver.current_url, method="select_menu_about")
