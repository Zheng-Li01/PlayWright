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
    page.get_by_role("button", name="Codespace configuration").nth(0).click()
    page.get_by_role("menuitem", name="Rename").click()
    # page.keyboard.press("ArrowDown")
    # page.keyboard.press("ArrowDown")
    # page.keyboard.press("Enter")
    # page.on("dialog", lambda dialog:dialog.accept("CodeSpaceRenameTesting"))
    # page.keyboard.press("Enter")
    # codeSpaceRenameLocator = page.locator("body > div.logged-in.env-production.page-responsive > div.application-main > main > div > div.Layout-main > div:nth-child(4) > div > div:nth-child(2) > div > div:nth-child(1) > div:nth-child(2) > div > a")
    # codeSpaceRenameText = codeSpaceRenameLocator.text_content()
    # assert "CodeSpaceRenameTesting" in codeSpaceRenameText
  
    
@pytest.mark.delete
def test_delete_codespace(playwright : Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="./playwright/.auth/state.json")
    page = context.new_page()
    page.goto("https://github.com/codespaces")
    page.get_by_role("button", name="Codespace configuration").nth(0).click()
    page.get_by_role("menuitem", name="Delete codespace CodeSpaceRename").click()
    # page.keyboard.press("ArrowDown")
    # page.keyboard.press("ArrowDown")
    # page.keyboard.press("ArrowDown")
    # page.keyboard.press("ArrowDown")
    # page.keyboard.press("ArrowDown")
    # page.keyboard.press("Enter")
    page.on("dialog", lambda dialog: dialog.accept())
    page.keyboard.press("Enter")
    # page.reload()

@pytest.mark.stop
def test_stop_codespace(playwright : Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="./playwright/.auth/state.json")
    page = context.new_page()
    page.goto("https://github.com/codespaces")
    codeSpaceStatus = page.locator("body > div.logged-in.env-production.page-responsive > div.application-main > main > div > div.Layout-main > div:nth-child(4) > div > div.Box-row > div > div:nth-child(2) > div")
    # codeSpaceStatusText = codeSpaceStatus.text_content()
    # assert "Active" in codeSpaceStatusText
    if "Active" in codeSpaceStatus.text_content():
        page.get_by_role("button", name="Codespace configuration").nth(0).click()
        page.get_by_role("menuitem", name="Stop codespace").click()
    else:
        "The codesapce has been stoped"
    # page.keyboard.press("ArrowDown")
    # page.keyboard.press("ArrowDown")
    # page.keyboard.press("ArrowDown")
    # page.keyboard.press("ArrowDown")
    # page.keyboard.press("Enter")
    page.reload()


