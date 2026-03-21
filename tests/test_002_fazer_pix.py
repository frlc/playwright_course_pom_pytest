from playwright.sync_api import expect


def test_002_fazer_pix(common_page, login_page, home_page, pix_page) -> None:    
    login_page.login("user1", "pass1")
    home_page.acessar_menu("Fazer Pix")
    pix_page.fazer_pix("teste@teste.com", "100.00")
    expect(pix_page.success_message).to_be_visible()
    common_page.voltar_para_home()
    common_page.assert_text("4.900,00")
    home_page.acessar_menu("Ver Extrato")
    common_page.assert_text("Pix para teste@teste.com - R$ -100,00")
