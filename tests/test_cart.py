import unittest
import utils as u
from pages.home import HomePage
class TestCartPage(unittest.TestCase):
    def setUp(self):
        try:
            options = u.WebDriver.ChromeOptions()
            options.add_argument("--disable-extensions")
            self.driver = u.WebDriver.Chrome(options=options)
            self.driver.maximize_window()
            self.driver.get("https://www.demoblaze.com/index.html")
        except AssertionError:
            self.driver.quit()

    def tearDown(self):
        self.driver.quit()


    def test_cart_recovery(self):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located((u.By.XPATH, "/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a"))).click()
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located((u.By.XPATH, "/html/body/div[5]/div/div[2]/div[2]/div/a"))).click()
        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert
        self.assertEqual(alert.text, "Product added")
        alert.accept()
        hp = HomePage
        hp.click_cart_btn(self)
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located((u.By.XPATH, "/html/body/div[6]/div/div[1]/div/table/tbody/tr")))
        self.assertEqual(self.driver.find_element(u.By.XPATH, "/html/body/div[6]/div/div[1]/div/table/tbody/tr").get_attribute("class"), "success")
        self.driver.quit()
        self.driver = u.WebDriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/index.html")
        hp = HomePage
        hp.click_cart_btn(self)
        try:
            u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located((u.By.XPATH, "/html/body/div[6]/div/div[1]/div/table/tbody/tr")))
        except:
            pass
        self.assertTrue(self.driver.find_elements(u.By.XPATH,"/html/body/div[6]/div/div[1]/div/table/tbody/tr"), msg="Item is not avalible")

#######################################################################################################
    def test_add_item_to_cart(self):
        u.sleep(3)
        self.driver.find_element(u.By.XPATH, '//*[@id="tbodyid"]/div[1]/div/div/h4/a').click()
        u.sleep(3)
        self.add_cart = self.driver.find_element(u.By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a')
        self.add_cart.click()
        u.sleep(3)
        u.WDW(self.driver, 3).until(u.EC.alert_is_present())
        self.alert = self.driver.switch_to.alert
        self.alert.accept()
        self.driver.find_element(u.By.XPATH, '//*[@id="cartur"]').click()
        u.sleep(3)
        self.assertTrue(True)



    def test_Removing_item_from_cart(self):
        u.sleep(3)
        self.driver.find_element(u.By.XPATH, '//*[@id="tbodyid"]/div[3]/div/div/h4/a').click()
        u.sleep(3)
        self.Add_to_cart_button = self.driver.find_element(u.By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a')
        self.Add_to_cart_button.click()
        u.sleep(3)
        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()
        self.driver.find_element(u.By.XPATH, '//*[@id="cartur"]').click()
        u.sleep(2)
        delete = self.driver.find_element(u.By.XPATH, '//*[@id="tbodyid"]/tr/td[4]/a')
        delete.click()
        u.sleep(3)
        self.assertTrue(True)




    def test_place_order_button(self):

        u.sleep(4)
        self.driver.find_element(u.By.XPATH, '//*[@id="tbodyid"]/div[5]/div/div/h4/a').click()
        u.sleep(3)
        self.Add_cart_button = self.driver.find_element(u.By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a')
        self.Add_cart_button.click()
        u.sleep(3)
        u.WDW(self.driver, 3).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()
        self.driver.find_element(u.By.XPATH, '//*[@id="cartur"]').click()
        u.sleep(4)
        self.Place_order_button = self.driver.find_element(u.By.XPATH, '//*[@id="page-wrapper"]/div/div[2]/button')
        self.Place_order_button.click()
        u.sleep(3)



    def test_purchace_with_valid_data(self):

        u.sleep(5)
        self.driver.find_element(u.By.XPATH, '//*[@id="tbodyid"]/div[5]/div/div/h4/a').click()
        u.sleep(5)
        self.Add_cart_button = self.driver.find_element(u.By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a')
        self.Add_cart_button.click()
        u.sleep(5)
        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()
        u.sleep(4)
        self.driver.find_element(u.By.XPATH, '//*[@id="cartur"]').click()
        u.sleep(4)
        self.Place_order_button = self.driver.find_element(u.By.XPATH, '//*[@id="page-wrapper"]/div/div[2]/button')
        self.Place_order_button.click()
        u.sleep(5)
        self.name_field = self.driver.find_element(u.By.XPATH, '//*[@id="name"]')
        self.country_filed = self.driver.find_element(u.By.XPATH, '//*[@id="country"]')
        self.city_filed = self.driver.find_element(u.By.XPATH, '//*[@id="city"]')
        self.credit_card_filed = self.driver.find_element(u.By.XPATH, '//*[@id="card"]')
        self.month_filed = self.driver.find_element(u.By.XPATH, '//*[@id="month"]')
        self.year_filed = self.driver.find_element(u.By.XPATH, '//*[@id="year"]')

        self.name_field.send_keys("nir_peled")
        self.country_filed.send_keys("israel")
        self.city_filed.send_keys("shoam")
        self.credit_card_filed.send_keys("51159876543654")
        self.month_filed.send_keys("14.6")
        self.year_filed.send_keys("2001")

        u.sleep(3)
        self.purchase = self.driver.find_element(u.By.XPATH, '//*[@id="orderModal"]/div/div/div[3]/button[2] ')
        self.purchase.click()
        u.sleep(3)



    def test_ok_button_valid(self):

        u.sleep(5)
        self.driver.find_element(u.By.XPATH, '//*[@id="tbodyid"]/div[5]/div/div/h4/a').click()
        u.sleep(5)
        self.Add_cart_button = self.driver.find_element(u.By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a')
        self.Add_cart_button.click()
        u.sleep(5)
        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()
        u.sleep(4)
        self.driver.find_element(u.By.XPATH, '//*[@id="cartur"]').click()
        u.sleep(4)
        self.Place_order_button = self.driver.find_element(u.By.XPATH, '//*[@id="page-wrapper"]/div/div[2]/button')
        self.Place_order_button.click()
        u.sleep(5)

        self.name_field = self.driver.find_element(u.By.XPATH, '//*[@id="name"]')
        self.country_filed = self.driver.find_element(u.By.XPATH, '//*[@id="country"]')
        self.city_filed = self.driver.find_element(u.By.XPATH, '//*[@id="city"]')
        self.credit_card_filed = self.driver.find_element(u.By.XPATH, '//*[@id="card"]')
        self.month_filed = self.driver.find_element(u.By.XPATH, '//*[@id="month"]')
        self.year_filed = self.driver.find_element(u.By.XPATH, '//*[@id="year"]')

        self.name_field.send_keys("nir_peled")
        self.country_filed.send_keys("israel")
        self.city_filed.send_keys("shoam")
        self.credit_card_filed.send_keys("51159876543654")
        self.month_filed.send_keys("14.6")
        self.year_filed.send_keys("2001")

        u.sleep(3)
        self.purchase = self.driver.find_element(u.By.XPATH, '//*[@id="orderModal"]/div/div/div[3]/button[2] ')
        self.purchase.click()
        u.sleep(3)
        ok_button = self.driver.find_element(u.By.XPATH, '/html/body/div[10]/div[7]/div/button')
        ok_button.click()
        u.sleep(4)

    def test_purchace_invalid_data(self):

        u.sleep(5)
        self.driver.find_element(u.By.XPATH, '//*[@id="tbodyid"]/div[6]/div/div/h4/a').click()
        u.sleep(5)
        self.Add_cart_button = self.driver.find_element(u.By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a')
        self.Add_cart_button.click()
        u.sleep(5)
        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()
        self.driver.find_element(u.By.XPATH, '//*[@id="cartur"]').click()
        u.sleep(4)
        self.Place_order_button = self.driver.find_element(u.By.XPATH, '//*[@id="page-wrapper"]/div/div[2]/button')
        self.Place_order_button.click()
        u.sleep(5)

        self.name_field = self.driver.find_element(u.By.XPATH, '//*[@id="name"]')
        self.country_filed = self.driver.find_element(u.By.XPATH, '//*[@id="country"]')
        self.city_filed = self.driver.find_element(u.By.XPATH, '//*[@id="city"]')
        self.credit_card_filed = self.driver.find_element(u.By.XPATH, '//*[@id="card"]')
        self.month_filed = self.driver.find_element(u.By.XPATH, '//*[@id="month"]')
        self.year_filed = self.driver.find_element(u.By.XPATH, '//*[@id="year"]')

        self.name_field.send_keys("!%#^@dscfg")
        self.country_filed.send_keys("ndskxmcn")
        self.city_filed.send_keys("543gf")
        self.credit_card_filed.send_keys("gtrdsx34#%^$#")
        self.month_filed.send_keys("%$#@FD")
        self.year_filed.send_keys("^TGFD")

        u.sleep(4)
        purchase = self.driver.find_element(u.By.XPATH, '//*[@id="orderModal"]/div/div/div[3]/button[2] ')
        purchase.click()
        u.sleep(4)
        ok_button = self.driver.find_element(u.By.XPATH, '/html/body/div[10]/div[7]/div/button')
        ok_button.click()
        u.sleep(2)

    def test_purchace_valid_data(self):

        u.sleep(5)
        self.driver.find_element(u.By.XPATH, '//*[@id="tbodyid"]/div[6]/div/div/h4/a').click()
        u.sleep(5)
        self.Add_cart_button = self.driver.find_element(u.By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a')
        self.Add_cart_button.click()
        u.sleep(5)
        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()
        self.driver.find_element(u.By.XPATH, '//*[@id="cartur"]').click()
        u.sleep(4)
        self.Place_order_button = self.driver.find_element(u.By.XPATH, '//*[@id="page-wrapper"]/div/div[2]/button')
        self.Place_order_button.click()
        u.sleep(5)

        self.name_field = self.driver.find_element(u.By.XPATH, '//*[@id="name"]')
        self.country_filed = self.driver.find_element(u.By.XPATH, '//*[@id="country"]')
        self.city_filed = self.driver.find_element(u.By.XPATH, '//*[@id="city"]')
        self.credit_card_filed = self.driver.find_element(u.By.XPATH, '//*[@id="card"]')
        self.month_filed = self.driver.find_element(u.By.XPATH, '//*[@id="month"]')
        self.year_filed = self.driver.find_element(u.By.XPATH, '//*[@id="year"]')

        self.name_field.send_keys("Ran")
        self.country_filed.send_keys("Israel")
        self.city_filed.send_keys("Holon")
        self.credit_card_filed.send_keys("1884230548932442")
        self.month_filed.send_keys("13.4")
        self.year_filed.send_keys("2002")

        u.sleep(4)
        purchase = self.driver.find_element(u.By.XPATH, '//*[@id="orderModal"]/div/div/div[3]/button[2] ')
        purchase.click()
        u.sleep(4)
        ok_button = self.driver.find_element(u.By.XPATH, '/html/body/div[10]/div[7]/div/button')
        ok_button.click()
        u.sleep(4)


