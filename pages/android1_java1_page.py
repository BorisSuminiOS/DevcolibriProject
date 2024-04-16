import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utilities.logger import Logger


class Android1Java1Page(Base):

    # Locations

    button_buy = '//*[@id="content-wrapper"]/div[1]/main/div/div[2]/div/div[2]/section[1]/div/form/div[6]/button'
    text_payment = '//*[@id="paymentComponent"]/div[2]/div[3]/div[2]/button/span[1]'


    # Getters

    def get_text_payment(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.text_payment))).text

    def get_button_buy(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.button_buy)))

    # Actions

    def click_button_buy(self):
        self.get_button_buy().click()
        print('Click button buy')

    # Methods

    def making_order_android1_java1(self):
        with allure.step("Making_order_android1_java1"):
            Logger.add_start_step(method='making_order_android1_java1')
            '''Оформление заказа'''
            self.get_current_url()
            self.apply_scroll(0,200)
            self.click_button_buy()
            self.method_assert_word('Оплатить', self.get_text_payment())
            self.separator_tests()
            Logger.add_end_step(self.driver.current_url, method='making_order_android1_java1')
