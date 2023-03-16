import pytest
from asyncio import sleep
from playwright.sync_api import Page, Playwright, expect
import re
import uuid

@pytest.mark.changemachinetype
def test_change_machine_type_codespace_connected_F1(playwright : Playwright):
    browser = playwright.chromium.launch(headless=False,args=["--start-maximized"])
    context = browser.new_context(storage_state="./playwright/.auth/state.json",no_viewport=True)
    page = context.new_page()
    page.goto("https://github.com/codespaces")
    # page.get_by_role("group").filter(has_text="Open in ... Rename Export changes to a branch Change machine type Stop codespace").get_by_role("button", name="Codespace configuration").click()
    page.get_by_role("button", name="Codespace configuration").nth(0).click()
    page.get_by_role("menuitem", name="Open in ...").click()
    page.get_by_role("menuitem", name="Open in browser").click()
    # page.wait_for_load_state()
    page.wait_for_timeout(30000)
    # page.get_by_role("button", name="remote Codespaces").click()
    page.keyboard.press("F1")
    page.get_by_placeholder("Type the name of a command to run.").fill(">codespace: Change Machine Type")
    page.wait_for_timeout(10000)
    page.keyboard.press("Enter")
    machineTypeInfoBefore = page.get_by_role("option", name=re.compile(".*(Current machine type)")).text_content()
    # page.get_by_placeholder("Select an option to open a Remote Window").click()
    page.wait_for_timeout(2000)
    page.keyboard.press("ArrowDown")
    page.keyboard.press("Enter")
    # page.wait_for_load_state()

    dialog_message = page.locator("#monaco-dialog-message-detail").text_content()

    if "Machine type successfully updated and will take effect on the next restart" in dialog_message:
        page.get_by_role("button", name="Yes", exact=True).click()
        page.wait_for_timeout(1000)
        page.get_by_text("Restart codespace").click()
        page.wait_for_timeout(30000)
        page.locator(".monaco-list > .monaco-scrollable-element").nth(0).click()
        page.keyboard.press("F1")
        page.get_by_placeholder("Type the name of a command to run.").fill(">codespace: Change Machine Type")
        page.wait_for_timeout(10000)
        page.keyboard.press("Enter")
        machineTypeInfoAfter= page.get_by_role("option", name=re.compile(".*(Current machine type)")).text_content()
        assert machineTypeInfoBefore not in machineTypeInfoAfter
    elif  "Changing to a machine type with a different amount of storage will require this" in dialog_message:
        page.get_by_role("button", name="Yes", exact=True).click()
        # page.get_by_text("Restart codespace").click()
        page.wait_for_timeout(10000)
        page.wait_for_selector(".static-screen-message", state="attached")
        button_message_first =  page.locator(".container").text_content()
        if "Restart codespace" in button_message_first:
            page.get_by_text("Restart codespace").click()
            status_text = page.get_by_role("heading", name="Codespace is being updated, you will need to wait for a few minutes for the operation to finish").inner_text()
            assert "Codespace is being updated, you will need to wait for a few minutes for the operation to finish" in status_text
            page.wait_for_timeout(600000)# the page will wait for 10 mins, need to find a way to replace this.
            page_current_url = page.url
            page.goto(page_current_url)
            # page.wait_for_timeout(10000)
            page.wait_for_selector(".static-screen-message", state="attached")
            # page.wait_for_selector(".static-screen-message",state="detached")
            button_message_second =  page.locator(".container").text_content()
            if "Restart codespace" in button_message_second:
                page.get_by_text("Restart codespace").click()
            if "Try again" in button_message_second:
                page.get_by_text("Try again").click()
        elif "Try again" in button_message_first:
            status_text = page.get_by_role("heading", name="Codespace is being updated, you will need to wait for a few minutes for the operation to finish").inner_text()
            assert "Codespace is being updated, you will need to wait for a few minutes for the operation to finish" in status_text
            page.wait_for_timeout(600000)
            page_current_url = page.url
            page.goto(page_current_url)
            # page.wait_for_timeout(10000)
            page.wait_for_selector(".static-screen-message", state="attached")
            button_message_third =  page.locator(".container").text_content()
            if "Restart codespace" in button_message_third:
                page.get_by_text("Restart codespace").click()
            if "Try again" in button_message_third:
                page.get_by_text("Try again").click()      
        page.wait_for_timeout(30000)
        page.locator(".monaco-list > .monaco-scrollable-element").nth(0).click()
        page.keyboard.press("F1")
        page.get_by_placeholder("Type the name of a command to run.").fill(">codespace: Change Machine Type")
        page.wait_for_timeout(10000)
        page.keyboard.press("Enter")
        machineTypeInfoAfter= page.get_by_role("option", name=re.compile(".*(Current machine type)")).text_content()
        assert machineTypeInfoBefore not in machineTypeInfoAfter
        
    else:
        print("Have change the machine type successfully")


@pytest.mark.changemachinetype
def test_change_machine_type_codespace_disconnected(playwright : Playwright):
    browser = playwright.chromium.launch(headless=False,args=["--start-maximized"])
    context = browser.new_context(storage_state="./playwright/.auth/state.json",no_viewport=True)
    page = context.new_page()
    page.goto("https://github.com/codespaces")
    page.get_by_role("button", name="Codespace configuration").first.click()
    machine_type_info_before = page.get_by_text(re.compile(".*-core")).first.text_content().replace("\n","").strip()
    page.get_by_role("menuitem", name="Change machine type").click()
    page.wait_for_timeout(1000)
    # all_machine_type_info = page.locator("label").filter(has_text=re.compile(".*-core.*")).all_text_contents()
    # all_machine_type_info1= list(filter(lambda x: x.replace("\n","").strip(), all_machine_type_info))
    # print(all_machine_type_info1)
    # for machine_type_info in all_machine_type_info:
    if "2-core" in machine_type_info_before:
        page.locator("label").filter(has_text=machine_type_info_before).click()
        page.keyboard.press("ArrowDown")
        page.get_by_role("button", name="Update codespace").click()
            # break
        alert_message = page.get_by_text(re.compile(".*Changes will take effect the next time your codespace restarts")).text_content()
        assert "Changes will take effect the next time your codespace restarts" in alert_message
        machine_type_info_after = page.get_by_text(re.compile(".*-core")).first.text_content().replace("\n","").strip()
        assert machine_type_info_after not in machine_type_info_before
    # print(machine_type_info_after, machine_type_info_before)
    else:
        list_machine_type_info = ["4-core","8-core","16-core"]
        for machine_type_info in list_machine_type_info:
            if machine_type_info in machine_type_info_before:
                page.locator("label").filter(has_text=machine_type_info).click()
                page.keyboard.press("ArrowDown")
                page.get_by_role("button", name="Update codespace").click()
                alert_message = page.get_by_text(re.compile(".*Your codespace will be stopped and unavailable during the update")).text_content()
                assert "Your codespace will be stopped and unavailable during the update" in alert_message
                page.wait_for_timeout(600000)
                page_current_url = page.url
                page.goto(page_current_url)
                machine_type_info_after = page.get_by_text(re.compile(".*-core")).first.text_content().replace("\n","").strip()
                assert machine_type_info_after not in machine_type_info_before
                break
                # print(machine_type_info_before, machine_type_info_after)

    
