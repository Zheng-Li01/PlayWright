import pytest
from asyncio import sleep
from playwright.sync_api import Page, Playwright, expect
import re
import uuid

@pytest.mark.prebuild
def test_prebuild_with_vscode_repo(playwright : Playwright):
    browser = playwright.chromium.launch(headless=False,args=["--start-maximized"])
    context = browser.new_context(storage_state="./playwright/.auth/state.json",no_viewport=True)
    page = context.new_page()
    page.goto("https://github.com/microsoft/vscode")
    page.wait_for_timeout(3000)
    page.locator("summary").filter(has_text="Code").click()
    page.get_by_role("tab", name="Codespaces").click()
    with page.expect_popup() as new_page_info:
        page.get_by_role("button", name="Create codespace on main").click()
        page.wait_for_timeout(30000)
    new_page = new_page_info.value
    new_page.wait_for_timeout(30000)
    terminaltextarea =  "#terminal > div > div > div.monaco-scrollable-element > div.split-view-container > div > div > div.pane-body.shell-integration.integrated-terminal.wide > div.monaco-split-view2.horizontal > div.monaco-scrollable-element > div.split-view-container > div > div > div > div > div > div.monaco-scrollable-element > div.split-view-container > div > div > div > div > div > div.xterm-screen > div.xterm-helpers > textarea"
    new_page.type(terminaltextarea,"clear")
    new_page.keyboard.press("Enter")

    new_page.type(terminaltextarea, "cat /workspaces/.codespaces/shared/environment-variables.json | jq '.ACTION_NAME'")
    new_page.keyboard.press("Enter")
    new_page.wait_for_timeout(3000)
    new_page.locator(".xterm-decoration-container > div").first.click()
    new_page.wait_for_timeout(1000)
    new_page.get_by_role("menuitem", name="Copy Output",exact=True).click()
    new_page.locator(terminaltextarea).press("Control+Shift+F")
    new_page.keyboard.press("Control+V")
    searchtextarea="#workbench\.view\.search > div > div > div.monaco-scrollable-element > div.split-view-container > div > div > div.pane-body > div.search-view.actions-right > div.search-widgets-container > div.search-widget > div.search-container.input-box > div > div.monaco-scrollable-element > div.monaco-inputbox.idle > div > textarea"
    output_message = new_page.locator(searchtextarea).input_value()
    assert "createFromPrebuild" in output_message