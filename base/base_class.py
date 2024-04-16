import time
import datetime
from selenium.webdriver import ActionChains


class Base():
    def __init__(self, driver):
        self.driver = driver


    '''Получить текущий URL'''
    def get_current_url(self):
        print(f'URL: {self.driver.current_url}')


    '''Метод для разделения тестов'''
    def separator_tests(self):
        print('---------------------------------------------------------')


    '''Метод сравнения элемента по тексту'''
    def method_assert_word(self, word, result):
        assert word == result
        print(f"Verification is successful: '{word}'")


    '''Позволяет сделать прокрутку страницы до выбранного элемента'''
    def apply_scrolling_to_element(self, locator):
        action = ActionChains(self.driver)
        action.move_to_element(locator).perform()


    '''Позволяет сделать прокрутку по X и Y'''
    def apply_scroll(self, x, y):
        time.sleep(2)
        self.driver.execute_script(f"window.scrollTo({x}, {y})")
        print(f'Scroll, horizontal: {x}, vertical: {y}')
        time.sleep(2)


    '''Метод для получения скриншота страницы'''
    def to_screenshot(self, name):
        time.sleep(7)
        date = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        name = rf'C:\Users\ноутбук\PycharmProjects\DevcolibriProject\screen\{name}_{date}.png'
        self.driver.save_screenshot(name)
        print(f'Screenshot is successful: {name}')
        time.sleep(2)
