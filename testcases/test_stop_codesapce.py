import pytest
from asyncio import sleep
from playwright.sync_api import Page, Playwright, expect
import re

@pytest.mark.stop
def test_stop_codespace_from_index_page(playwright : Playwright):
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

@pytest.mark.stop
def test_stop_current_codespace(playwright : Playwright):
    browser = playwright.chromium.launch(headless=False,args=["--start-maximized"])
    context = browser.new_context(storage_state="./playwright/.auth/state.json",no_viewport=True)
    page = context.new_page()
    page.goto("https://github.com/codespaces")
    # page.get_by_role("group").filter(has_text="Open in ... Rename Export changes to a branch Change machine type Stop codespace").get_by_role("button", name="Codespace configuration").click()
    page.get_by_role("button", name="Codespace configuration").nth(0).click()
    page.get_by_role("menuitem", name="Open in ...").click()
    page.get_by_role("menuitem", name="Open in browser").click()
    # page.wait_for_load_state()
    page.wait_for_timeout(30000)
    page.get_by_role("button", name="remote Codespaces").click()
    page.get_by_placeholder("Select an option to open a Remote Window").click()
    page.wait_for_timeout(10000)
    page.get_by_placeholder("Select an option to open a Remote Window").fill("stop current codespace")
    page.keyboard.press("Enter")
    page.wait_for_load_state()
    # page.wait_for_timeout(3000)
    stop_text = page.get_by_role("heading", name="Codespace is stopped").inner_text()
    assert "Codespace is stopped" in stop_text
    # page.get_by_role("option", name="Stop Current Codespace, Codespaces").locator("a").click()
    # stop_locator = page.locator(".static-screen-message")

@pytest.mark.stop
def test_stop_current_codespace_F1(playwright : Playwright):
    browser = playwright.chromium.launch(headless=False,args=["--start-maximized"])
    context = browser.new_context(storage_state="./playwright/.auth/state.json",no_viewport=True)
    page = context.new_page()
    page.goto("https://github.com/codespaces")
    # page.get_by_role("group").filter(has_text="Open in ... Rename Export changes to a branch Change machine type Stop codespace").get_by_role("button", name="Codespace configuration").click()
    page.get_by_role("button", name="Codespace configuration").nth(0).click()
    page.get_by_role("menuitem", name="Open in ...").click()
    page.get_by_role("menuitem", name="Open in browser").click()
    # page.wait_for_load_state()
    page.wait_for_timeout(30000)
    page.locator(".monaco-list > .monaco-scrollable-element").nth(0).click()
    # page.get_by_role("button", name="remote Codespaces").click()
    page.keyboard.press("F1")
    page.get_by_placeholder("Type the name of a command to run.").fill(">codespace: stop current codespace")
    # page.get_by_placeholder("Select an option to open a Remote Window").click()
    page.wait_for_timeout(20000)
    page.keyboard.press("Enter")
    page.wait_for_load_state()
    # page.wait_for_timeout(3000)
    stop_text = page.get_by_role("heading", name="Codespace is stopped").inner_text()
    assert "Codespace is stopped" in stop_text
    # page.get_by_role("option", name="Stop Current Codespace, Codespaces").locator("a").click()
    # stop_locator = page.locator(".static-screen-message")
    
