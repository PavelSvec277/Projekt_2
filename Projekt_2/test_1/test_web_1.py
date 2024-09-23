import pytest
import playwright

@pytest.fixture()
def browser():

    with playwright():
        

        browser = playwright.chromium.launch(
            headless=False, slow_mo=3000
        )  

        yield browser

        browser.close()

@pytest.fixture()
def page(browser):

    page = browser.new_page()

    yield page

    page.close()

def test_idos(page):
     page.goto("https://idos.cz/vlakyautobusymhdvse/spojeni/")
     logo = page.locator(h1 id= "logo")

     assert logo == True