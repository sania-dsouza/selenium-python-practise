# tests run using pytest
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SITE_ADDRESS = "http://automationpractice.com/index.php"


@pytest.fixture(scope="class")
def driver_init(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    driver.get(SITE_ADDRESS)
    yield
    driver.close()


class TestHomePage:
    @pytest.mark.usefixtures("driver_init")
    def test1_launch_page_title(self):
        #self.driver.get(SITE_ADDRESS)
        assert 'My Store' in self.driver.title
        time.sleep(2)

    def test2_emptyCart(self):
        ele = self.driver.find_element_by_class_name("shopping_cart")
        assert "(empty)" in ele.text
        self.driver.save_screenshot("screenshots/before_cart.png")

    def test3_addToCart(self):
        browser = self.driver
        browser.execute_script("window.scrollTo(0, 800)")
        time.sleep(5)  # pause for 5 seconds
        # element = browser.find_elements_by_class_name("product-image-container")
        element = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Faded Short Sleeve T-shirts")))
        element.click()
        time.sleep(3)
        ele = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "p#add_to_cart")))
        ele.click()
        time.sleep(2)
        browser.save_screenshot("screenshots/before_cart.png")
        ele = browser.find_element_by_class_name("cross")
        ele.click()
        browser.save_screenshot("screenshots/after_cart.png")
        ele = browser.find_element_by_class_name("shopping_cart")
        assert "(empty)" not in ele.text
        browser.back()  # go one page back
        browser.save_screenshot("screenshots/browser_back.png")
        browser.execute_script("window.scrollTo(0, 0)")  # scroll to the top of the page
        browser.save_screenshot("screenshots/scroll_up.png")
        # upon return to the home page , the cart still has the product added and is not empty
        ele = browser.find_element_by_class_name("shopping_cart")
        assert "(empty)" not in ele.text

    def test4_search(self):
        browser = self.driver
        ele = browser.find_element_by_class_name("search_query")
        ele.click()
        ele.send_keys("blouse")    # search for blouse
        ele = browser.find_element_by_class_name("button-search")
        ele.click()
        time.sleep(3)

        # assert the count of the search results
        ele = browser.find_elements_by_class_name("product_img_link")
        browser.save_screenshot("screenshots/search_results.png")
        assert len(ele) == 1, "There must be only 1 result"

