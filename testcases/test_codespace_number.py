
import pytest
from asyncio import sleep
from playwright.sync_api import Page, Playwright, expect
import re

def test_codespace_number(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False,args=["--start-maximized"])
    context = browser.new_context(storage_state="./playwright/.auth/state.json",no_viewport=True)
    page = context.new_page()
    page.goto("https://github.com/codespaces")
    # codeSpaceNumber= page.locator("#item-faf5a532-969b-4150-85e7-74b097cef7de > span.ActionListItem-visual.ActionListItem-visual--trailing > span")
    # codeSpaceNumberText = codeSpaceNumber.text_content()
    # codeSpaceNumberText= page.get_by_role("link",name="All *").text_content()
    element = page.locator(".Counter").first.inner_text()
    # for element in elements:
    #     text = element.innerText()
    #     elementsText = " ".join(text)
    # expect(element).not.toEqual("0")
    assert "0" not in element