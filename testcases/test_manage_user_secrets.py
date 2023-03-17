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
    guid = uuid.uuid4().hex
    secret_name = "TESTING" + guid
    page.get_by_role("textbox", name="Enter Secret Name").fill(secret_name)
    page.keyboard.press("Enter")
    page.get_by_role("textbox", name="Enter Secret Value").fill("123456" + guid)
    page.keyboard.press("Enter")
    # Page.wait_for_timeout(3000)
    dialog_message = page.locator(".notification-list-item.expanded").filter(has_text="Your codespace secrets have changed.").text_content()
    assert "Your codespace secrets have changed" in dialog_message
    page.get_by_role("button", name="Reload to apply").click()
    page.wait_for_timeout(20000)
    page.locator(".monaco-list > .monaco-scrollable-element").nth(0).click()
    page.keyboard.press("F1")
    page.get_by_placeholder("Type the name of a command to run.").fill(">codespace: Manage User Secrets")
    page.keyboard.press("Enter")
    page.wait_for_timeout(1000)
    page.get_by_placeholder("Secrets are environment variables that are encrypted and only exposed to codespaces you create.").fill(secret_name)
    # secret_message = page.get_by_text(re.compile(secret_name)).text_content()
    secret_message = page.get_by_role("option", name=re.compile(".*Added to current repository.*")).nth(0).text_content().strip()
    assert secret_name.lower() in secret_message.lower()
    # issues
    # 1. How to assert the secret in the terminal window

    # page.get_by_role("textbox", name="Terminal 1, bash\nRun the command: Toggle Screen Reader Accessibility Mode for an optimized screen reader experience\nUse Alt+F1 for terminal accessibility help").fill("echo $TESTING")
    # page.keyboard.press("Enter")
    # terminal_message = page.get_by_role("textbox", name="Terminal 1, bash\nRun the command: Toggle Screen Reader Accessibility Mode for an optimized screen reader experience\nUse Alt+F1 for terminal accessibility help").text_content()
    # ternimal_locator = "#terminal > div > div > div.monaco-scrollable-element > div.split-view-container > div > div > div.pane-body.shell-integration.integrated-terminal.wide > div.monaco-split-view2.horizontal > div.monaco-scrollable-element > div.split-view-container > div > div > div > div > div > div.monaco-scrollable-element > div.split-view-container > div > div > div > div > div > div.xterm-screen > canvas.xterm-cursor-layer"
    # terminal_message = page.locator(ternimal_locator).text_content()
    # assert "123456" in terminal_message
    # print(terminal_message)

@pytest.mark.secrets
def test_manage_secret_github(playwright : Playwright):
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
    with page.expect_popup() as codesapce_page_info:
        page.get_by_placeholder("Secrets are environment variables that are encrypted and only exposed to codespaces you create.").fill("Manage on GitHub.com")
        page.wait_for_timeout(1000)
        page.keyboard.press("Enter")
        page.wait_for_timeout(3000)
    codesapcepage = codesapce_page_info.value
    expect(codesapcepage).to_have_url("https://github.com/settings/codespaces")

@pytest.mark.secrets
def test_add_secret_to_current_repo(playwright : Playwright):
    browser = playwright.chromium.launch(headless=False,args=["--start-maximized"])
    context = browser.new_context(storage_state="./playwright/.auth/state.json",no_viewport=True)
    page = context.new_page()
    page.goto("https://github.com/codespaces")
    page.get_by_role("button", name="View profile and more").click()
    page.get_by_role("menuitem", name="Settings").click()
    page.wait_for_timeout(2000)
    page.get_by_role("navigation", name="User settings").get_by_role("link", name="Codespaces").click()
    page.get_by_role("button", name="New secret").click()
    guid = uuid.uuid4().hex
    secret_name = "TESTING" + guid
    # page.get_by_placeholder("YOUR_SECRET_NAME").click()
    page.get_by_placeholder("YOUR_SECRET_NAME").fill(secret_name)
    # page.get_by_label("Value").click()
    page.get_by_label("Value").fill(guid)
    page.get_by_role("button", name="Add secret").click()
    page.get_by_role("navigation", name="Global").get_by_role("link", name="Codespaces").click()
    page.wait_for_timeout(3000)
    page.get_by_role("button", name="Codespace configuration").first.click()
    page.get_by_role("menuitem", name="Open in ...").click()
    page.get_by_role("menuitem", name="Open in browser").click()
    page.wait_for_timeout(30000)
    page.locator(".monaco-list > .monaco-scrollable-element").nth(0).click()
    page.keyboard.press("F1")
    page.get_by_placeholder("Type the name of a command to run.").fill(">codespace: Manage User Secrets")
    page.wait_for_timeout(1000)
    page.keyboard.press("Enter")
    page.get_by_placeholder("Secrets are environment variables that are encrypted and only exposed to codespaces you create.").fill(secret_name)
    page.wait_for_timeout(1000)
    page.keyboard.press("Enter")
    add_secret_info_before = page.get_by_role("option", name="Add this secret to the current repository", exact=True).text_content()
    page.get_by_placeholder("What would you like to do?").fill("Add this secret to the current repository")
    page.keyboard.press("Enter")
    # page.get_by_role("option", name="Add this secret to the current repository", exact=True).click()
    # page.wait_for_timeout(1000)
    dialog_message = page.locator(".notification-list-item.expanded").filter(has_text="Your codespace secrets have changed.").text_content()
    assert "Your codespace secrets have changed" in dialog_message
    page.get_by_role("button", name="Reload to apply").click()
    page.wait_for_timeout(30000)
    page.locator(".monaco-list > .monaco-scrollable-element").nth(0).click()
    page.keyboard.press("F1")
    page.get_by_placeholder("Type the name of a command to run.").fill(">codespace: Manage User Secrets")
    page.wait_for_timeout(1000)
    page.keyboard.press("Enter")
    page.get_by_placeholder("Secrets are environment variables that are encrypted and only exposed to codespaces you create.").fill(secret_name)
    page.wait_for_timeout(1000)
    page.keyboard.press("Enter")
    # add_secret_locator_after = "#list_id_3_1 > div > label > div > div:nth-child(1) > div.monaco-icon-label > div > span.monaco-icon-name-container > a > span"
    # add_secret_info_after = Page.locator(add_secret_locator_after).nth(0).text_content()
    add_secret_info_after = page.get_by_role("option", name="Remove this secret from the current repository", exact=True).text_content()
    # page.get_by_placeholder("What would you like to do?").fill("Add this secret to the current repository")
    assert add_secret_info_before not in add_secret_info_after
    # print(add_secret_info_after, add_secret_info_before)