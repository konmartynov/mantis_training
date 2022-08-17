from random import choice
from string import ascii_letters, digits
from selenium import webdriver
from fixtures.session import SessionHelper
from fixtures.project import ProjectHelper
from fixtures.james import JamesHelper
from fixtures.signup import SignupHelper
from fixtures.mail import MailHelper
from fixtures.soap import SoapHelper


class Application:

    def __init__(self, browser, config):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(3)
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.james = JamesHelper(self)
        self.signup = SignupHelper(self)
        self.mail = MailHelper(self)
        self.soap = SoapHelper(self)
        self.config = config
        self.base_url = config['web']['baseUrl']

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def gen_random_string(self):
        r_str = ''.join(choice(ascii_letters) for i in range(5))
        return r_str

    def gen_random_number(self):
        r_mob = '+7' + ''.join(choice(digits) for i in range(10))
        return r_mob

    def open_homepage(self):
        wd = self.wd
        wd.get(self.base_url)

    def return_to_homepage(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    def go_to_home(self):
        wd = self.wd
        if not (wd.find_elements_by_xpath("//div[4]/div/form/input") and len(wd.find_elements_by_name("add")) == 0):
            wd.find_element_by_xpath("//div[3]/ul/li[1]").click()

    def destroy(self):
        self.wd.quit()
