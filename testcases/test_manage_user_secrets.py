import pytest
from asyncio import sleep
from playwright.sync_api import Page, Playwright, expect
import re
import uuid

@pytest.mark.secrets
def test_add_secret_within_codesapace(playwright : Playwright):
    browser = playwright.chromium.launch(headless=False,args=["--start-maximized"])
    context = browser.new_context(storage_state="./playwright/.auth/state.json",no_viewport=True)
    page = context.new_page()
    page.goto("https://github.com/codespaces")
    # page.get_by_role("group").filter(has_text="Open in ... Rename Export changes to a branch Change machine type Stop codespace").get_by_role("button", name="Codespace configuration").click()
    page.get_by_role("button", name="Codespace configuration").nth(0).click()
    page.get_by_role("menuitem", name="Open in ...").click()
    page.get_by_role("menuitem", name="Open in browser").click()
    page.wait_for_timeout(30000)
    # with page.expect_popup() as page_info:
    #     page.get_by_role("menuitem", name="Open in browser").click()
    #     page.wait_for_timeout(30000)
    # page.wait_for_load_state()
    # page = page_info.value
    page.locator(".monaco-list > .monaco-scrollable-element").nth(0).click()
    page.keyboard.press("F1")
    page.get_by_placeholder("Type the name of a command to run.").fill(">codespace: Manage User Secrets")
    page.keyboard.press("Enter")
    page.wait_for_timeout(1000)
    page.get_by_placeholder("Secrets are environment variables that are encrypted and only exposed to codespaces you create.").fill("Add a new secret")
    # page.keyboard.press("ArrowDown")
    page.keyboard.press("Enter")
    # guid = uuid.uuid4().hex
    page.get_by_role("textbox", name="Enter Secret Name").fill("TESTING")
    page.keyboard.press("Enter")
    page.get_by_role("textbox", name="Enter Secret Value").fill("123456")
    page.keyboard.press("Enter")
    # Page.wait_for_timeout(3000)
    dialog_message = page.locator(".notification-list-item.expanded").filter(has_text="Your codespace secrets have changed.").text_content()
    assert "Your codespace secrets have changed" in dialog_message
    page.get_by_role("button", name="Reload to apply").click()
    page.wait_for_timeout(30000)
    page.locator(".monaco-list > .monaco-scrollable-element").nth(0).click()
    page.keyboard.press("F1")
    page.get_by_placeholder("Type the name of a command to run.").fill(">codespace: Manage User Secrets")
    page.keyboard.press("Enter")
    page.wait_for_timeout(1000)
    page.get_by_placeholder("Secrets are environment variables that are encrypted and only exposed to codespaces you create.").fill("TESTING")
    secret_message = page.get_by_role("option", name=re.compile(".*Added to current repository.*")).text_content()
    assert "TESTING" in secret_message
    # page.get_by_role("textbox", name="Terminal 1, bash\nRun the command: Toggle Screen Reader Accessibility Mode for an optimized screen reader experience\nUse Alt+F1 for terminal accessibility help").fill("echo $TESTING")
    # page.keyboard.press("Enter")
    # terminal_message = page.get_by_role("textbox", name="Terminal 1, bash\nRun the command: Toggle Screen Reader Accessibility Mode for an optimized screen reader experience\nUse Alt+F1 for terminal accessibility help").text_content()
    # ternimal_locator = "#terminal > div > div > div.monaco-scrollable-element > div.split-view-container > div > div > div.pane-body.shell-integration.integrated-terminal.wide > div.monaco-split-view2.horizontal > div.monaco-scrollable-element > div.split-view-container > div > div > div > div > div > div.monaco-scrollable-element > div.split-view-container > div > div > div > div > div > div.xterm-screen > canvas.xterm-cursor-layer"
    # terminal_message = page.locator(ternimal_locator).text_content()
    # assert "123456" in terminal_message
    # print(terminal_message)

