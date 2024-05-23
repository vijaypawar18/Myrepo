from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    email_field_id = "input-email"
    password_field_id = "input-password"
    login_button_xpath = "//input[@value='Login']"
    warning_message_xpath = "//*[@id='account-login']/div[1]"
    my_account_option_link_text = "My Account"

    def enter_email_field(self, email_address_text):
        self.driver.find_element(By.ID, self.email_field_id).click()
        self.driver.find_element(By.ID, self.email_field_id).clear()
        self.driver.find_element(By.ID, self.email_field_id).send_keys(email_address_text)

    def enter_password_field(self, password_text):
        self.driver.find_element(By.ID, self.password_field_id).click()
        self.driver.find_element(By.ID, self.password_field_id).clear()
        self.driver.find_element(By.ID, self.password_field_id).send_keys(password_text)

    def click_on_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def login_to_application(self,email_address_text,password_text):
        self.enter_email_field(email_address_text)
        self.enter_password_field(password_text)
        return self.click_on_login_button()

    def retrieve_warning_message(self):
        return self.driver.find_element(By.XPATH, self.warning_message_xpath).text

    def display_status_of_my_account_option(self):
        return self.driver.find_element(By.LINK_TEXT, self.my_account_option_link_text).text