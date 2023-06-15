import allure
import pytest
import requests
from selenium.common import ElementNotVisibleException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


WELCOME_TO_INTERNET = 'http://the-internet.herokuapp.com/'


@allure.story('Welcome to Internet tests')
class TestInternet:

    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(WELCOME_TO_INTERNET)

    def teardown_method(self):
        self.driver.quit()

    def search_element(self, by, selector):
        wait = WebDriverWait(self.driver, timeout=10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException])
        return wait.until(EC.element_to_be_clickable((by, selector)))

    @allure.title('Hover test')
    @allure.description('Test hovering over the items')
    def test_hover(self):
        open_hover_page = self.search_element(By.XPATH, '//*[@id="content"]/ul/li[25]/a')
        open_hover_page.click()

        hover_to_user_1 = self.search_element(By.XPATH, '//*[@id="content"]/div/div[1]')
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(hover_to_user_1).perform()

        open_profile = self.search_element(By.XPATH, '//*[@id="content"]/div/div[1]/div/a')
        open_profile.click()

        current_url = self.driver.current_url
        expected_url = 'http://the-internet.herokuapp.com/users/1'

        assert current_url == expected_url

        page_title = self.search_element(By.XPATH, '/html/body/h1')

        assert page_title.text == 'Not Found'

    @allure.title('Redirection test')
    @allure.description('Test link redirection and its status code')
    def test_redirection(self):

        redirection_url = "http://the-internet.herokuapp.com/status_codes"

        open_redirection_page = self.search_element(By.XPATH, '//*[@id="content"]/ul/li[36]/a')
        open_redirection_page.click()

        redirect_link = self.search_element(By.ID, "redirect")
        redirect_link.click()

        current_url = self.driver.current_url
        assert current_url == redirection_url

        redirection = requests.get(redirection_url)

        assert redirection.status_code == 200

    @allure.title('Key press test')
    @allure.description('Test key press')
    def test_key_press(self):
        open_key_press_page = self.search_element(By.XPATH, '//*[@id="content"]/ul/li[31]/a')
        open_key_press_page.click()

        activate_input = self.search_element(By.ID, "target")

        actions = ActionChains(self.driver)
        actions.click(activate_input)
        actions.send_keys(Keys.NUMPAD3)
        actions.perform()

        assert activate_input.is_displayed()

    @allure.title('JS alerts test')
    @allure.description('Test JS alerts and how to manage them')
    def test_js_alerts(self):
        open_js_alerts_page = self.search_element(By.XPATH, '//*[@id="content"]/ul/li[29]/a')
        open_js_alerts_page.click()

        call_js_alert = self.search_element(By.XPATH, '//*[@id="content"]/div/ul/li[1]/button')
        call_js_alert.click()

        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()

        assert alert_text == 'I am a JS Alert'

        call_js_confirm = self.search_element(By.XPATH, '//*[@id="content"]/div/ul/li[2]/button')
        call_js_confirm.click()

        alert.dismiss()
        alert_result_text = self.search_element(By.ID, "result").text

        assert alert_result_text == 'You clicked: Cancel'

        call_js_confirm = self.search_element(By.XPATH, '//*[@id="content"]/div/ul/li[2]/button')
        call_js_confirm.click()

        alert.accept()
        alert_result_text = self.search_element(By.ID, "result").text

        assert alert_result_text == 'You clicked: Ok'

        call_js_prompt = self.search_element(By.XPATH, '//*[@id="content"]/div/ul/li[3]/button')
        call_js_prompt.click()

        alert.send_keys('Hello World')
        alert.accept()

        prompt_result_text = self.search_element(By.ID, "result").text

        assert prompt_result_text == 'You entered: Hello World'
















