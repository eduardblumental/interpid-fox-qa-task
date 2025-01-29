from playwright.sync_api import Page

from locators import *

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://www.intrepidfox.tech/"
        self.get_demo_button = page.locator(data_testid("linkElement")).nth(0)

    def open(self):
        self.page.goto(self.url)

    def click_get_demo(self):
        self.get_demo_button.click()


class RequestDemoPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.url = f"{super().url}blanc-2"

    def click_get_demo(self):
        self.get_demo_button.click()