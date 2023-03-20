import pytest
from asyncio import sleep
from playwright.sync_api import Page, Playwright, expect
import re
import uuid

@pytest.mark.secrets
def test_terminal_command_window(playwright : Playwright):
    browser = playwright.chromium.launch(headless=False,args=["--start-maximized"])
    context = browser.new_context(storage_state="./playwright/.auth/state.json",no_viewport=True)
    page = context.new_page()
    page.goto("https://github.com/codespaces")
    # page.get_by_role("group").filter(has_text="Open in ... Rename Export changes to a branch Change machine type Stop codespace").get_by_role("button", name="Codespace configuration").click()
    page.get_by_role("button", name="Codespace configuration").nth(0).click()
    page.get_by_role("menuitem", name="Open in ...").click()
    page.get_by_role("menuitem", name="Open in browser").click()
    page.wait_for_timeout(30000)
    # page.get_by_role("textbox", name="Terminal 1, bash\nRun the command: Toggle Screen Reader Accessibility Mode for an optimized screen reader experience\nUse Alt+F1 for terminal accessibility help").fill("git status")
    # page.get_by_role("textbox", name=re.compile("^Terminal.*help$")).fill("git status")
    terminaltextarea =  "#terminal > div > div > div.monaco-scrollable-element > div.split-view-container > div > div > div.pane-body.shell-integration.integrated-terminal.wide > div.monaco-split-view2.horizontal > div.monaco-scrollable-element > div.split-view-container > div > div > div > div > div > div.monaco-scrollable-element > div.split-view-container > div > div > div > div > div > div.xterm-screen > div.xterm-helpers > textarea"
    page.type(terminaltextarea, "clear")
    page.keyboard.press("Enter")
    page.type(terminaltextarea, "git status")
    page.keyboard.press("Enter")
    page.wait_for_timeout(3000)
    # page.get_by_role("textbox", name="Terminal 1, bash\nRun the command: Toggle Screen Reader Accessibility Mode for an optimized screen reader experience\nUse Alt+F1 for terminal accessibility help").fill("git status")
    # page.keyboard.press("Enter")
    # output_locator = "#terminal > div > div > div.monaco-scrollable-element > div.split-view-container > div > div > div.pane-body.shell-integration.integrated-terminal.wide > div.monaco-split-view2.horizontal > div.monaco-scrollable-element > div.split-view-container > div > div > div > div > div > div.monaco-scrollable-element > div.split-view-container > div > div > div > div > div > div.xterm-screen > div.xterm-decoration-container > div.xterm-decoration.codicon.terminal-command-decoration.codicon-terminal-decoration-success"
    page.locator(".xterm-decoration-container > div").first.click()
    page.wait_for_timeout(1000)
    page.get_by_role("menuitem", name="Copy Output",exact=True).click()
    # page.locator(".xterm-decoration-container > div:nth-child(2)").click()
    # page.get_by_role("textbox", name="Terminal 1, bash\nRun the command: Toggle Screen Reader Accessibility Mode for an optimized screen reader experience\nUse Alt+F1 for terminal accessibility help").press("Control+Shift+F")
    # page.get_by_role("textbox", name=re.compile("^Terminal.*help$")).press("Control+Shift+F")
    page.locator(terminaltextarea).press("Control+Shift+F")
    page.keyboard.press("Control+V")
    searchtextarea="#workbench\.view\.search > div > div > div.monaco-scrollable-element > div.split-view-container > div > div > div.pane-body > div.search-view.actions-right > div.search-widgets-container > div.search-widget > div.search-container.input-box > div > div.monaco-scrollable-element > div.monaco-inputbox.idle > div > textarea"
    output_message = page.locator(searchtextarea).input_value()
    assert "On branch main" in output_message