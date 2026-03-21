from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def acessar_menu(self, menu):
        self.page.get_by_role("button", name=f"{menu}").click()