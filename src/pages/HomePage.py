from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from src.locators.HomeLocators import homelocs

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def wdw_locator(self, locator):
        return WDW(self.driver, 5).until(EC.visibility_of_element_located(locator))

    # Header
    def home_btn_click(self):
        HomePage.wdw_locator(self, homelocs['Home']).click()
    def contact_btn_click(self):
        HomePage.wdw_locator(self, homelocs['Contact']).click()
    def about_us_btn_click(self):
        HomePage.wdw_locator(self, homelocs['AboutUs']).click()
    def cart_btn_click(self):
        HomePage.wdw_locator(self, homelocs['Cart']).click()
    def login_btn_click(self):
        HomePage.wdw_locator(self, homelocs['LogIn']).click()
    def signup_btn_click(self):
        HomePage.wdw_locator(self, homelocs['SignUp']).click()
    def logout_btn_click(self, username, password):
        HomePage.wdw_locator(self, homelocs['LogIn']).click()
        HomePage.wdw_locator(self, (By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div[1]/input")).send_keys(username)
        HomePage.wdw_locator(self, (By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div[2]/input")).send_keys(password)
        HomePage.wdw_locator(self, (By.XPATH, "/html/body/div[3]/div/div/div[3]/button[2]")).click()
        HomePage.wdw_locator(self, homelocs['LogOut']).click()
    def logo_btn_click(self):
        HomePage.wdw_locator(self, homelocs['Logo']).click()

    # Slide Show
    def right_arrow_click(self):
        HomePage.wdw_locator(self, homelocs['slsh_right_arrow']).click()
    def left_arrow_click(self):
        HomePage.wdw_locator(self, homelocs['slsh_left_arrow']).click()
    def left_indicator_click(self):
        HomePage.wdw_locator(self, homelocs['slsh_left_indicator']).click()
    def middle_indicator_click(self):
        HomePage.wdw_locator(self, homelocs['slsh_middle_indicator']).click()
    def right_indicator_click(self):
        HomePage.wdw_locator(self, homelocs['slsh_right_indicator']).click()

    # Body
    def categories_btn_click(self):
        HomePage.wdw_locator(self, homelocs['Categories']).click()
    def phones_btn_click(self):
        HomePage.wdw_locator(self, homelocs['Phones']).click()
    def laptops_btn_click(self):
        HomePage.wdw_locator(self, homelocs['Laptops']).click()
    def monitors_btn_click(self):
        HomePage.wdw_locator(self, homelocs['Monitors']).click()
    def item_click(self):
        HomePage.wdw_locator(self, homelocs['Item']).click()
    def previous_btn_click(self):
        HomePage.wdw_locator(self, homelocs['Previous']).click()
    def next_btn_click(self):
        HomePage.wdw_locator(self, homelocs['Next']).click()
