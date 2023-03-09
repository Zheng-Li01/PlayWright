import pytest
from asyncio import sleep
from playwright.sync_api import Page, Playwright, expect
import re

@pytest.mark.stop
def test_stop_codespace(playwright : Playwright):
    browser = playwright.chromium.launch(headless=False,args=["--start-maximized"])
    context = browser.new_context(storage_state="./playwright/.auth/state.json",no_viewport=True)
    page = context.new_page()
    page.goto("https://github.com/codespaces")
    codeSpaceStatusBefore = page.locator("body > div.logged-in.env-production.page-responsive > div.application-main > main > div > div.Layout-main > div:nth-child(4) > div > div.Box-row > div > div:nth-child(2) > div")
    codeSpaceStatustxtBefore = list(filter(None, codeSpaceStatusBefore.nth(0).text_content().replace("\n","").split(" ")))
    # assert "Active" in codeSpaceStatusText
    if "Active" in codeSpaceStatustxtBefore:
        page.get_by_role("button", name="Codespace configuration").nth(0).click()
        page.get_by_role("menuitem", name="Stop codespace").click()
    else:
        print("The codespace status is stopped")
    page.wait_for_timeout(1000)
    # page.close()
    page.goto("https://github.com/codespaces")
    codeSpaceStatusAfter = page.locator("body > div.logged-in.env-production.page-responsive > div.application-main > main > div > div.Layout-main > div:nth-child(4) > div > div.Box-row > div > div:nth-child(2) > div")
    codeSpaceStatustxtAfter = list(filter(None, codeSpaceStatusAfter.nth(0).text_content().replace("\n","").split(" ")))
    assert "Active" not in codeSpaceStatustxtAfter
    # page.keyboard.press("ArrowDown")
    # page.keyboard.press("ArrowDown")
    # page.keyboard.press("ArrowDown")
    # page.keyboard.press("ArrowDown")
    # page.keyboard.press("Enter")
    # page.reload()

    