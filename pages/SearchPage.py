from selenium.webdriver.common.by import By


class SearchPage:

    def __init__(self, driver):
        self.driver = driver

    valid_hp_product_link_text = "HP LP3065"
    no_product_msg_xpath = "//input[@id='button-search']/following-sibling::p"

    def status_of_valid_hp_product(self):
        return self.driver.find_element(By.LINK_TEXT, self.valid_hp_product_link_text).is_displayed()

    def retrieve_no_product_msg(self):
        return self.driver.find_element(By.XPATH, self.no_product_msg_xpath).text
