import pytest

from playwright.sync_api import Page


@pytest.mark.only("chromium")
def test_should_work(page: Page):
    page.goto("https://example.com")
    assert page.title() == "Example Domain"


@pytest.mark.parametrize("url", ["https://example.com", "https://www.bing.com/new"])
def test_should_work_on_multiple_pages(page: Page, url: str):
    page.goto(url)
    assert page.title() != ""


# @pytest.mark.skipif(
#     condition=not pytest.Config.getoption("--headed"),
#     reason="Only works in headed mode",
# )
def test_should_work_in_headed_mode_only(page: Page):
    page.goto("https://example.com")
    assert page.title() == "Example Domain"


@pytest.mark.xfail
def test_should_fail(page: Page):
    page.goto("https://example.com")
    assert page.title() == "Wrong Title"