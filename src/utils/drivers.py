from selenium import webdriver
from selenium.webdriver.chrome.service import Service as SC
from selenium.webdriver.edge.service import Service as SE

class Drivers:

    def __init__(self, driver):
        self.driver = driver

    def get_chrome_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-extensions")
        service = SC(executable_path="C:/WebDrivers/chromedriver_win32/chromedriver.exe")
        self.driver = webdriver.Chrome(service=service, options=options)

        return self.driver


    def get_edge_driver(self):
        options = webdriver.EdgeOptions()
        options.add_argument("--disable-extensions")
        service = SE(executable_path="C:/WebDrivers/edgedriver_win32/msedgedriver.exe")
        self.driver = webdriver.Edge(service=service, options=options)

        return self.driver

