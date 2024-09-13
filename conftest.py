import pytest
from playwright.sync_api import Page, Playwright


@pytest.fixture() # фикстура с конфигом браузера
def page(context, playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, args=["--start-maximized"], slow_mo=50)
    context = browser.new_context(no_viewport=True)
    page: Page = context.new_page()
    yield page
    browser.close()