import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope='session')
def playwright():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        yield playwright, browser, context, page
        page.close()
        context.close()
        browser.close()


BASE_URL = 'https://demoqa.com/select-menu'


class SelectMenu:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto(BASE_URL)

    def select_value(self, option):
        self.page.locator("#withOptGroup svg").click()
        self.page.get_by_text(option, exact=True).click()

    def select_prefixes(self, prefix):
        self.page.locator("#selectOne svg").click()
        self.page.get_by_text(prefix, exact=True).click()

    def select_old_style_menu(self, color):
        self.page.locator("#oldSelectMenu").select_option(f"{color}")

    def drop_down(self, option):
        self.page.locator("#selectMenuContainer svg").nth(2).click()
        self.page.locator(f"#react-select-4-option-{option}").click()

    def clear_drop_down(self):
        self.page.locator("#selectMenuContainer path").nth(3).click()

    def select_car(self, car):
        self.page.locator("#cars").select_option(car)
