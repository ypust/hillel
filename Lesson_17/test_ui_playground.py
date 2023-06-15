import random
import time
import allure
import pytest
from selenium.common import ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

UI_TEST_PLAYGROUND = 'http://uitestingplayground.com/home'


@allure.story('UI Playground tests')
class TestPlayground:

    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(UI_TEST_PLAYGROUND)

    def teardown_method(self):
        self.driver.quit()

    def search_element(self, by, selector):
        wait = WebDriverWait(self.driver, timeout=10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException])
        return wait.until(EC.element_to_be_clickable((by, selector)))

    @staticmethod
    def generate_username():
        names = ['johny', 'liza', 'sara', 'mike', 'kate', 'janet', 'nancy']
        surnames = ['smith', 'brown', 'turtle', 'bird', 'harrison', 'lion', 'philips']
        numbers = random.randint(10, 99)

        name = random.choice(names)
        surname = random.choice(surnames)
        username = name + surname + str(numbers)

        return username

    @allure.title('dynamic_id_page test')
    @allure.description('Test the dynamic_id page')
    def test_dynamic_id_page(self):
        open_dynamic_id_link = self.search_element(By.XPATH, '//*[@id="overview"]/div/div[1]/div[1]/h3/a')
        open_dynamic_id_link.click()

        page_title = self.search_element(By.XPATH, '/html/body/section/div/h3')
        page_title_text = page_title.text

        current_url = self.driver.current_url
        expected_url = 'http://uitestingplayground.com/dynamicid'

        assert current_url == expected_url

        assert page_title_text == 'Dynamic ID'

    @allure.title('class_attribute test')
    @allure.description('Test the class_attribute page')
    def test_class_attribute(self):
        open_class_attribute_link = self.search_element(By.XPATH, '//*[@id="overview"]/div/div[1]/div[2]/h3/a')
        open_class_attribute_link.click()

        page_title = self.search_element(By.XPATH, '/html/body/section/div/h3')
        page_title_text = page_title.text
        assert page_title_text == 'Class Attribute'

        button_pop_up = self.search_element(By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
        button_pop_up.click()

        accept = self.driver.switch_to.alert
        accept.accept()

        current_url = self.driver.current_url
        expected_url = 'http://uitestingplayground.com/classattr'
        assert current_url == expected_url

    @allure.title('text_input test')
    @allure.description('Test the text_input page')
    def test_text_input(self):
        open_text_input_link = self.search_element(By.XPATH, '//*[@id="overview"]/div/div[2]/div[4]/h3/a')
        open_text_input_link.click()

        new_name = 'Activation button'

        input_field = self.search_element(By.ID, 'newButtonName')
        input_field.click()
        input_field.send_keys(new_name)

        button = self.search_element(By.ID, 'updatingButton')
        button.click()

        assert new_name == button.text

    @allure.title('sample_app test')
    @allure.description('Test the sample_app page')
    def test_sample_app(self):
        open_sample_app = self.search_element(By.XPATH, '//*[@id="overview"]/div/div[4]/div[2]/h3/a')
        open_sample_app.click()

        username = self.generate_username()

        enter_user_name = self.search_element(By.XPATH, '//input[@name="UserName"]')
        enter_user_name.click()
        enter_user_name.send_keys(username)

        enter_password = self.search_element(By.XPATH, '//input[@name="Password"]')
        enter_password.click()
        enter_password.send_keys("pwd")

        login = self.search_element(By.ID, "login")
        login.click()

        is_logged_in = self.search_element(By.ID, "loginstatus")

        assert is_logged_in.text == f"Welcome, {username}!"

    @allure.title('overlapped_element test')
    @allure.description('Test the overlapped_element page')
    def test_overlapped_element(self):

        open_overlapped_element_page = self.search_element(By.XPATH, '//*[@id="overview"]/div/div[5]/div[1]/h3/a')
        open_overlapped_element_page.click()

        id_input = self.search_element(By.ID, 'id')
        id_input.click()
        id_input.send_keys('UFH32JF')

        name_input = self.search_element(By.ID, 'name')

        self.driver.execute_script("arguments[0].scrollIntoView();", name_input)
        time.sleep(2)

        name_input.click()
        name_input.send_keys('User13')

        assert id_input.get_attribute('value') == 'UFH32JF'
        assert name_input.get_attribute('value') == 'User13'


