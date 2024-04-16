from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from pages.edit_profile_page import EditProfilePage
from pages.login_page import LoginPage
from pages.main_page import MainPage
import allure

@allure.description('Редактирование профиля пользователя')
def test_editing_profile():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    lp = LoginPage(driver)
    lp.authorization()

    mp = MainPage(driver)
    mp.edit_profile_section()

    epp = EditProfilePage(driver)
    epp.edit_profile()