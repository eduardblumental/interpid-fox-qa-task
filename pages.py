from playwright.sync_api import Page

from locators import data_hook, data_testid, placeholder

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://www.intrepidfox.tech/"
        self.get_demo_button = page.locator(data_testid("linkElement")).nth(0)

    def open(self):
        self.page.goto(self.url)

    def click_get_demo(self):
        self.get_demo_button.click()


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)


class RequestDemoPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.url = f"{super().url}blanc-2"

        self.name = page.locator(placeholder("Name"))
        self.email = page.locator(placeholder("Email"))
        self.msg = page.locator(placeholder("Message"))
        self.checkbox = page.locator(data_hook("checkbox-wrapper"))
        self.submit_button = page.locator(data_hook("submit-button"))
        self.verification = page.locator(data_testid("title"))

    def fill_order_demo_form(self, name, email, msg):
        self.name.fill(name)
        self.email.fill(email)
        self.msg.fill(msg)
        return self

    def tick_checkbox(self):
        self.checkbox.click()
        return self

    def submit_form(self):
        self.submit_button.click()
        return self
