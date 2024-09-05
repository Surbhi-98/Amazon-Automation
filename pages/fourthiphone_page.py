from selenium.webdriver.common.by import By


class Fourthiphone_Page:
    #Locators
    BUY_NOW = (By.ID ,"buy-now-button")
    
    def __init__(self, driver):
        self.driver = driver

    def switch_to_new_tab(self):
        """"
        Switch to a new tab
        """
        windows_open = self.driver.window_handles
        return self.driver.switch_to.window(windows_open[1])

    def click_on_buy_now(self):
        """"
        Click on buy now button
        """
        return self.driver.find_element(*Fourthiphone_Page.BUY_NOW).click()
