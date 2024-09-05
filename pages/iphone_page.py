from selenium.webdriver.common.by import By


class Iphone_Page:
    #Locators
    RESULTS = (By.XPATH ,"//div[@class = 'sg-col sg-col-4-of-12 sg-col-8-of-16 sg-col-12-of-20 s-list-col-right']")
    RESULTS_PRODUCTS_TITLE = (By.XPATH, "//div[@class = 'sg-col sg-col-4-of-12 sg-col-8-of-16 sg-col-12-of-20 s-list-col-right']/div[@class = 'sg-col-inner']/div[@class = 'a-section a-spacing-small a-spacing-top-small']/div[@class = 'a-section a-spacing-none puis-padding-right-small s-title-instructions-style']/h2[@class = 'a-size-mini a-spacing-none a-color-base s-line-clamp-2']/a[@class = 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']/span[@class = 'a-size-medium a-color-base a-text-normal']")
    
    def __init__(self, driver):
        self.driver = driver

    def get_Results(self):
        """"
        Count total no. of iphone from Results
        """
        count_results = self.driver.find_elements(*Iphone_Page.RESULTS)
        return (len(count_results))

    def get_Results_Products_title(self):
        """"
        Click on 4th iphone
        """
        product_title = []
        i = 0
        count_results = self.driver.find_elements(*Iphone_Page.RESULTS_PRODUCTS_TITLE)
        for count in count_results:
            product_title.append(count.text)
            i = i + 1
            if i == 4:
                count.click()
        return product_title
    
    
        

