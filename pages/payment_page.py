from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger
import allure


class Payment_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators - наши локаторы

    finish_button = "//button[@id='finish']"


    # Getters - обращение к нашим локаторам

    def get_finish_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.finish_button)))


    # Actions - действия с нашими локаторами

    def click_finish_button(self):
        self.get_finish_button().click()
        print("Click finish button")


    # Methods

    def payment(self):
        with allure.step("Payment"):
            Logger.add_start_step(method="payment")
            self.get_current_url()
            self.click_finish_button()
            Logger.add_end_step(url=self.driver.current_url, method="payment")
