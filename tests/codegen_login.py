import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    page.get_by_role("textbox", name="teste@teste.com").click()
    page.get_by_role("textbox", name="teste@teste.com").fill("novotest@test.com")
    page.get_by_role("textbox", name="Sua senha secreta").click()
    page.get_by_role("textbox", name="Sua senha secreta").fill("senha")
    page.locator("#loginForm").get_by_role("button", name="Entrar").click()
    page.get_by_role("button", name="Italiana").click()
    page.get_by_role("link", name="Restaurante Sabor 0").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)