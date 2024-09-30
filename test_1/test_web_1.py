import pytest

from playwright.sync_api import sync_playwright

@pytest.fixture()
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False, slow_mo=6000
            )
        yield browser
        browser.close()

@pytest.fixture()
def page(browser):

    page = browser.new_page()
    browser.window={'width': 1920, 'height': 1080}

    yield page
    page.close()

def test_google_search(page):
    page.goto("https://www.google.com/")

    button = page.locator("#W0wltc")
    button.click()

    textarea = page.locator("#APjFqb")
    textarea.fill("engeto")

def test_engeto_logo_click(page):
     page.goto("https://engeto.cz/")
     logo = page.locator('div.logo-link')
     
     assert logo.click()