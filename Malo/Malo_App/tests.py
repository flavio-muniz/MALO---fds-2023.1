from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By


# Create your tests here.
class TestHome(LiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://127.0.0.1:8000/')


    def testTitle(self):
        # Checa se o titulo está correto
        assert 'MALO' in self.driver.title    

    def Login(self):
        self.setUp()

        self.driver.find_element(By.NAME, 'username').send_keys('teaste')
        self.driver.find_element(By.NAME, 'password').send_keys('teste')
        self.driver.find_element(By.CLASS_NAME, 'login').click()



    def testLogin(self):
        self.Login()
        #self.driver.get('http://127.0.0.1:8000/home/')

        curl = self.driver.current_url

        if '/home/' in curl:
            return 'User logged in'
        else:
            return 'User not logged in'
       


    def testLogout(self):

        self.Login()
        logout = self.driver.find_element(By.CLASS_NAME, 'logout')
        assert logout.get_attribute('href') == "http://127.0.0.1:8000/logout/"
        print(self.testLogin())
    
    def tearDown(self):
        self.driver.quit()


