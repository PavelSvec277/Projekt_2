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

@pytest.fixture
def page(context):
    page = context.new_page()
    yield page
    page.close()