import allure

from Lesson_18.pages.web_pages import WebTables


@allure.story('Test Web Pages')
class TestWebPages:
    @allure.title('Test adding a new user')
    @allure.description('Test user can add a new user')
    def test_adding_new_user(self, page):
        user = WebTables(page)
        user.navigate()
        user.add_new_user('Maria', 'Jones', 'maria.jones@testmail.com', '30', '5000', 'Sales')
        user.submit_application()

        assert page.get_by_role("gridcell", name="Maria", exact=True)

    @allure.title('Test search for a user')
    @allure.description('Test user can search for a user')
    def test_search_for_user(self, page):
        user = WebTables(page)
        user.navigate()
        user.search_for_user('Cierra')

        assert user.page.get_by_role("gridcell", name="Cierra", exact=True)

    @allure.title('Test user deletion from the search results')
    @allure.description('Test user can delete a user from search results')
    def test_delete_user_from_search_result(self, page):
        user = WebTables(page)
        user.navigate()
        user.search_for_user('Cierra')
        user.delete_user_from_search_result()

        assert user.search_for_user('Cierra') is None

    @allure.title('Test user deletion from the table')
    @allure.description('Test user can delete a user from the table')
    def test_delete_user_from_the_table(self, page):
        user = WebTables(page)
        user.navigate()
        user.delete_user_from_the_table('Cierra', 'Vega', 39, 'cierra@example.com', 10000, 'Insurance')
        user.search_for_user('Cierra')

        assert user.search_for_user('Cierra') is None
