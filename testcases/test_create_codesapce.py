import pytest
from asyncio import sleep
from playwright.sync_api import Page, Playwright, expect
import re
import uuid

@pytest.mark.blanktemplate
def test_blank_template_codespace(playwright : Playwright):
    browser = playwright.chromium.launch(headless=False,args=["--start-maximized"])
    context = browser.new_context(storage_state="./playwright/.auth/state.json",no_viewport=True)
    page = context.new_page()
    page.goto("https://github.com/codespaces")
    with page.expect_popup() as new_page_info:
        page.get_by_role("listitem").filter(has_text="Blank By github Start with a blank canvas or import any packages you need. Use t").get_by_role("button", name="Use this template").click()
        page.wait_for_timeout(30000)
    new_page_value = new_page_info.value
    # terminalTetx= new_page_value.get_by_role("generic", name=re.compile("Terminal.*")).text_content()
    new_page_value.locator(".monaco-list > .monaco-scrollable-element").nth(0).click()
    new_page_value.get_by_role("button", name="New File...").click()
    # page.get_by_role("textbox", name="Type file name. Press Enter to confirm or Escape to cancel.").click()
    guid = uuid.uuid4().hex
    new_page_value.get_by_role("textbox", name="Type file name. Press Enter to confirm or Escape to cancel.").fill("codesapce" + guid + ".html")
    new_page_value.keyboard.press("Enter")
    # page.locator(".editor-group-container").click()
    # new_page_value.get_by_role("textbox", name="codesapce.html" + guid).fill("test")
    new_page_value.get_by_role("textbox", name=re.compile("codesapce.*\.html")).fill("test")
    new_page_value.press("body", "Control+s")
    new_page_value.press("body", "Control+Shift+G")
    publish_github_button = "#workbench\.view\.scm > div > div > div.monaco-scrollable-element > div.split-view-container > div > div > div.pane-body.welcome > div.welcome-view > div > div.welcome-view-content > div > a > span:nth-child(2)"
    new_page_value.locator(publish_github_button).click()
    # new_page_value.get_by_role("button", name=re.compile("*. Publish to GitHub")).click()
    guid = uuid.uuid4().hex
    new_page_value.get_by_role("combobox", name= "Repository Name").fill("codesapceTesting_" + guid)
    new_page_value.wait_for_timeout(1000)
    new_page_value.keyboard.press("ArrowDown")
    # new_page_value.keyboard.press("ArrowDown")
    new_page_value.keyboard.press("Enter")
    new_page_value.get_by_role("button", name="OK").click()
    # new_page_value.keyboard.press("Enter")
    page.wait_for_timeout(3000)
    # new_page_value.go_back()
    success_locator = "#list_id_9_0 > div.notification-list-item.expanded > div.notification-list-item-main-row > div.notification-list-item-message > span"
    success_info = new_page_value.locator(success_locator).text_content()
    assert "Successfully published" in success_info

@pytest.mark.repotemplate
def test_repo_template_codespace(playwright : Playwright):
    browser = playwright.chromium.launch(headless=False,args=["--start-maximized"])
    context = browser.new_context(storage_state="./playwright/.auth/state.json",no_viewport=True)
    page = context.new_page()
    page.goto("https://github.com/codespaces")
    with page.expect_popup() as new_page_info:
        page.get_by_role("link", name="New codespace").click()
        # page.wait_for_timeout(30000)
    new_page_value = new_page_info.value
    new_page_value.get_by_role("button", name="Select a repository").click()
    new_page_value.wait_for_timeout(1000)
    new_page_value.keyboard.press("ArrowDown")
    new_page_value.keyboard.press("ArrowDown")
    new_page_value.keyboard.press("Enter")
    # with new_page_value.expect_popup() as new_page_info1:
    #     new_page_value.get_by_role("button", name="Create codespace").click()
    #     new_page_value.wait_for_timeout(10000)
    new_page_value.get_by_role("button", name="Create codespace").click()
    # new_page_value.wait_for_load_state()
    new_page_value.wait_for_timeout(40000)
    # new_page_value.get_by_role("tree", name="Files Explorer").focus()
    # new_page_value.get_by_role("tree", name="Files Explorer").click()
    new_page_value.locator(".monaco-list > .monaco-scrollable-element").first.click()
    new_page_value.get_by_role("button", name="New File...").click()
    # new_page_value.pause()
    # page.get_by_role("textbox", name="Type file name. Press Enter to confirm or Escape to cancel.").click()
    guid = uuid.uuid4().hex
    new_page_value.get_by_role("textbox", name="Type file name. Press Enter to confirm or Escape to cancel.").fill("codesapce" + guid + ".html")
    new_page_value.keyboard.press("Enter")
    # page.locator(".editor-group-container").click()
    new_page_value.get_by_role("textbox", name=re.compile("codesapce.*\.html")).fill("test")
    new_page_value.get_by_role("textbox").filter()
    new_page_value.press("body", "Control+s")
    new_page_value.get_by_role("textbox", name="Terminal 1, bash\nRun the command: Toggle Screen Reader Accessibility Mode for an optimized screen reader experience\nUse Alt+F1 for terminal accessibility help").fill("git add .")
    new_page_value.keyboard.press("Enter")
    new_page_value.wait_for_timeout(1000)
    new_page_value.get_by_role("textbox", name="Terminal 1, bash\nRun the command: Toggle Screen Reader Accessibility Mode for an optimized screen reader experience\nUse Alt+F1 for terminal accessibility help").fill('git commit -m "just for testing"')
    new_page_value.keyboard.press("Enter")
    new_page_value.wait_for_timeout(1000)
    new_page_value.get_by_role("textbox", name="Terminal 1, bash\nRun the command: Toggle Screen Reader Accessibility Mode for an optimized screen reader experience\nUse Alt+F1 for terminal accessibility help").fill("git push")
    new_page_value.keyboard.press("Enter")
    new_page_value.wait_for_timeout(3000)
    # new_page_value.go_back()
    # success_locator = "#list_id_9_0 > div.notification-list-item.expanded > div.notification-list-item-main-row > div.notification-list-item-message > span"
    # success_info = new_page_value.locator(success_locator).text_content()
    # assert "Successfully published" in success_info

@pytest.mark.secrets
def test_update_add_secret_to_current_repo(playwright : Playwright):
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
    add_secret_info_before = page.get_by_role("option", name="Update the value and add this secret to the current repository", exact=True).text_content()
    page.get_by_placeholder("What would you like to do?").fill("Update the value and add this secret to the current repository")
    page.keyboard.press("Enter")
    page.wait_for_timeout(1000)
    page.get_by_role("textbox", name="Enter Secret Value").fill("update" + guid)
    page.keyboard.press("Enter")
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
    add_secret_info_after = page.get_by_role("option", name="Remove this secret from the current repository", exact=True).text_content()
    assert add_secret_info_before not in add_secret_info_after