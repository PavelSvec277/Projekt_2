import pytest

from playwright.sync_api import sync_playwright

@pytest.fixture()
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
            )
        yield browser
        browser.close()

@pytest.fixture()
def page(browser):

    page = browser.new_page()
    browser.window={'width': 1920, 'height': 1080}

    yield page
    page.close()


def test_engeto_cookies(page):
    page.goto("https://engeto.cz/")
    button = page.locator("#cookiescript_accept")
    button.click()

def test_engeto_logo(page):
    page.goto("https://engeto.cz/")
    button = page.locator("#cookiescript_accept")
    button.click()
    logo = page.locator('#logo')
     
    assert logo.is_visible()

def test_zobrazit_terminy_kurzu_click(page):
    page.goto("https://engeto.cz/")
    button = page.locator("#cookiescript_accept")
    button.click()

    button_terminy = page.locator('div.block-button:has-text("Zobrazit termíny kurzů")')
    button_terminy.click()

def test_engeto_kontakt_click(page):
    page.goto("https://engeto.cz/")
    button = page.locator("#cookiescript_accept")
    button.click()
    
    button_kontakt = page.locator('div.contact-link.h6.is_bold_700:has-text("Kontakt")')
    button_kontakt.click()
    