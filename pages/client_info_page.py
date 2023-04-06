from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from base.base_class import Base
from utilities.logger import Logger


class Client_info_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators - наши локаторы

    first_name = "//input[@id='first-name']"
    last_name = "//input[@id='last-name']"
    postal_code = "//input[@id='postal-code']"
    continue_button = "//input[@id='continue']"


    # Getters - обращение к нашим локаторам

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_postal_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.postal_code)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))


    # Actions - действия с нашими локаторами

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("Input first name")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("Input last name")

    def input_postal_code(self, postal_code):
        self.get_postal_code().send_keys(postal_code)
        print("Input postal code")

    def click_continue_button(self):
        self.get_continue_button().click()
        print("Click continue button")


    # Methods

    def input_information(self):
        with allure.step("Input information"):
            Logger.add_start_step(method="input_information")
            self.get_current_url()
            self.input_first_name("John")
            self.input_last_name("Rambo")
            self.input_postal_code("12345")
            self.click_continue_button()
            Logger.add_end_step(url=self.driver.current_url, method="input_information")

