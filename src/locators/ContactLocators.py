from selenium.webdriver.common.by import By

contactlocs = dict()

contactlocs['Email_fld'] = (By.CSS_SELECTOR, "#recipient-email")
contactlocs['Name_fld'] = (By.CSS_SELECTOR, "#recipient-name")
contactlocs['Message_fld'] = (By.CSS_SELECTOR, "#message-text")
contactlocs['X_btn'] = (By.CSS_SELECTOR, "#exampleModal > div > div > div.modal-header > button > span")
contactlocs['Close_btn'] = (By.CSS_SELECTOR, "#exampleModal > div > div > div.modal-footer > button.btn.btn-secondary")
contactlocs['Send_msg_btn'] = (By.CSS_SELECTOR, "#exampleModal > div > div > div.modal-footer > button.btn.btn-primary")