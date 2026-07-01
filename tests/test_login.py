import re
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.home_page import HomePage

HOME_URL = "https://local-eats-unisenac.vercel.app/"


def test_deve_realizar_login_com_sucesso(page):
    # Arrange
    login = LoginPage(page)

    # Act
    login.acessar()
    login.realizar_login("novotest@test.com", "senha")

    # Assert
    expect(page).not_to_have_url(re.compile(r".*login\.html"))
    expect(page.get_by_role("button", name="Italiana")).to_be_visible()


def test_nao_deve_logar_com_campos_vazios(page):
    # Arrange
    login = LoginPage(page)

    # Act
    login.acessar()
    login.submeter()
    # Assert
    expect(page).to_have_url(re.compile(r".*login\.html"))


def test_deve_logar_filtrar_e_abrir_detalhes_do_restaurante(page):
    # Arrange
    login = LoginPage(page)
    home = HomePage(page)

    # Act
    login.acessar()
    login.realizar_login("novotest@test.com", "senha")
    home.filtrar_por_categoria("Italiana")
    home.abrir_restaurante("Restaurante Sabor 0")

    # Assert
    expect(page).not_to_have_url(HOME_URL)