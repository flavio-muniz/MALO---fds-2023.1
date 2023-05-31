from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestHome(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        cls.browser = webdriver.Chrome(options=chrome_options)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def test_title(self):
        self.browser.get('http://127.0.0.1:8000/')
       

 