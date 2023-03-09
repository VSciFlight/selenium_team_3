import utils as u


# def add_item_to_cart():
#     driver = u.WebDriver.Chrome()
#     driver.get("https://demoblaze.com/index.html")
#     u.sleep(5)
#     driver.find_element(u.By.XPATH, '//*[@id="tbodyid"]/div[1]/div/div/h4/a').click()
#     u.sleep(4)
#     add_cart = driver.find_element(u.By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a')
#     add_cart.click()
#     u.sleep(4)
#     u.WDW(driver, 5).until(u.EC.alert_is_present())
#     alert = driver.switch_to.alert
#     alert.accept()
#     driver.find_element(u.By.XPATH, '//*[@id="cartur"]').click()
#     u.sleep(4)
#
# add_item_to_cart()

#####################################################################################################

# def Removing_item_from_cart():
#     driver = u.WebDriver.Chrome()
#     driver.get("https://demoblaze.com/index.html")
#     u.sleep(5)
#     driver.find_element(u.By.XPATH , '//*[@id="tbodyid"]/div[3]/div/div/h4/a').click()
#     u.sleep(3)
#     Add_to_cart_button = driver.find_element(u.By.XPATH , '//*[@id="tbodyid"]/div[2]/div/a')
#     Add_to_cart_button.click()
#     u.sleep(3)
#     u.WDW(driver, 5).until(u.EC.alert_is_present())
#     alert = driver.switch_to.alert
#     alert.accept()
#     driver.find_element(u.By.XPATH, '//*[@id="cartur"]').click()
#     u.sleep(2)
#     delete = driver.find_element(u.By.XPATH , '//*[@id="tbodyid"]/tr/td[4]/a')
#     delete.click()
#     u.sleep(3)
#
#
#
# Removing_item_from_cart()

#######################################################################################################
# def place_order_button():
#     driver = u.WebDriver.Chrome()
#     driver.get("https://demoblaze.com/index.html")
#     u.sleep(5)
#     driver.find_element(u.By.XPATH , '//*[@id="tbodyid"]/div[5]/div/div/h4/a').click()
#     u.sleep(4)
#     Add_cart_button = driver.find_element(u.By.XPATH , '//*[@id="tbodyid"]/div[2]/div/a')
#     Add_cart_button.click()
#     u.sleep(4)
#     u.WDW(driver, 5).until(u.EC.alert_is_present())
#     alert = driver.switch_to.alert
#     alert.accept()
#     driver.find_element(u.By.XPATH, '//*[@id="cartur"]').click()
#     u.sleep(4)
#     Place_order_button = driver.find_element(u.By.XPATH , '//*[@id="page-wrapper"]/div/div[2]/button')
#     Place_order_button.click()
#     u.sleep(3)
#
# place_order_button()

########################################################################################################

# def purchace_with_valid_data():
#     driver = u.WebDriver.Chrome()
#     driver.get("https://demoblaze.com/index.html")
#     u.sleep(5)
#     driver.find_element(u.By.XPATH, '//*[@id="tbodyid"]/div[5]/div/div/h4/a').click()
#     u.sleep(5)
#     Add_cart_button = driver.find_element(u.By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a')
#     Add_cart_button.click()
#     u.sleep(5)
#     u.WDW(driver, 5).until(u.EC.alert_is_present())
#     alert = driver.switch_to.alert
#     alert.accept()
#     driver.find_element(u.By.XPATH, '//*[@id="cartur"]').click()
#     u.sleep(4)
#     Place_order_button = driver.find_element(u.By.XPATH, '//*[@id="page-wrapper"]/div/div[2]/button')
#     Place_order_button.click()
#     u.sleep(5)
#     name_field = driver.find_element(u.By.XPATH, '//*[@id="name"]')
#     country_filed = driver.find_element(u.By.XPATH, '//*[@id="country"]')
#     city_filed = driver.find_element(u.By.XPATH, '//*[@id="city"]')
#     credit_card_filed = driver.find_element(u.By.XPATH, '//*[@id="card"]')
#     month_filed = driver.find_element(u.By.XPATH, '//*[@id="month"]')
#     year_filed = driver.find_element(u.By.XPATH, '//*[@id="year"]')
#
#     name_field.send_keys("nir_peled")
#     country_filed.send_keys("israel")
#     city_filed.send_keys("shoam")
#     credit_card_filed.send_keys("51159876543654")
#     month_filed.send_keys("14.6")
#     year_filed.send_keys("2001")
#
#     u.sleep(4)
#     purchase = driver.find_element(u.By.XPATH, '//*[@id="orderModal"]/div/div/div[3]/button[2] ')
#     purchase.click()
#     u.sleep(4)
#
#
# purchace_with_valid_data()


######################################################################################################

# def ok_button_valid():
#     driver = u.WebDriver.Chrome()
#     driver.get("https://demoblaze.com/index.html")
#     u.sleep(5)
#     driver.find_element(u.By.XPATH, '//*[@id="tbodyid"]/div[5]/div/div/h4/a').click()
#     u.sleep(5)
#     Add_cart_button = driver.find_element(u.By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a')
#     Add_cart_button.click()
#     u.sleep(5)
#     u.WDW(driver, 5).until(u.EC.alert_is_present())
#     alert = driver.switch_to.alert
#     alert.accept()
#     driver.find_element(u.By.XPATH, '//*[@id="cartur"]').click()
#     u.sleep(4)
#     Place_order_button = driver.find_element(u.By.XPATH, '//*[@id="page-wrapper"]/div/div[2]/button')
#     Place_order_button.click()
#     u.sleep(5)
#
#     name_field = driver.find_element(u.By.XPATH, '//*[@id="name"]')
#     country_filed = driver.find_element(u.By.XPATH, '//*[@id="country"]')
#     city_filed = driver.find_element(u.By.XPATH, '//*[@id="city"]')
#     credit_card_filed = driver.find_element(u.By.XPATH, '//*[@id="card"]')
#     month_filed = driver.find_element(u.By.XPATH, '//*[@id="month"]')
#     year_filed = driver.find_element(u.By.XPATH, '//*[@id="year"]')
#
#     name_field.send_keys("nir_peled")
#     country_filed.send_keys("israel")
#     city_filed.send_keys("shoam")
#     credit_card_filed.send_keys("51159876543654")
#     month_filed.send_keys("14.6")
#     year_filed.send_keys("2001")
#
#     u.sleep(4)
#     purchase = driver.find_element(u.By.XPATH, '//*[@id="orderModal"]/div/div/div[3]/button[2] ')
#     purchase.click()
#     u.sleep(4)
#     ok_button = driver.find_element(u.By.XPATH, '/html/body/div[10]/div[7]/div/button')
#     ok_button.click()
#     u.sleep(4)
#
# ok_button_valid()


########################################################################################################

# def purchace_invalid_data():
#
#     driver = u.WebDriver.Chrome()
#     driver.get("https://demoblaze.com/index.html")
#     u.sleep(5)
#     driver.find_element(u.By.XPATH, '//*[@id="tbodyid"]/div[6]/div/div/h4/a').click()
#     u.sleep(5)
#     Add_cart_button = driver.find_element(u.By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a')
#     Add_cart_button.click()
#     u.sleep(5)
#     u.WDW(driver, 5).until(u.EC.alert_is_present())
#     alert = driver.switch_to.alert
#     alert.accept()
#     driver.find_element(u.By.XPATH, '//*[@id="cartur"]').click()
#     u.sleep(4)
#     Place_order_button = driver.find_element(u.By.XPATH, '//*[@id="page-wrapper"]/div/div[2]/button')
#     Place_order_button.click()
#     u.sleep(5)
#
#     name_field = driver.find_element(u.By.XPATH, '//*[@id="name"]')
#     country_filed = driver.find_element(u.By.XPATH, '//*[@id="country"]')
#     city_filed = driver.find_element(u.By.XPATH, '//*[@id="city"]')
#     credit_card_filed = driver.find_element(u.By.XPATH, '//*[@id="card"]')
#     month_filed = driver.find_element(u.By.XPATH, '//*[@id="month"]')
#     year_filed = driver.find_element(u.By.XPATH, '//*[@id="year"]')
#
#     name_field.send_keys("!%#^@dscfg")
#     country_filed.send_keys("ndskxmcn")
#     city_filed.send_keys("543gf")
#     credit_card_filed.send_keys("gtrdsx34#%^$#")
#     month_filed.send_keys("%$#@FD")
#     year_filed.send_keys("^TGFD")
#
#     u.sleep(4)
#     purchase = driver.find_element(u.By.XPATH, '//*[@id="orderModal"]/div/div/div[3]/button[2] ')
#     purchase.click()
#     u.sleep(4)
#     ok_button = driver.find_element(u.By.XPATH, '/html/body/div[10]/div[7]/div/button')
#     ok_button.click()
#     u.sleep(4)
#
# purchace_invalid_data()


########################################################################################################


def purchace_valid_data():

    driver = u.WebDriver.Chrome()
    driver.get("https://demoblaze.com/index.html")
    u.sleep(5)
    driver.find_element(u.By.XPATH, '//*[@id="tbodyid"]/div[6]/div/div/h4/a').click()
    u.sleep(5)
    Add_cart_button = driver.find_element(u.By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a')
    Add_cart_button.click()
    u.sleep(5)
    u.WDW(driver, 5).until(u.EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()
    driver.find_element(u.By.XPATH, '//*[@id="cartur"]').click()
    u.sleep(4)
    Place_order_button = driver.find_element(u.By.XPATH, '//*[@id="page-wrapper"]/div/div[2]/button')
    Place_order_button.click()
    u.sleep(5)

    name_field = driver.find_element(u.By.XPATH, '//*[@id="name"]')
    country_filed = driver.find_element(u.By.XPATH, '//*[@id="country"]')
    city_filed = driver.find_element(u.By.XPATH, '//*[@id="city"]')
    credit_card_filed = driver.find_element(u.By.XPATH, '//*[@id="card"]')
    month_filed = driver.find_element(u.By.XPATH, '//*[@id="month"]')
    year_filed = driver.find_element(u.By.XPATH, '//*[@id="year"]')

    name_field.send_keys("Ran")
    country_filed.send_keys("Israel")
    city_filed.send_keys("Holon")
    credit_card_filed.send_keys("1884230548932442")
    month_filed.send_keys("13.4")
    year_filed.send_keys("^2002")

    u.sleep(4)
    purchase = driver.find_element(u.By.XPATH, '//*[@id="orderModal"]/div/div/div[3]/button[2] ')
    purchase.click()
    u.sleep(4)
    ok_button = driver.find_element(u.By.XPATH, '/html/body/div[10]/div[7]/div/button')
    ok_button.click()
    u.sleep(4)

purchace_valid_data()