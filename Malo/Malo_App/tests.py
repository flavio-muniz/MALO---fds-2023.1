from django import test
from django.forms import Select
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



# Create your tests here.
class TestHome(LiveServerTestCase):
 
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://127.0.0.1:8000/')


    def testTitle(self):
        # Checa se o titulo está correto
        assert 'MALO' in self.driver.title
    '''
    def test1CriarLoginGerente(self):
        self.setUp()


        self.driver.find_element(By.CLASS_NAME, 'signup').click()
        
        self.driver.find_element(By.CLASS_NAME, 'username').send_keys('Gerente')
        self.driver.find_element(By.CLASS_NAME, 'email').send_keys('gerente@malo.com')
        self.driver.find_element(By.CLASS_NAME, 'password1').send_keys('Senhamassa')
        self.driver.find_element(By.CLASS_NAME, 'password2').send_keys('Senhamassa')
        criarLogin = self.driver.find_element(By.CLASS_NAME, 'submit').submit()
        print(criarLogin, 'teste')


    def test2CriarLoginGarcom1(self):
        self.setUp()

        self.driver.find_element(By.CLASS_NAME, 'signup').click()
        
        self.driver.find_element(By.CLASS_NAME, 'username').send_keys('Garcom1')
        self.driver.find_element(By.CLASS_NAME, 'email').send_keys('garcom1@malo.com')
        self.driver.find_element(By.CLASS_NAME, 'password1').send_keys('Senhamassa')
        self.driver.find_element(By.CLASS_NAME, 'password2').send_keys('Senhamassa')
        criarLogin = self.driver.find_element(By.CLASS_NAME, 'submit').submit()
        print(criarLogin, 'teste')
    '''


    def Login(self):
        self.setUp()

        self.driver.find_element(By.NAME, 'username').send_keys('Gerente')
        self.driver.find_element(By.NAME, 'password').send_keys('Senhamassa')
        self.driver.find_element(By.CLASS_NAME, 'login').click()



    def testLoginGerente(self):
        self.Login()

        curl = self.driver.current_url
        print(curl)
        if '/home/' in curl:
            return 'User logged in'
        else:
            return 'User not logged in'
        
    def testOpenMesa(self):
        self.Login()
        omesa = self.driver.find_element(By.CLASS_NAME, 'mesa')
        assert omesa.get_attribute('href') == "http://127.0.0.1:8000/mesa/"


    
    def testAdd1Mesa(self):
        self.Login()
        self.driver.find_element(By.CLASS_NAME, 'mesa').click()
        self.driver.find_element(By.CLASS_NAME, 'add_mesa').click()


    def testAddMultMesas(self):
        self.Login()
        self.driver.find_element(By.CLASS_NAME, 'mesa').click()
        self.driver.find_element(By.ID, 'add_qtd_mesas').send_keys('4')
        self.driver.find_element(By.CLASS_NAME, 'submit_add_mesas').click()

    def testRem1Mesa(self):
        self.Login()
        self.driver.find_element(By.CLASS_NAME, 'mesa').click()
        self.driver.find_element(By.ID, 'rem_mesa').click()


    def testRemMultMesas(self):
        self.Login()
        self.driver.find_element(By.CLASS_NAME, 'mesa').click()
        self.driver.find_element(By.ID, 'rem_qtd_mesas').send_keys('2')
        self.driver.find_element(By.CLASS_NAME, 'submit_rem_mesas').click()

    def testAddCategory1(self):
        self.Login()
        self.driver.get('http://127.0.0.1:8000/home/')
        self.driver.find_element(By.CLASS_NAME, 'menu_category').click()
        self.driver.find_element(By.CLASS_NAME, 'add_category').click()
        self.driver.find_element(By.CLASS_NAME, 'categoria').send_keys('Bebidass')
        self.driver.find_element(By.CLASS_NAME, 'enviar').click()


    def testAddCategory2(self):
        self.Login()
        self.driver.get('http://127.0.0.1:8000/home/')
        self.driver.find_element(By.CLASS_NAME, 'menu_category').click()
        self.driver.find_element(By.CLASS_NAME, 'add_category').click()
        self.driver.find_element(By.CLASS_NAME, 'categoria').send_keys('Comidas')
        self.driver.find_element(By.CLASS_NAME, 'enviar').click()

    def testAddCategoryTemp(self):
        self.Login()
        self.driver.get('http://127.0.0.1:8000/home/')
        self.driver.find_element(By.CLASS_NAME, 'menu_category').click()
        self.driver.find_element(By.CLASS_NAME, 'add_category').click()
        self.driver.find_element(By.CLASS_NAME, 'categoria').send_keys('Categoria para remover')
        self.driver.find_element(By.CLASS_NAME, 'enviar').click()
  
        
    def testRemCategoryTemp(self):
        self.Login()
        self.driver.get('http://127.0.0.1:8000/home/')
        self.driver.find_element(By.CLASS_NAME, 'menu_category').click()
        self.driver.find_element(By.NAME, 'rem_Categoria para remover').click()

    def testAddDish1(self):
        self.Login()
        self.driver.get('http://127.0.0.1:8000/add-dishes/')
        elemento_select = self.driver.find_element(By.NAME, "category")

        dropdown = Select(elemento_select)
        elemento_select.click()
        dropdown.select_by_visible_text("Bebidas")

        self.driver.find_element(By.NAME, 'name').send_keys('Coca-Cola')
        self.driver.find_element(By.NAME, 'price').send_keys('8')
        self.driver.find_element(By.NAME, 'description').send_keys('Coca-Cola ks')

        self.driver.find_element(By.CLASS_NAME, 'submit').click()

    def testAddDish2(self):
        self.Login()
        self.driver.get('http://127.0.0.1:8000/add-dishes/')
        elemento_select = self.driver.find_element(By.NAME, "category")

        dropdown = Select(elemento_select)
        elemento_select.click()
        dropdown.select_by_visible_text("Comidas")

        self.driver.find_element(By.NAME, 'name').send_keys('Suco de laranja')
        self.driver.find_element(By.NAME, 'price').send_keys('10')
        self.driver.find_element(By.NAME, 'description').send_keys('Suco de laranja 300ml')

        self.driver.find_element(By.CLASS_NAME, 'submit').click()
   
    '''
    def testEditDish(self):
        self.Login()
        self.driver.get('http://127.0.0.1:8000/menu-category/')
        self.driver.find_element(By.NAME, 'edit_Suco de laranja').click()
        elemento_select = self.driver.find_element(By.NAME, "category")

        dropdown = Select(elemento_select)
        elemento_select.click()
        dropdown.select_by_visible_text("Comidas")

        self.driver.find_element(By.NAME, 'name').send_keys('Suco de laranja')
        self.driver.find_element(By.NAME, 'price').send_keys('10')
        self.driver.find_element(By.NAME, 'description').send_keys('Suco de laranja 300ml')

        self.driver.find_element(By.CLASS_NAME, 'submit').click()
    '''

    
    def testEditCategory(self):
        self.Login()
        self.driver.get('http://127.0.0.1:8000/home/')
        self.driver.find_element(By.CLASS_NAME, 'menu_category').click()
        self.driver.find_element(By.CLASS_NAME, 'edit_Bebidass').click()
        self.driver.find_element(By.CLASS_NAME, 'categoria').clear()
        self.driver.find_element(By.CLASS_NAME, 'categoria').send_keys('Bebidas')

        self.driver.find_element(By.CLASS_NAME, 'submit').click()


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
        self.driver.get('http://127.0.0.1:8000/home/')
        self.driver.find_element(By.CLASS_NAME, 'menu_category').click()
        menu = self.driver.find_element(By.CLASS_NAME, 'menu')
        assert menu.get_attribute('href') == "http://127.0.0.1:8000/menu/"
        
    def testOpenAddCategory(self):
        self.Login()
        self.driver.get('http://127.0.0.1:8000/home/')
        self.driver.find_element(By.CLASS_NAME, 'menu_category').click()
        oaddcat = self.driver.find_element(By.CLASS_NAME, 'add_category')
        assert oaddcat.get_attribute('href') == "http://127.0.0.1:8000/add-category/"

    

    def testLogout(self):
        self.Login()
        logout = self.driver.find_element(By.CLASS_NAME, 'logout')
        assert logout.get_attribute('href') == "http://127.0.0.1:8000/logout/"
        print(self.testLoginGerente())
    

    def tearDown(self):
        self.driver.quit()

    


