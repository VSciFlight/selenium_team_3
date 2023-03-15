from selenium.webdriver.common.by import By

cartlocs = dict()

cartlocs['Place_order_btn'] = (By.CSS_SELECTOR, "#page-wrapper > div > div.col-lg-1 > button")
cartlocs['Name_fld'] = (By.CSS_SELECTOR, "#name")
cartlocs['Country_fld'] = (By.CSS_SELECTOR, "#country")
cartlocs['City_fld'] = (By.CSS_SELECTOR, "#city")
cartlocs['Credit_card_fld'] = (By.CSS_SELECTOR, "#card")
cartlocs['Month_fld'] = (By.CSS_SELECTOR, "#month")
cartlocs['Year_fld'] = (By.CSS_SELECTOR, "/html/body/div[3]/div/div/div[2]/form/div[6]/input")
cartlocs['X_btn'] = (By.CSS_SELECTOR, "#orderModal > div > div > div.modal-header > button > span")
cartlocs['Close_btn'] = (By.CSS_SELECTOR, "#orderModal > div > div > div.modal-footer > button.btn.btn-secondary")
cartlocs['Purchase_btn'] = (By.CSS_SELECTOR, "#orderModal > div > div > div.modal-footer > button.btn.btn-primary")
cartlocs['Delete_btn'] = (By.CSS_SELECTOR, "#orderModal > div > div > div.modal-header > button > span")
