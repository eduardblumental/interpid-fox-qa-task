import pytest
from playwright.sync_api import Page, expect

import data


@pytest.fixture(scope="function", autouse=True)
def setup(page: Page):
    page.goto("https://www.intrepidfox.tech/")
    page.locator('[data-testid="linkElement"]').nth(0).click()
    page.locator('[placeholder="Name"]').fill(test_data.name)
    page.locator('[placeholder="Email"]').fill(test_data.email)
    page.locator('[placeholder="Message"]').fill(test_data.msg)
    page.locator('[data-hook="icon-wrapper"]').click()
    page.locator('[data-hook="submit-button"]').click()
    page.locator('[data-testid="title"]')


def test_main_navigation(page: Page):
    expect(page.locator('h2[data-testid="title"]')).to_contain_text("Verification")
