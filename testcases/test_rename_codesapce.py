import pytest
from asyncio import sleep
from playwright.sync_api import Page, Playwright, expect
import re

@pytest.mark.rename
def test_rename_codespace(playwright : Playwright):
    browser = playwright.chromium.launch(headless=False,args=["--start-maximized"])
    context = browser.new_context(storage_state="./playwright/.auth/state.json",no_viewport=True)
    page = context.new_page()
    page.goto("https://github.com/codespaces")
    page.get_by_role("button", name="Codespace configuration").nth(0).click()
    page.get_by_role("menuitem", name="Rename").click()
    # page.keyboard.press("ArrowDown")
    # page.keyboard.press("ArrowDown")
    # page.keyboard.press("Enter")
    page.on("dialog", lambda dialog:dialog.accept("CodeSpaceRenameTesting"))
    page.keyboard.press("Enter")
    page.wait_for_timeout(1000)
    # codeSpaceRenameLocator = page.locator("body > div.logged-in.env-production.page-responsive > div.application-main > main > div > div.Layout-main > div:nth-child(4) > div > div.Box-row > div > div:nth-child(1) > div:nth-child(2) > div")
    # codeSpaceRenameText=codeSpaceRenameLocator.nth(0).text_content().replace("\n","").strip()
    # assert "CodeSpaceRenameTesting" in codeSpaceRenameText