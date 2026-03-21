from playwright.sync_api import Page, expect

class ExtratoPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.transaction = page.get_by_text("/20/2026 - Pix para frlc - R$ -15,00").first