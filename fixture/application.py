from selenium.webdriver.firefox.webdraiver import WebDriver
from fixture.session import SessionHelper
class Application:

    def __init__(self):
        self.wd = webdriver.Chrome(executable_path=r'')
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
    def test_untitled_test_case(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.create_group(wd)


    def destroy(self):
        self.wd.quit()
