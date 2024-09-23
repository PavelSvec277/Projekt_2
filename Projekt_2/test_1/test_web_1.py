import pytest
import playwright



def test_idos(page):
     page.goto("https://idos.cz/vlakyautobusymhdvse/spojeni/")
     logo = page.locator(id= "logo")

     assert logo == True