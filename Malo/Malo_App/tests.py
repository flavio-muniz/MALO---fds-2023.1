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

        self.driver.find_element(By.NAME, 'username').send_keys('teste')
        self.driver.find_element(By.NAME, 'password').send_keys('teste')
        self.driver.find_element(By.CLASS_NAME, 'login').click()



    def testLogin(self):
        self.Login()

        curl = self.driver.current_url

        if '/home/' in curl:
            return 'User logged in'
        else:
            return 'User not logged in'
       

    def testOpenMenu(self):
        self.Login()
        self.driver.get('http://127.0.0.1:8000/home/')
        menu = self.driver.find_element(By.CLASS_NAME, 'menu_category')
        assert menu.get_attribute('href') == "http://127.0.0.1:8000/menu-category/"


    def testOpenIgredient(self):
        self.Login()
        self.driver.get('http://127.0.0.1:8000/home/')

        ingredient_list = self.driver.find_element(By.CLASS_NAME, 'ingredient_list')
        assert ingredient_list.get_attribute('href') == "http://127.0.0.1:8000/ingredient-list/"

    def testOpenMenuList(self):
        self.Login()
        self.driver.get('http://127.0.0.1:8000/menu-category/')
        menu = self.driver.find_element(By.CLASS_NAME, 'menu')
        assert menu.get_attribute('href') == "http://127.0.0.1:8000/menu/"
        
    def testOpenAddCategory(self):
        self.Login()
        self.driver.get('http://127.0.0.1:8000/menu-category/')
        oaddcat = self.driver.find_element(By.CLASS_NAME, 'add_category')
        assert oaddcat.get_attribute('href') == "http://127.0.0.1:8000/add-category/"

    def testAddCategory(self):
        self.Login()
        self.driver.get('http://127.0.0.1:8000/add-category/')
        self.driver.find_element(By.CLASS_NAME, 'categoria').send_keys('categoria teste')
        self.driver.find_element(By.CLASS_NAME, 'enviar').click()





    def testLogout(self):
        self.Login()
        logout = self.driver.find_element(By.CLASS_NAME, 'logout')
        assert logout.get_attribute('href') == "http://127.0.0.1:8000/logout/"
        print(self.testLogin())
    
    def tearDown(self):
        self.driver.quit()


