import re

from pytest_bdd import scenarios, given, when, then, parsers
from playwright.sync_api import expect

scenarios('../features/navegacao_paginas.feature')

URL_LOGIN = "https://local-eats-unisenac.vercel.app/static/login.html"

PAGINAS = {
    "Explorar": {
        "url_contem": "index.html",
    },
    "Meus Favoritos": {
        "url_contem": "profile.html",
    },
    "Meus Pedidos": {
        "url_contem": "orders.html",
    },
}


@given('que o usuário está autenticado na página inicial do LocalEats')
def acessar_pagina_autenticado(page):
    page.goto(URL_LOGIN)
    page.get_by_role("textbox", name="teste@teste.com").click()
    page.get_by_role("textbox", name="teste@teste.com").fill("novo@teste.com")
    page.get_by_role("textbox", name="Sua senha secreta").click()
    page.get_by_role("textbox", name="Sua senha secreta").fill("teste")
    page.locator("#loginForm").get_by_role("button", name="Entrar").click()
    page.get_by_role("link", name="Explorar").wait_for()


@given(parsers.parse('ele navegou até a página de "{pagina}"'))
def navegar_previamente(page, pagina):
    page.get_by_role("link", name=pagina, exact=True).click()
    url_esperada = PAGINAS[pagina]["url_contem"]
    expect(page).to_have_url(re.compile(url_esperada), timeout=10000)


@when(parsers.parse('ele clica no link "{pagina}"'))
def clicar_no_link(page, pagina):
    page.get_by_role("link", name=pagina, exact=True).click()


@then(parsers.parse('a página de "{pagina}" deve carregar corretamente'))
def validar_pagina_carregada(page, pagina):
    url_esperada = PAGINAS[pagina]["url_contem"]
    expect(page).to_have_url(re.compile(url_esperada), timeout=10000)
    expect(page.get_by_role("link", name="Explorar")).to_be_visible()
    expect(page.get_by_role("heading").first).to_be_visible()