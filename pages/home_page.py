from selenium.webdriver.common.by import By


class Home_Page:
    #Locators
    SEARCH_INPUT = (By.XPATH ,"//input[@id='twotabsearchtextbox']")
    
    def __init__(self, driver, search_product):
        self.driver = driver
        # self.iphone = iphone
        self.search_product = search_product

    def Search_iphone(self):
        """"
        Search iphone from search box
        """
        return self.driver.find_element(*Home_Page.SEARCH_INPUT).send_keys(self.search_product)
