import string
import json
import uuid
import pytest
from playwright.async_api import Page, Playwright, Browser

def create_secret_with_github(playwright: Playwright, url= "https://github.com/codespaces", storage_path ="./playwright/.auth/state.json",secret_name = "TESTING"):
    browser = playwright.chromium.launch(headless=False,args=["--start-maximized"])
    context = browser.new_context(storage_state= storage_path,no_viewport=True)
    page = context.new_page()
    page.goto(url)
    page.get_by_role("button", name="View profile and more").click()
    page.get_by_role("menuitem", name="Settings").click()
    page.wait_for_timeout(2000)
    page.get_by_role("navigation", name="User settings").get_by_role("link", name="Codespaces").click()
    page.get_by_role("button", name="New secret").click()
    guid = uuid.uuid4().hex
    secret_name = secret_name + guid
    page.get_by_placeholder("YOUR_SECRET_NAME").fill(secret_name)
    page.get_by_label("Value").fill(guid)
    page.get_by_role("button", name="Add secret").click()
    

