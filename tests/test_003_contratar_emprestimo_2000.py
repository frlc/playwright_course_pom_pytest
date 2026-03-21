from playwright.sync_api import expect
from time import sleep


def test_003_contratar_emprestimo_2000(common_page, login_page, home_page, emprestimo_page) -> None:    
    login_page.login("user1", "pass1")
    home_page.acessar_menu("Empréstimos")
    emprestimo_page.selecionar_valor_emprestimo("R$ 2.000,00")
    emprestimo_page.contratar_emprestimo()
    common_page.assert_text("Transação Realizada com Sucesso!")
    common_page.voltar_para_home()
    common_page.assert_text("7.000,00")
    home_page.acessar_menu("Ver Extrato")
    common_page.assert_text("Empréstimo contratado - R$ 2000,00")