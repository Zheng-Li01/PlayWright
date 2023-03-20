import string
import json
import uuid
import pytest
from playwright.async_api import Page, Playwright, Browser

def terminal_command_window(page : Page,cmdline: string):
    terminaltextarea="#terminal > div > div > div.monaco-scrollable-element > div.split-view-container > div > div > div.pane-body.shell-integration.integrated-terminal.wide > div.monaco-split-view2.horizontal > div.monaco-scrollable-element > div.split-view-container > div > div > div > div > div > div.monaco-scrollable-element > div.split-view-container > div > div > div > div > div > div.xterm-screen > div.xterm-helpers > textarea"
    page.type(terminaltextarea, cmdline)
    page.keyboard.press("Enter")

def terminal_command_window_copy_command(page : Page, cmdline: string, assertstr:string):
    terminaltextarea="#terminal > div > div > div.monaco-scrollable-element > div.split-view-container > div > div > div.pane-body.shell-integration.integrated-terminal.wide > div.monaco-split-view2.horizontal > div.monaco-scrollable-element > div.split-view-container > div > div > div > div > div > div.monaco-scrollable-element > div.split-view-container > div > div > div > div > div > div.xterm-screen > div.xterm-helpers > textarea"
    page.type(terminaltextarea, cmdline)
    page.keyboard.press("Enter")
    page.wait_for_timeout(3000)
    page.locator(".xterm-decoration-container > div").first.click()
    page.wait_for_timeout(1000)
    page.get_by_role("menuitem", name="Copy Command",exact=True).click()
    page.locator(terminaltextarea).press("Control+Shift+F")
    page.keyboard.press("Control+V")
    searchtextarea="#workbench\.view\.search > div > div > div.monaco-scrollable-element > div.split-view-container > div > div > div.pane-body > div.search-view.actions-right > div.search-widgets-container > div.search-widget > div.search-container.input-box > div > div.monaco-scrollable-element > div.monaco-inputbox.idle > div > textarea"
    copy_command_message = page.locator(searchtextarea).input_value()
    assert assertstr in copy_command_message

def terminal_command_window_copy_output(page : Page, cmdline: string, assertstr:string):
    terminaltextarea="#terminal > div > div > div.monaco-scrollable-element > div.split-view-container > div > div > div.pane-body.shell-integration.integrated-terminal.wide > div.monaco-split-view2.horizontal > div.monaco-scrollable-element > div.split-view-container > div > div > div > div > div > div.monaco-scrollable-element > div.split-view-container > div > div > div > div > div > div.xterm-screen > div.xterm-helpers > textarea"
    page.type(terminaltextarea, cmdline)
    page.keyboard.press("Enter")
    page.wait_for_timeout(3000)
    page.locator(".xterm-decoration-container > div").first.click()
    page.wait_for_timeout(1000)
    page.get_by_role("menuitem", name="Copy Output",exact=True).click()
    page.locator(terminaltextarea).press("Control+Shift+F")
    page.keyboard.press("Control+V")
    searchtextarea="#workbench\.view\.search > div > div > div.monaco-scrollable-element > div.split-view-container > div > div > div.pane-body > div.search-view.actions-right > div.search-widgets-container > div.search-widget > div.search-container.input-box > div > div.monaco-scrollable-element > div.monaco-inputbox.idle > div > textarea"
    output_command_message = page.locator(searchtextarea).input_value()
    assert assertstr in output_command_message