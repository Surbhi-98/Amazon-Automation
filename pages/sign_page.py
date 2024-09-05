from selenium.webdriver.common.by import By


class Sign_Page:
    #Locators
    EMAIL_ID = (By.ID ,"ap_email")
    PASSWORD = (By.ID, "ap_password")
    CONTINUE_BUTTON = (By.XPATH, "//input[@class = 'a-button-input']")
    SIGN_BUTTON = (By.ID, "signInSubmit")
    INCORRECT_ALERT_POPUP = (By.XPATH, "//div[@class='a-box-inner a-alert-container']/div/ul/li/span[@class= 'a-list-item']")
    # INCORRECT_ALERT_EMAIL_POPUP = (By.XPATH, "//body/div/div/div[@id = 'authportal-center-section']/div/div/div/div/div/div/ul/li/span[@class = 'a-list-item']")
    INCORRECT_ALERT_EMAIL_POPUP = (By.XPATH, "//div[@class='a-box-inner a-alert-container']/div/ul/li/span[@class= 'a-list-item']")
   
    def __init__(self, driver, user_name, password):
        self.driver = driver
        self.user_name = user_name
        self.password = password
    
    #Enter Email Id
    def enter_email_id(self):
        return self.driver.find_element(*Sign_Page.EMAIL_ID).send_keys(self.user_name)

    def click_continue_button(self):
        """"
        Click on continue button
        """
        return self.driver.find_element(*Sign_Page.CONTINUE_BUTTON).click()

    def enter_password(self):
        """"
        Enter password
        """
        return self.driver.find_element(*Sign_Page.PASSWORD).send_keys(self.password)

    def click_sign_button(self):
        """"
        Click on sign button
        """
        return self.driver.find_element(*Sign_Page.SIGN_BUTTON).click()

    def incorrect_password_popup(self):
        """"
        Get error message for password
        """
        alert_message = self.driver.find_element(*Sign_Page.INCORRECT_ALERT_POPUP).text
        return alert_message

    def close_new_tab(self):
        """"
        Close new tab
        """
        self.driver.close()
        windows_open = self.driver.window_handles
        return self.driver.switch_to.window(windows_open[0])

    




