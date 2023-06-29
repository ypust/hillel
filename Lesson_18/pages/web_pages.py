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


BASE_URL = "https://demoqa.com/webtables"


class WebTables:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto(BASE_URL)

    def add_new_user(self, first_name, last_name, email, age, salary, department):
        self.page.locator('[id=addNewRecordButton]').click()
        self.page.locator('[id=firstName]').fill(first_name)
        self.page.locator('[id=lastName]').fill(last_name)
        self.page.locator('[id=userEmail]').fill(email)
        self.page.locator('[id=age]').fill(age)
        self.page.locator('[id=salary]').fill(salary)
        self.page.locator('[id=department]').fill(department)

    def submit_application(self):
        self.page.locator('[id=submit]').click()

    def search_for_user(self, user_name):
        self.page.locator('[id=searchBox]').fill(user_name)

    def edit_user(self, first_name, last_name, email, age, salary, department):
        self.page.locator('[id="edit-record-1"]').click()
        self.page.locator('[id=addNewRecordButton]').click()
        self.page.locator('[id=firstName]').fill(first_name)
        self.page.locator('[id=lastName]').fill(last_name)
        self.page.locator('[id=userEmail]').fill(email)
        self.page.locator('[id=age]').fill(age)
        self.page.locator('[id=salary]').fill(salary)
        self.page.locator('[id=department]').fill(department)

    def delete_user_from_search_result(self):
        self.page.get_by_title("Delete").get_by_role("img").click()

    def delete_user_from_the_table(self, first_name, last_name, age, email, salary, department):
        self.page.get_by_role("row",
                              name=f"{first_name} {last_name} {age} {email} {salary} {department} Edit Delete").get_by_title(
            "Delete").locator("path").click()
