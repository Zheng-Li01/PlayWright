import pytest
from asyncio import sleep
from playwright.sync_api import Page, Playwright, expect
import re

@pytest.mark.delete
def test_delete_codespace(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False,args=["--start-maximized"])
    context = browser.new_context(storage_state="./playwright/.auth/state.json", no_viewport=True)
    page = context.new_page()
    page.goto("https://github.com/codespaces")
    codeSpaceStatus = page.locator("body > div.logged-in.env-production.page-responsive > div.application-main > main > div > div.Layout-main > div:nth-child(4) > div > div.Box-row > div > div:nth-child(2) > div")
    if "Active" in codeSpaceStatus.nth(0).text_content():
        delete_codespace_withActive(playwright)
    else:
        delete_codespace_withStoped(playwright)

@pytest.mark.delete
def delete_codespace_withActive(playwright : Playwright):
    browser = playwright.chromium.launch(headless=False,args=["--start-maximized"])
    context = browser.new_context(storage_state="./playwright/.auth/state.json", no_viewport=True)
    page = context.new_page()
    page.goto("https://github.com/codespaces")
    page.get_by_role("button", name="Codespace configuration").nth(0).click()
    codeSpaceNameLocatorBefore = page.locator("body > div.logged-in.env-production.page-responsive > div.application-main > main > div > div.Layout-main > div:nth-child(4) > div > div.Box-row > div > div:nth-child(1) > div:nth-child(2) > div")
    codeSpaceNametextBefore = codeSpaceNameLocatorBefore.nth(0).text_content().replace("\n","").strip()
    page.keyboard.press("ArrowDown")
    page.keyboard.press("ArrowDown")
    page.keyboard.press("ArrowDown")
    page.keyboard.press("ArrowDown")
    page.keyboard.press("ArrowDown")
    page.keyboard.press("ArrowDown")
    page.keyboard.press("Enter")
    # page.get_by_role("menuitem", name="Delete codespace CodeSpaceRename").click()
    page.on("dialog", lambda dialog: dialog.accept())
    page.keyboard.press("Enter")
    page.wait_for_timeout(1000)
    # page.close()
    page.goto("https://github.com/codespaces")
    # codeSpaceNameLocatorAfter = page.locator("body > div.logged-in.env-production.page-responsive > div.application-main > main > div > div.Layout-main > div:nth-child(4) > div > div.Box-row > div > div:nth-child(1) > div:nth-child(2) > div")
    # codeSpaceNametextAfter=codeSpaceNameLocatorAfter.nth(0).text_content().replace("\n","").strip()
    codeSpaceNameLocatorAfter = page.locator("body > div.logged-in.env-production.page-responsive > div.application-main > main > div > div.Layout-main > div:nth-child(4) > div")
    codeSpaceNametextAfter=codeSpaceNameLocatorAfter.text_content().replace("\n","").replace(" ","'").strip()
    assert codeSpaceNametextBefore not in codeSpaceNametextAfter

@pytest.mark.delete
def delete_codespace_withStoped(playwright : Playwright):
    browser = playwright.chromium.launch(headless=False,args=["--start-maximized"])
    context = browser.new_context(storage_state="./playwright/.auth/state.json", no_viewport=True)
    page = context.new_page()
    page.goto("https://github.com/codespaces")
    page.get_by_role("button", name="Codespace configuration").nth(0).click()
    codeSpaceNameLocatorBefore = page.locator("body > div.logged-in.env-production.page-responsive > div.application-main > main > div > div.Layout-main > div:nth-child(4) > div > div.Box-row > div > div:nth-child(1) > div:nth-child(2) > div")
    codeSpaceNametextBefore = codeSpaceNameLocatorBefore.nth(0).text_content().replace("\n","").strip()
    page.keyboard.press("ArrowDown")
    page.keyboard.press("ArrowDown")
    page.keyboard.press("ArrowDown")
    page.keyboard.press("ArrowDown")
    page.keyboard.press("ArrowDown")
    page.keyboard.press("Enter")
    # page.get_by_role("menuitem", name="Delete codespace CodeSpaceRename").click()
    page.on("dialog", lambda dialog: dialog.accept())
    page.keyboard.press("Enter")
    page.wait_for_timeout(3000)
    # page.close()
    page.goto("https://github.com/codespaces")
    # codeSpaceNameLocatorAfter = page.locator("body > div.logged-in.env-production.page-responsive > div.application-main > main > div > div.Layout-main > div:nth-child(4) > div > div.Box-row > div > div:nth-child(1) > div:nth-child(2) > div")
    # codeSpaceNametextAfter=codeSpaceNameLocatorAfter.nth(0).text_content().replace("\n","").strip()
    codeSpaceNameLocatorAfter = page.locator("body > div.logged-in.env-production.page-responsive > div.application-main > main > div > div.Layout-main > div:nth-child(4) > div")
    codeSpaceNametextAfter=codeSpaceNameLocatorAfter.text_content().replace("\n","").replace(" ","'").strip()
    assert codeSpaceNametextBefore not in codeSpaceNametextAfter
    # assert codeSpaceNametextBefore in codeSpaceNametextAfter
    # expect(codeSpaceNametextAfter).not_to_contain_text(codeSpaceNametextBefore)