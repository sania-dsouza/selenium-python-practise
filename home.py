import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SITE_ADDRESS = "http://automationpractice.com/index.php"


class TestHome(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)  # called even if setUp fails
        self.browser.get(SITE_ADDRESS)

    @unittest.skip("skipping")
    def test1_launchPageTitle(self):
        self.assertIn('My Store', self.browser.title)

    @unittest.skip("skipping")
    def test2_emptyCart(self):
        browser = self.browser
        ele = browser.find_element_by_class_name("shopping_cart")
        self.assertIn("(empty)", ele.text)
    
    def test3_addToCart(self):
        browser = self.browser
        browser.execute_script("window.scrollTo(0, 800)")
        sleep(5)
        # element = browser.find_elements_by_class_name("product-image-container")
        element = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.LINK_TEXT ,"Faded Short Sleeve T-shirts")))
        element.click()
        sleep(3)
        ele = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR ,"p#add_to_cart")))
        ele.click()
        sleep(2)
        browser.save_screenshot("before_cart.png")
        ele = browser.find_element_by_class_name("cross")
        ele.click()
        browser.save_screenshot("after_cart.png")
        ele = browser.find_element_by_class_name("shopping_cart")
        self.assertNotIn("(empty)", ele.text)
        browser.back()

    def tearDown(self):
        self.browser.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)