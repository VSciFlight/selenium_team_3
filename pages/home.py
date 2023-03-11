import utils as u
import locators


class HomePage:

    def __init__(self, driver):
        self.driver = driver

################################################## Header ############################################################################################################
    def click_home_btn(self):
        """
        performs click on the Home button in the Header of Home page
        :return:
        """
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(locators.Locator.locHome['Head_Home'])).click()
    def click_contact_btn(self):
        """
        performs click on the Contact button in the Header of Home page
        :return:
        """
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(locators.Locator.locHome['Head_Contact'])).click()
    def click_about_us_btn(self):
        """
        performs click on the About us button in the Header of Home page
        :return:
        """
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(locators.Locator.locHome['Head_About_Us'])).click()
    def click_cart_btn(self):
        """
        performs click on the Cart button in the Header of Home page
        :return:
        """
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(locators.Locator.locHome['Head_Cart'])).click()
    def click_login_btn(self):
        """
        performs click on the Log-in button in the Header of Home page
        :return:
        """
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(locators.Locator.locHome['Head_Login'])).click()
    def set_usernsme(self, username):
        """
        set the given username in the Lod-in modal username field
        :param self:
        :param username:
        :return:
        """
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located((u.By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div[1]/input"))).send_keys(username)
    def set_password(self, password):
        """
        set the given password in the Lod-in modal password field
        :param self:
        :param password:
        :return:
        """
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located((u.By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div[2]/input"))).send_keys(password)
    def click_login(self):
        """
        performs click on the log-in button in the Log-in modal
        :param self:
        :return:
        """
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located((u.By.XPATH, "/html/body/div[3]/div/div/div[3]/button[2]"))).click()
    def click_logout_btn(self):
        """
        performs click on the Log-out button in the Header of Home page
        :param self:
        :return:
        """
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(locators.Locator.locHome['Head_Logout'])).click()
    def click_signup_btn(self):
        """
        performs click on the Sign-up button in the Header of Home page
        :param self:
        :return:
        """
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(locators.Locator.locHome['Head_Signup'])).click()
    def click_logo_btn(self):
        """
        performs click on the Logo in the Header of Home page
        :param self:
        :return:
        """
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(locators.Locator.locHome['Head_Logo'])).click()

#######################################################################################################################################################################

################################################################ Slideshow #################################################################################################

    def click_right_arrow_btn(self):
        """
        performs click on the right arrow in the Slide show window
        :param self:
        :return:
        """
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(locators.Locator.locHome['Slide_Right_Arrow'])).click()
    def click_left_arrow_btn(self):
        """
        performs click on the left arrow in the Slide show window
        :param self:
        :return:
        """
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(locators.Locator.locHome['Slide_Left_Arrow'])).click()
    def click_leftslide_indicator(self):
        """
        performs click on the left side indicator in the Slide show window
        :param self:
        :return:
        """
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(locators.Locator.locHome['Slide_LeftSlide_indicator'])).click()
    def click_middleslide_indicator(self):
        """
        performs click on the middle indicator in the Slide show window
        :param self:
        :return:
        """
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(locators.Locator.locHome['Slide_MidleSlide_indicator'])).click()
    def click_rightslide_indicator(self):
        """
        performs click on the right indicator in the Slide show window
        :param self:
        :return:
        """
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(locators.Locator.locHome['Slide_RightSlide_indicator'])).click()
