import unittest,time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_pg import LoginPage
from pages.store_pg import InventoryPage


class loginTests(unittest.TestCase):

    def setUp(self):
        
        options = Options()
        
        options.add_argument('--headless=new')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
        self.driver.maximize_window()

        self.login_page = LoginPage(self.driver)
        self.login_page.open()

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

    def test_valid_form(self):
        self.login_page.login('standard_user', 'secret_sauce')
        inventory_page = InventoryPage(self.driver)

        self.assertTrue(inventory_page.is_loaded())

    def test_invalid_form(self):
        self.login_page.login('xyz', 'def4ault')
        
        error_message = self.login_page.find(self.login_page.err_message).text
        self.assertIn('Username and password do not match any user in this service', error_message)

    def test_empty_form(self):
        self.login_page.login('', '')

        error_message = self.login_page.find(LoginPage.err_message).text
        self.assertIn('Username is required', error_message)
    
    def test_empty_login(self):
        self.login_page.login('', 'secret_sauce')

        error_message = self.login_page.find(LoginPage.err_message).text
        self.assertIn('Username is required', error_message)
          
    def test_empty_password(self):
        self.login_page.login('problem_user', '')

        error_message = self.login_page.find(LoginPage.err_message).text
        self.assertIn('Password is required', error_message)


if __name__ == "__main__":
    unittest.main()
