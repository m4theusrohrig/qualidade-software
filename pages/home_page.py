"""
Page Object - Home (listagem de restaurantes após login)
LocalEats
"""


class HomePage:
    def __init__(self, page):
        self.page = page

    def filtrar_por_categoria(self, categoria):
        self.page.get_by_role("button", name=categoria).click()

    def abrir_restaurante(self, nome):
        self.page.get_by_role("link", name=nome).click()