import pytest
from playwright.sync_api import Playwright, sync_playwright

@pytest.fixture
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=false, slow_mo = 1000)
        yield browser
        browser.close()

@pytest.fixture
def context(browser):
    context = browser.new_content(
        viewport={'width': 1920, 'height': 1080}
    )
    yield context
    context.close()

@pytest.fixture
def page(context):
    page = context.new_page()
    yield page
    page.close()