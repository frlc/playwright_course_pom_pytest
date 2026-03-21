from playwright.sync_api import Page, expect

class PixPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.pix_key_input = page.get_by_role("textbox", name="Chave Pix:")
        self.value_input = page.get_by_role("textbox", name="Valor:")
        self.send_pix_button = page.get_by_role("button", name="Enviar Pix")        
        self.success_message = page.get_by_role("heading", name="Transação Realizada com Sucesso!")

    def fazer_pix(self, pix_key, value):
        self.pix_key_input.wait_for()
        self.pix_key_input.fill(pix_key)
        self.value_input.fill(value)
        self.send_pix_button.click()