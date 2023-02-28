import re
from time import sleep

from playwright.sync_api import Page, expect, sync_playwright


# https://blog.csdn.net/u010698107/article/details/121070094
def test_text(page : Page):
    page.goto("https://www.baidu.com/")
    # page.click('text="百度一下"')
    page.click('"百度一下"')
    page.close()

def test_id(page: Page):
    page.goto("https://www.baidu.com/")
    page.fill("id=kw","test")
    page.fill('css=[id="kw"]',"test")
    page.fill('css=[class="s_ipt"]',"test")
    page.fill('css=[name="wd"]',"test")
    page.click("id=su")
    
def test_xpath(page: Page):
    page.goto("https://www.baidu.com/")
    page.click('//*[@id="s-top-left"]//a[2]')

def test_css(page: Page):
    page.goto("https://www.baidu.com/")
    page.click("#s-top-left a:nth-child(2) +a")
    # page.click("button:visble")
    # page.click("button >> visble = true")

def test_has(page: Page):
    page.goto("https://www.baidu.com/")
    page.click("#s-top-left:has(a) > a:nth-child(2)")

def test_is(page: Page):
    page.goto("https://www.baidu.com/")
    page.click(':is(a:has-text("新闻"))')

# def test_right_of(page: Page):
#     page.goto("https://www.baidu.com/")
#     page.click("input:right-of(#kw)")

def test_zuhe(page: Page):
    page.goto("https://www.baidu.com/")
    # page.click('css=[class="bg s_btn"] >> text = 百度一下')
    page.click('#s-top-left:has(a) >> text= hao123')
    # page.click('//*[@id="s_tab"]//a >> text = 资讯')

def test_nth(page: Page):
    # 如果定位到多个元素需要选择其中某一个，可以使用:nth-match()，索引从1开始
    # 注意：和 :nth-child() 不同之处在于，:nth-match()匹配的元素可以不是邻居关系。
    page.goto("https://www.baidu.com/")
    page.click(':nth-match(#s-top-left > a,2)')
    

    