import string
import json
import uuid
import pytest
from playwright.async_api import Page, Playwright, Browser

def open_codesapce_url(playwright: Playwright, url= "https://github.com/codespaces", storage_path ="./playwright/.auth/state.json"):
    browser = playwright.chromium.launch(headless=False,args=["--start-maximized"])
    context = browser.new_context(storage_state=storage_path, no_viewport=True)
    page = context.new_page()
    page.goto(url)

def connect_the_codesapce_web_client(playwright: Playwright,  url= "https://github.com/codespaces", storage_path ="./playwright/.auth/state.json"):
    browser = playwright.chromium.launch(headless=False,args=["--start-maximized"])
    context = browser.new_context(storage_state=storage_path, no_viewport=True)
    page = context.new_page()
    page.goto(url)
    page.get_by_role("button", name="Codespace configuration").nth(0).click()
    page.get_by_role("menuitem", name="Open in ...").click()
    page.get_by_role("menuitem", name="Open in browser").click()
    # page.wait_for_load_state()
    page.wait_for_timeout(30000)

def connect_the_codesapce_web_client_with_F1(playwright: Playwright, command: string, url= "https://github.com/codespaces", storage_path ="./playwright/.auth/state.json"):
    browser = playwright.chromium.launch(headless=False,args=["--start-maximized"])
    context = browser.new_context(storage_state=storage_path, no_viewport=True)
    page = context.new_page()
    page.goto(url)
    # page.get_by_role("group").filter(has_text="Open in ... Rename Export changes to a branch Change machine type Stop codespace").get_by_role("button", name="Codespace configuration").click()
    page.get_by_role("button", name="Codespace configuration").nth(0).click()
    page.get_by_role("menuitem", name="Open in ...").click()
    page.get_by_role("menuitem", name="Open in browser").click()
    # page.wait_for_load_state()
    page.wait_for_timeout(30000)
    # page.get_by_role("button", name="remote Codespaces").click()
    page.keyboard.press("F1")
    page.get_by_placeholder("Type the name of a command to run.").fill(command)
    page.wait_for_timeout(10000)
    page.keyboard.press("Enter")

    