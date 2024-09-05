import time
import pytest
import sys
sys.path.append("/home/cbnits/Documents/Amazon_Assignment/utility")
sys.path.append("/home/cbnits/Documents/Amazon_Assignment/pages")
sys.path.append("/home/cbnits/Documents/Amazon_Assignment/data")
import test_data
import base_script
import home_page
import iphone_page
import fourthiphone_page
import sign_page

class Test_Page(base_script.Base_Script):

    def test_driver(self):
        self.driver.implicitly_wait(10)
        driver = self.driver
        page_title = driver.title
        self.message_logging(page_title)
        # assert page_title == "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in"
        assert page_title == test_data.Test_Data.PAGE_TITLE

    def test_search(self):
        # home_page_driver = home_page.Home_Page(self.driver, test_data.Test_Data.IPHONE)
        home_page_driver = home_page.Home_Page(self.driver, self.search_product)
        home_page_driver.Search_iphone()
        self.wait_search(home_page.Home_Page.SEARCH_INPUT)
        self.message_logging("Iphone Search Successfully")
    
    def test_results(self):
        iphone_page_driver = iphone_page.Iphone_Page(self.driver)
        total_iphone = iphone_page_driver.get_Results()
        # print(total_iphone)
        self.message_logging("Total Iphone from Results " + str(total_iphone))
        title_iphone = iphone_page_driver.get_Results_Products_title()
        # print(title_iphone)
        self.message_logging("Iphone List " + str(title_iphone))
        
    
    def test_fourthiphone_page(self):
        fourthiphone_page_driver = fourthiphone_page.Fourthiphone_Page(self.driver)
        fourthiphone_page_driver.switch_to_new_tab() 
        self.wait_click(fourthiphone_page_driver.BUY_NOW)
        fourthiphone_page_driver.click_on_buy_now()
        self.message_logging("Successfully switch to the new tab and click on Buy Button")

    def test_sign_page(self):
        sign_page_driver = sign_page.Sign_Page(self.driver, self.user_name, self.password)
        # sign_page_driver = sign_page.Sign_Page(self.driver)
        # time.sleep(5)
        sign_page_driver.enter_email_id()
        self.message_logging("Email id Entered") 
        self.wait_click(sign_page_driver.CONTINUE_BUTTON)
        sign_page_driver.click_continue_button()
        self.message_logging("Successfully click to the Continue Button")
        sign_page_driver.enter_password()
        self.message_logging("Password Entered")
        self.wait_click(sign_page_driver.SIGN_BUTTON)
        sign_page_driver.click_sign_button()
        self.message_logging("Successfully click Sign Button")
        alert_message_password = sign_page_driver.incorrect_password_popup()
        print(alert_message_password)
        # alert_message_ = alert_message_password.find("Your password is incorrect")
        try:
            if alert_message_password.find("Your password is incorrect"):
            # assert alert_message_password.find("Your password is incorrect")  
                self.message_logging("Message " + alert_message_password)
            elif alert_message_password.find("To better protect your account, please re-enter your password and then enter the characters as they are shown in the image below."):
                self.message_logging("Message " + alert_message_password)
        except Exception as e:
            self.message_logging(e)
        sign_page_driver.close_new_tab()
        self.message_logging("Sign page closed")



    
    
                
        






