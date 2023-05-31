from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=chrome_options)
class cleo(TestCase):
    

    def test(self):
        driver.get("http://127.0.0.1:8000/")
        self.run_tests(driver)

    def register_gerente(self, driver):
        register = driver.find_element(By.ID,"signup")
        register.click()
        time.sleep(2)
        username_register = driver.find_element(By.CLASS_NAME,"username")
        username_register.send_keys("Gerente")
        email_register = driver.find_element(By.CLASS_NAME,"email")
        email_register.send_keys("gerente@malo.com")
        password_register = driver.find_element(By.CLASS_NAME,"password1")
        password_register.send_keys("Senhamassa")
        confirm_register = driver.find_element(By.CLASS_NAME,"password2")
        confirm_register.send_keys("Senhamassa")
        login = driver.find_element(By.CLASS_NAME, "submit")
        login.submit()
        driver.quit()
        
    def register_garcom1(self, driver):
        register = driver.find_element(By.ID,"signup")
        register.click()
        time.sleep(2)
        username_register = driver.find_element(By.CLASS_NAME,"username")
        username_register.send_keys("Garcom5")
        email_register = driver.find_element(By.CLASS_NAME,"email")
        email_register.send_keys("garcom1@malo.com")
        password_register = driver.find_element(By.CLASS_NAME,"password1")
        password_register.send_keys("Senhamassa")
        confirm_register = driver.find_element(By.CLASS_NAME,"password2")
        confirm_register.send_keys("Senhamassa")
        login = driver.find_element(By.CLASS_NAME, "submit")
        login.submit()
        driver.quit()
        #qqq
    
    
    def run_tests(self, driver):
        self.register_gerente(driver)
        self.register_garcom1(driver)