from playwright.sync_api import Page, expect

class EmprestimoPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.contratar_emprestimo_button = page.get_by_role("button", name="Contratar Empréstimo")
        

    def selecionar_valor_emprestimo(self, value_option):
        self.page.locator("input").nth(0).wait_for()
        self.page.locator("input").nth(0).check()

    def contratar_emprestimo(self):
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.contratar_emprestimo_button.click()

    