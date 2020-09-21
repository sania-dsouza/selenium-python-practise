# tests run using pytest
from selenium import webdriver

SITE_ADDRESS = "http://automationpractice.com/index.php"


class TestHomePage:

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)  # called even if setUp fails

    def test1_launch_page_title(self):
        self.browser = webdriver.Chrome()
        self.browser.get(SITE_ADDRESS)
        assert 'My Store' in self.browser.title
        self.browser.quit()

