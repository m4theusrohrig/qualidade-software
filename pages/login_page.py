"""
Page Object - Página de Login
LocalEats
"""

URL_LOGIN = "https://local-eats-unisenac.vercel.app/static/login.html"


class LoginPage:
    def __init__(self, page):
        self.page = page
        self.campo_email = page.get_by_role("textbox", name="teste@teste.com")
        self.campo_senha = page.get_by_role("textbox", name="Sua senha secreta")
        self.form_login = page.locator("#loginForm")

    def acessar(self):
        self.page.goto(URL_LOGIN)

    def preencher_email(self, email):
        self.campo_email.fill(email)

    def preencher_senha(self, senha):
        self.campo_senha.fill(senha)

    def submeter(self):
        self.form_login.get_by_role("button", name="Entrar").click()

    def realizar_login(self, email, senha):
        self.preencher_email(email)
        self.preencher_senha(senha)
        self.submeter()