import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utilities.logger import Logger


class Java1Java2Page(Base):

    # Locations

    button_buy_1 = 'button[data-product_id="1"]'
    button_buy_2 = '//*[@id="RadicalMartExpressCheckoutModal"]/div/div/div[2]/form/div[6]/button'
    text_java1_java2 = '//*[@id="content-wrapper"]/div[1]/main/div/div[1]/div[1]/hgroup/h1'
    first_name = 'input[placeholder="Имя"]'
    last_name ='input[placeholder="Фамилия"]'
    email ='input[placeholder="Email"]'
    phone ='input[placeholder="Телефон"]'
    text_payment = '//*[@id="paymentComponent"]/div[2]/div[3]/div[2]/button/span[1]'


    # Getters

    def get_text_payment(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.text_payment))).text

    def get_button_buy_1(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.button_buy_1)))

    def get_first_name(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.last_name)))

    def get_email(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.email)))

    def get_phone(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.phone)))

    def get_button_buy_2(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.button_buy_2)))


    # Actions

    def click_button_buy_1(self):
        self.get_button_buy_1().click()
        print('Click button buy')

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print('Input first name')

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print('Input last name')

    def input_email(self, email):
        self.get_email().send_keys(email)
        print('Input email')

    def input_phone(self, phone):
        self.get_phone().send_keys(phone)
        print('Input phone')

    def click_button_buy_2(self):
        self.get_button_buy_2().click()
        print('Click button buy')

    # Methods
    def making_order_java1_java2(self):
        with allure.step("Making_order_java1_java2"):
            Logger.add_start_step(method='making_order_java1_java2')
            '''Оформление заказа'''
            self.get_current_url()
            self.apply_scroll(0,200)
            self.click_button_buy_1()
            self.input_first_name('Борис')
            self.input_last_name('Сумин')
            self.input_email('test_user2024@mail.ru')
            self.input_phone('89885648734')
            self.click_button_buy_2()
            self.method_assert_word('Оплатить', self.get_text_payment())
            self.separator_tests()
            Logger.add_end_step(self.driver.current_url, method='making_order_java1_java2')
