import pytest
from playwright.sync_api import Page, expect

import data

from pages import HomePage, RequestDemoPage


@pytest.fixture
def home_page(page: Page):
    return HomePage(page)


@pytest.fixture(autouse=True)
def setup(home_page):
    home_page.open()


def test_main_navigation(page: Page):
    expect(page.locator('h2[data-testid="title"]')).to_contain_text("Verification")
