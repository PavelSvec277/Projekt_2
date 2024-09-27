import pytest
from playwright.sync_api import Page
from Projekt_2.home_page import Home_page



def test_engeto_logo_click(page):
     page.goto("https://engeto.cz/")
     logo = page.locator(f'div.a.class:has-text("logo-link")')
     expect(logo).to_be_visible()
     assert logo.click()