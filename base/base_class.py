import time
import datetime
from selenium.webdriver import ActionChains


class Base():
    def __init__(self, driver):
        self.driver = driver


    def get_current_url(self):
        print(f'URL: {self.driver.current_url}')


    def separator_tests(self):
        print('------------------------')


    def method_assert_word(self, word, result):
        assert word == result
        print(f"Verification is successful: '{word}'")


    def apply_scrolling_to_element(self, locator):
        action = ActionChains(self.driver)
        action.move_to_element(locator).perform()


    def apply_scroll(self, x, y):
        time.sleep(2)
        self.driver.execute_script(f"window.scrollTo({x}, {y})")
        print(f'Scroll, horizontal: {x}, vertical: {y}')
        time.sleep(2)


    def to_screenshot(self, name):
        time.sleep(7)
        date = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        name = rf'C:\Users\ноутбук\PycharmProjects\DevcolibriProject\screen\{name}_{date}.png'
        self.driver.save_screenshot(name)
        print(f'Screenshot is successful: {name}')
        time.sleep(2)
