from playwright.sync_api import expect
from web_page import WebTables


class TestWebPages:

    def test_adding_new_user(self, page):
        user = WebTables(page)
        user.navigate()
        user.add_new_user('Maria', 'Jones', 'maria.jones@testmail.com', '30', '5000', 'Sales')
        user.submit_application()

        expect(page.get_by_role("row", name="Maria Jones 30 maria.jones@testmail.com 5000 Sales",
                                exact=False)).to_be_visible()

    def test_search_for_user(self, page):
        user = WebTables(page)
        user.navigate()
        user.search_for_user('Cierra')

        assert user.page.get_by_role("gridcell", name="Cierra", exact=True)

    def test_delete_user_from_search_result(self, page):
        user = WebTables(page)
        user.navigate()
        user.search_for_user('Cierra')
        user.delete_user_from_search_result()

        assert user.search_for_user('Cierra') is None

    def test_delete_user_from_the_table(self, page):
        user = WebTables(page)
        user.navigate()
        user.delete_user_from_the_table('Cierra', 'Vega', 39, 'cierra@example.com', 10000, 'Insurance')
        user.search_for_user('Cierra')

        assert user.search_for_user('Cierra') is None
