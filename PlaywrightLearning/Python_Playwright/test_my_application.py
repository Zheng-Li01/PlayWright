from playwright.sync_api import sync_playwright

def run(playwright):
    chromium = playwright.chromium
    browser = chromium.launch()
    page = browser.new_page()
    # Subscribe to "request" and "response" events.
    page.on("request", lambda request: print(">>", request.method, request.url))
    page.on("response", lambda response: print("<<", response.status, response.url))
    page.goto("https://example.com")
    browser.close()

with sync_playwright() as playwright:
    run(playwright)

#  import asyncio
# from playwright.async_api import async_playwright

# async def main():
#     async with async_playwright() as p:
#         browser = await p.chromium.launch()
#         page = await browser.new_page()
#         await page.goto("http://playwright.dev")
#         print(await page.title())
#         await browser.close()

# asyncio.run(main())

# from pydoc import pager
# import re
# import unittest
# from ast import Yield
# from typing import Dict
# import pytest
# from playwright.sync_api import Browser, BrowserType, Page, expect, sync_playwright
# import asyncio


# with sync_playwright() as p:
#     browser = p.chromium.launch()
#     page = browser.new_page()
#     page.goto("http://playwright.dev")
#     print(page.title())
#     browser.close()
# class MyTest(unittest.TestCase):
#     @pytest.fixture(autouse=True)
#     def setup(self, page: Page):
#         self.page = page

#     def test_foobar(self):
#         self.page.goto("https://microsoft.com")
#         breakpoint()
#         self.page.locator("#foobar").click()
#         assert self.page.evaluate("1 + 1") == 2
        
        
# @pytest.fixture(scope="session")
# def context(
#     browser_type: BrowserType,
#     browser_type_launch_args: Dict,
#     browser_context_args: Dict
# ):
#     context = browser_type.launch_persistent_context("./foobar", **{
#         **browser_type_launch_args,
#         **browser_context_args,
#         "locale":"de-DE"
#     })
#     yield context
#     context.close()

# @pytest.fixture(scope="session")
# def browser_context_args(browser_context_args, playwright):
#     iphone_11 = playwright.devices["iPhone 11 Pro"]
#     return{
#         **browser_context_args,
#         **iphone_11,
#     }
    
# @pytest.mark.skip('firefox')
# @pytest.mark.usefixtures()
# @pytest.fixture(scope="session")
# def  test_homepage(page: Page):
#     page.goto("https://playwright.dev/")

#     expect(page).to_have_title(re.compile("Playwright"))

#     get_started = page.locator("text= Get Started")
#     expect(get_started).to_have_attribute("href","/docs/intro")

#     get_started.click()

#     expect(page).to_have_url(re.compile(".*intro"))

#     context = Browser.new_context()
