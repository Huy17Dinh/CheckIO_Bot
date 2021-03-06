import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import time


def read_credentials():
    secrets = 'secrets.json'
    with open(secrets) as f:
        keys = json.loads(f.read())
        return keys


class CheckIOSolver:

    def __init__(self, login, password):
        # init function is a special function in python when we created a class. 
        # init function will executed everytime a new object is created
        self.login = login
        self.password = password
        self.google = "https://www.google.com"
        self.base_url = "https://checkio.org"
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def login_to_checkio(self):
        self.driver.get(self.base_url)
        self.get_on_python_checkio()
        self.put_credentials_to_form()
    
    def put_credentials_to_form(self):
        try:
            # enter user credentials and Click on Submit button to logins
            self.driver.find_element_by_id("id_username").send_keys(self.login)
            time.sleep(1)
            password_field = self.driver.find_element_by_id("id_password")
            password_field.send_keys(self.password)
            password_field.submit()

        except NoSuchElementException:
            print("Exception NoSuchElementException")

    
    def get_on_python_checkio(self):
        try:
            self.driver.find_element_by_link_text('Python').click()
            time.sleep(2)
        except NoSuchElementException:
            print("incorrect Page")


            
    
    def main_logic(self):
        self.login_to_checkio()
        time.sleep(10)
        self.driver.quit()
       


if __name__ == '__main__':
    credentials = read_credentials()
    bot = CheckIOSolver(credentials['username'], credentials['password'])
    # at this stage, we can created our objects
    bot.main_logic()