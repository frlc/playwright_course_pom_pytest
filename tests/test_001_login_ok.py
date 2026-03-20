from playwright.sync_api import expect


def test_001_login_ok(login_page) -> None:    
    login_page.login("user1", "pass1")
    expect(login_page.welcome_message).to_be_visible()  

