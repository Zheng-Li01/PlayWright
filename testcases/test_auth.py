import pytest
from asyncio import sleep
from playwright.sync_api import Page, Playwright, expect
import re

@pytest.mark.loginpage
def test_login_codespace(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://github.com/codespaces")
    # Interact with login form
    page.get_by_label("Username or email address").fill("m18629016454@163.com")
    page.get_by_label("Password").fill("Lz@936548")
    page.get_by_role("button", name="Sign in").click()
    expect(page).to_have_url(re.compile(".*two-factor/app"))
    page.locator("id=app_totp").fill("007513")
    # page.get_by_role("button", name="Verify").click()
    # page.close()
    storage = context.storage_state(path="./playwright/.auth/state.json")
    expect(page).to_have_url(re.compile(".*/codespaces"))
    

