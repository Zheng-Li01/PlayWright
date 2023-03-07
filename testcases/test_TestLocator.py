# from time import sleep
# from playwright.sync_api import sync_playwright

# # https://blog.csdn.net/u010698107/article/details/111415888
# class TestLocator(object):
#     def setup(self):
#         playwright = sync_playwright().start()
#         self.browser = playwright.chromium.launch(headless=False)
#         self.context = self.browser.new_context()
#         self.page = self.context.new_page()

#     def teardown(self):
#         self.browser.close()

#     def test_text(self):
#         self.page.goto("https://www.baidu.com/")
#         self.page.click("百度一下")
#         sleep(5)
#         self.page.close()

#     def test_id(self):
#         self.page.goto("https://www.baidu.com/")
#         self.page.fill('[class="s_ipt"]',"test")
#         self.page.click("id=su")
#         sleep(5)
        

#     def test_xpath(self):
#         self.page.goto("https://www.baidu.com/")
#         self.page.fill("id=kw","test")
#         self.page.click("id=kw")
#         sleep(2)
#         self.page.click('//*[@id="s_tab"]//a[2]')
#         sleep(5)

#     def test_css_selector(self):
#         self.page.goto("https://www.baidu.com/")
#         self.page.fill("id=kw","test")
#         self.page.click("id=kw")
#         sleep(2)
#         self.page.click("#s_tab a:nth-child(2) + a")
#         sleep(3)

#     def test_css_has(self):
#         self.page.goto("https://www.baidu.com/")
#         self.page.click('#s-top-left:has(a) > a:nth-child(2)')

#     def test_css_is(self):
#         self.page.goto("https://www.baidu.com/")
#         sleep(2)
#         self.page.click(':is(a:has-text("新闻"))')
#         sleep(5)

#     def test_layout(self):
#         self.page.goto("https://www.baidu.com/")
#         sleep(2)
#         self.page.fill("id=kw","test")
#         self.page.click('inpit:right-of(#kw)')
#         sleep(5)

#     def test_nth_match(self):
#         self.page.goto("https://www.baidu.com/")
#         sleep(2)   
#         self.page.click(':nth-match(#s-top-left > a, 2)')
#         sleep(5)   
        
# testLocator = TestLocator()
# testLocator.setup()
# testLocator.test_text()
# testLocator.teardown()
       
        
        
        
        

        