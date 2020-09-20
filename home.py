import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import util_methods

SITE_ADDRESS = "http://automationpractice.com/index.php"


class TestHome(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)  # called even if setUp fails
        self.browser.get(SITE_ADDRESS)

    #@unittest.skip("skipping")
    def test1_launchPageTitle(self):
        self.assertIn('My Store', self.browser.title)

    #@unittest.skip("skipping")
    def test2_emptyCart(self):
        browser = self.browser
        ele = browser.find_element_by_class_name("shopping_cart")
        self.assertIn("(empty)", ele.text)
    
    def test3_addToCart(self):
        browser = self.browser
        browser.execute_script("window.scrollTo(0, 800)")
        sleep(5)  # pause for 5 seconds
        # element = browser.find_elements_by_class_name("product-image-container")
        element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.LINK_TEXT ,"Faded Short Sleeve T-shirts")))
        element.click()
        sleep(3)
        ele = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR ,"p#add_to_cart")))
        ele.click()
        sleep(2)
        browser.save_screenshot("screenshots/before_cart.png")
        ele = browser.find_element_by_class_name("cross")
        ele.click()
        browser.save_screenshot("screenshots/after_cart.png")
        ele = browser.find_element_by_class_name("shopping_cart")
        self.assertNotIn("(empty)", ele.text)
        browser.back()   # go one page back
        browser.save_screenshot("screenshots/browser_back.png")
        browser.execute_script("window.scrollTo(0, 0)")   # scroll to the top of the page
        browser.save_screenshot("screenshots/scroll_up.png")
        # upon return to the home page , the cart still has the product added and is not empty
        ele = browser.find_element_by_class_name("shopping_cart")
        self.assertNotIn("(empty)", ele.text)

    def test4_search(self):
        browser = self.browser
        ele = browser.find_element_by_class_name("search_query")
        ele.click()
        ele.send_keys("blouse")    # search for blouse
        ele = browser.find_element_by_class_name("button-search")
        ele.click()
        sleep(3)

        #assert the count of the search results
        ele = browser.find_elements_by_class_name("product_img_link")
        browser.save_screenshot("screenshots/search_results.png")
        self.assertEqual(len(ele), 1, "There must be only 1 result")

    def tearDown(self):
        self.browser.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)