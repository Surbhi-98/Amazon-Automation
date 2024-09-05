from curses import KEY_ENTER
import inspect
import logging
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys

@pytest.mark.usefixtures("invoke_driver", "passing_username_password", "search_your_product")
class Base_Script:

    def wait_search(self, path):
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(expected_conditions.presence_of_element_located((path))).send_keys(Keys.ENTER)
            # wait.until(expected_conditions.presence_of_element_located((path)))
        except Exception as e:
             self.message_logging(e) 

    def wait_search_1(self, path):
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(expected_conditions.visibility_of_element_located((path)))
        except Exception as e:
             self.message_logging(e)   

    def wait_click(self, path):
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(expected_conditions.element_to_be_clickable((path)))
        except Exception as e:
            self.message_logging(e)    

    def message_logging(self, message):
        """"
        Create Log file and store info
        """
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        filehandler = logging.FileHandler("/home/cbnits/Documents/Amazon_Assignment/LOG/logfile.log")
        logger.addHandler(filehandler)
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)
        logger.setLevel(logging.INFO)
        logger.info(message)