from pages.base_shape import Base

class LoginPage(Base):
    url = 'https://www.saucedemo.com/'
    username = ('id', 'user-name')
    password = ('id', 'password')
    login_button = ('id', 'login-button')
    err_message = ('css selector', '[data-test=error]')

    def open(self):
        self.driver.get(self.url)

    def login(self, username, password):
        self.find(self.username).send_keys(username)
        self.find(self.password).send_keys(password)
        self.find(self.login_button).click()

    def get_error_message(self):
        return self.find(self.err_message).text
