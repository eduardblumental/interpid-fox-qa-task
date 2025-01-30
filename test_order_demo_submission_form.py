import pytest
from playwright.sync_api import Page, expect

import data

from pages import HomePage, RequestDemoPage


@pytest.fixture
def home_page(page: Page):
    return HomePage(page)


@pytest.fixture
def request_demo_page(page: Page):
    return RequestDemoPage(page)


def test_order_demo_submission_form(home_page, request_demo_page):
    home_page.open().click_get_demo()
    expect(home_page.page, f"Wrong request demo page url.").to_have_url(request_demo_page.url)

    request_demo_page.fill_order_demo_form(data.name, data.email, data.msg).tick_checkbox().submit_form()
    expect(request_demo_page.captcha_dialog, f"Captcha dialog is not visible.").to_be_visible()
