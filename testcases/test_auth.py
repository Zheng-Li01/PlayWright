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
    page.locator("id=app_totp").fill("281482")
    # page.get_by_role("button", name="Verify").click()
    # page.close()
    storage = context.storage_state(path="./playwright/.auth/state.json")
    expect(page).to_have_url(re.compile(".*/codespaces"))
    # test_context = page.text_content(".mb-2")
    # assert 'Your codespaces' in test_context
    # assert 'Your codespaces' in page.text_content('h2')

@pytest.mark.rename
def test_rename_codespace(playwright : Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="./playwright/.auth/state.json")
    page = context.new_page()
    page.goto("https://github.com/codespaces")
    page.get_by_role("button", name="Codespace configuration").nth(1).click()
    page.get_by_role("menuitem", name="Rename").click()
    # message  = page.on("dialog", lambda dialog: dialog.accept())
    message1 =page.on("dialog", lambda dialog: dialog.accept())
    message2 = page.on("dialog", lambda dialog: dialog.default_value)
    message3 = page.on("dialog", lambda dialog: dialog.type())
    # message  = page.on("dialog", lambda dialog: print(dialog.message))
    # page.type("RenameCodeSpaceTesting")
    # page.get_by_role("button").click()
    # Will hang here
    # page.wait_for_selector(".modal", state="visible")
    # close_button = page.query_selector(".modal .close")
    # close_button.click()
    # page.wait_for_timeout(3000)
    # page.type("RenameCodeSpaceTest")
    page.close()

@pytest.mark.rename
def test_dailog(playwright : Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="./playwright/.auth/state.json")
    page = context.new_page()
    page.goto("https://github.com/codespaces")
    page.get_by_role("button", name="Codespace configuration").nth(1).click()
    page.get_by_role("menuitem", name="Rename").click() 
    page.on("dialog", lambda dialog: dialog.accept("renameCodeSpaceTestingZhengtesting"))
    sleep(3000)
    page.keyboard.press("Enter")
    # page.evaluate('prompt("hello playwright", "good idea")')

