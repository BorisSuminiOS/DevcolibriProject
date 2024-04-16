import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utilities.logger import Logger


class PaymentPage(Base):

    # Locations

    card_number = 'input[name="CardNumber"]'
    card_date = 'input[name = "ValidTo"]'
    code_cvc = 'input[name="CVC"]'
    card_holder = 'input[name="CardHolder"]'
    button_payment = '//*[@id="paymentComponent"]/div[2]/div[3]/div[2]/button'
    button_success_1= '//*[@id="globalPopupList"]/div/div[2]/div/div[3]/div[2]/button[2]/span'
    text_info_order = '/html/body/div/div[3]/div[1]/div/joomla-alert/div[2]/div'
    button_installment = '//*[@id="app"]/div[3]/div[2]/div/div[2]/div/div/div[1]/div/div/div[4]/div[2]/div/div[1]/div[2]'
    button_checkout = '//*[@id="app"]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[3]/div/div[1]/div[5]/button'
    button_success_2 = '//*[@id="globalPopupList"]/div/div[2]/div/div[3]/div[2]/button[2]/span'

    # Getters
    def get_card_number(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.card_number)))

    def get_card_date(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.card_date)))

    def get_code_cvc(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.code_cvc)))

    def get_card_holder(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.card_holder)))

    def get_button_payment(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.button_payment)))

    def get_button_success(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.button_success_1)))

    def get_text_info_order(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.text_info_order))).text

    def get_button_installment(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.button_installment)))

    def get_button_checkout(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.button_checkout)))

    def get_button_success_2(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.button_success_2)))

    # Actions

    def input_card_number(self, card_number):
        self.get_card_number().send_keys(card_number)
        print('Input card number')

    def input_card_date(self, card_date):
        self.get_card_date().send_keys(card_date)
        print('Input card date')

    def input_code_cvc(self, code_cvc):
        self.get_code_cvc().send_keys(code_cvc)
        print('Input code cvc')

    def input_card_holder(self, card_holder):
        self.get_card_holder().send_keys(card_holder)
        print('Input card holder')

    def click_button_payment(self):
        self.get_button_payment().click()
        print('Click button payment')

    def click_button_success(self):
        self.get_button_success().click()
        print('Click button success')

    def click_button_installment(self):
        self.get_button_installment().click()
        print('Click button installment')

    def click_button_checkout(self):
        self.get_button_checkout().click()
        print('Click button checkout')

    def click_button_success_2(self):
        self.get_button_success_2().click()
        print('Click button success 2')

    # Methods

    def payment_course_java1_java2(self):
        with allure.step("Payment_course_java1_java2"):
            Logger.add_start_step(method='payment_course_java1_java2')
            '''Оплата курса по карте'''
            self.get_current_url()
            self.input_card_number(1111111111112222)
            self.input_card_date(1111)
            self.input_code_cvc(111)
            self.input_card_holder('ALEX')
            self.click_button_payment()
            self.click_button_success()
            self.to_screenshot('payment_course_1')
            self.separator_tests()
            Logger.add_end_step(self.driver.current_url, method='payment_course_java1_java2')
            self.driver.close()

    def payment_course_android1_java1(self):
        with allure.step("Payment_course_android1_java1"):
            Logger.add_start_step(method='payment_course_android1_java1')
            '''Оплата курса в рассрочку'''
            self.get_current_url()
            self.click_button_installment()
            self.click_button_checkout()
            self.click_button_success_2()
            self.to_screenshot('payment_course_2')
            self.separator_tests()
            Logger.add_end_step(self.driver.current_url, method='payment_course_android1_java1')
            self.driver.close()

