from selenium.webdriver.common.by import By



homelocs = dict()

# Header
homelocs['Home'] = (By.CSS_SELECTOR, "#navbarExample > ul > li.nav-item.active > a")
homelocs['Contact'] = (By.CSS_SELECTOR, "#navbarExample > ul > li:nth-child(2) > a")
homelocs['AboutUs'] = (By.CSS_SELECTOR, "#navbarExample > ul > li:nth-child(3) > a")
homelocs['Cart'] = (By.CSS_SELECTOR, "#cartur")
homelocs['LogIn'] = (By.CSS_SELECTOR, "#login2")
homelocs['SignUp'] = (By.CSS_SELECTOR, "#signin2")
homelocs['LogOut'] = (By.CSS_SELECTOR, "#logout2")
homelocs['Logo']  = (By.CSS_SELECTOR, "#nava")

# Slide Show = slsh
homelocs['slsh_right_arrow'] = (By.CSS_SELECTOR, "#carouselExampleIndicators > a.carousel-control-next > span.carousel-control-next-icon")
homelocs['slsh_left_arrow'] = (By.CSS_SELECTOR, "#carouselExampleIndicators > a.carousel-control-prev > span.carousel-control-prev-icon")
homelocs['slsh_left_indicator'] = (By.CSS_SELECTOR, "#carouselExampleIndicators > ol > li.active")
homelocs['slsh_middle_indicator'] = (By.CSS_SELECTOR, "#carouselExampleIndicators > ol > li.active")
homelocs['slsh_right_indicator'] = (By.CSS_SELECTOR, "#carouselExampleIndicators > ol > li.active")

# Body
homelocs['Categories'] = (By.CSS_SELECTOR, "#cat")
homelocs['Phones'] = (By.XPATH, '//*[@id="itemc"]')
homelocs['Laptops'] = (By.CSS_SELECTOR, "#itemc")
homelocs['Monitors'] = (By.XPATH, "/html/body/div[5]/div/div[1]/div/a[4]")
homelocs['Item'] = (By.CSS_SELECTOR, "#tbodyid > div:nth-child(1) > div > div > h4 > a")
homelocs['Previous'] = (By.CSS_SELECTOR, "#prev2")
homelocs['Next'] = (By.CSS_SELECTOR, "#next2")