import pytest
from playwright.sync_api import Page
from home_page import Home_page


@pytest.mark.playwright
def test_engeto_logo_click(page):
     page.goto("https://engeto.cz/")
     logo = page.locator(f'div.a:has-text("{"logo-link"}")')
     
     assert logo.click()