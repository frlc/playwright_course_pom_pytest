import pytest
from pages.common_page import CommonPage
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.pix_page import PixPage
from pages.extrato_page import ExtratoPage
from pages.emprestimo_page import EmprestimoPage

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "headless": True,
        "slow_mo": 500,
    }

# Controla viewport — aqui é o lugar certo
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
    }

@pytest.fixture
def page(page):
    page.goto("https://leogcarvalho.github.io/simulabank/login.html")
    return page

@pytest.fixture
def common_page(page):
    return CommonPage(page)

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def home_page(page):
    return HomePage(page)

@pytest.fixture
def pix_page(page):
    return PixPage(page)

@pytest.fixture
def extrato_page(page):
    return ExtratoPage(page)

@pytest.fixture
def emprestimo_page(page):
    return EmprestimoPage(page)
