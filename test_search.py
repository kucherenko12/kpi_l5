from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class Tests(TestCase):
    def tests(self):
        search_request = 'nintendo switch oled'
        url = 'https://www.amazon.com'

        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.implicitly_wait(10)

        browser.get(url)

        browser.find_element_by_css_selector('[class="nav-input nav-progressive-attribute"]').send_keys(search_request)
        browser.find_element_by_css_selector('[class="nav-input nav-progressive-attribute"]').send_keys(Keys.ENTER)

        actualResult = browser.find_element_by_css_selector('[class="a-section a-spacing-small a-spacing-top-small"]').text

        expectedResult = "nintendo switch oled"

        assert expectedResult in actualResult
        browser.close()