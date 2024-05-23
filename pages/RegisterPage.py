from selenium.webdriver.common.by import By

from pages.AccountSuccessPage import AccountSuccessPage


class RegisterPage:

    def __init__(self, driver):
        self.driver = driver

    first_name_field_id = "input-firstname"
    last_name_field_id = "input-lastname"
    email_field_id = "input-email"
    telephone_field_id = "input-telephone"
    password_field_id = "input-password"
    confirm_password_field_id = "input-confirm"
    agree_field_name = "agree"
    continue_button_xpath = "//input[@value='Continue']"
    yes_radio_button_xpath = "//input[@name='newsletter'][@value='1']"
    email_warning_message_xpath = "//*[@id='account-register']/div[1]"
    privacy_policy_message_xpath = "//*[@id='account-register']/div[1]"
    first_name_warning_message_xpath = "//input[@id='input-firstname']/following-sibling::div"
    last_name_warning_message_xpath = "//*[@id='account']/div[3]/div/div"
    register_email_warning_message_xpath = "//*[@id='account']/div[4]/div/div"
    telephone_warning_message_xpath = "//*[@id='account']/div[5]/div/div"
    password_warning_message_xpath = "//*[@id='content']/form/fieldset[2]/div[1]/div/div"

    def enter_first_name(self, first_name_text):
        self.driver.find_element(By.ID, self.first_name_field_id).click()
        self.driver.find_element(By.ID, self.first_name_field_id).clear()
        self.driver.find_element(By.ID, self.first_name_field_id).send_keys(first_name_text)

    def enter_last_name(self, last_name_text):
        self.driver.find_element(By.ID, self.last_name_field_id).click()
        self.driver.find_element(By.ID, self.last_name_field_id).clear()
        self.driver.find_element(By.ID, self.last_name_field_id).send_keys(last_name_text)

    def enter_email(self, email_text):
        self.driver.find_element(By.ID, self.email_field_id).click()
        self.driver.find_element(By.ID, self.email_field_id).clear()
        self.driver.find_element(By.ID, self.email_field_id).send_keys(email_text)

    def enter_telephone(self, telephone_text):
        self.driver.find_element(By.ID, self.telephone_field_id).click()
        self.driver.find_element(By.ID, self.telephone_field_id).clear()
        self.driver.find_element(By.ID, self.telephone_field_id).send_keys(telephone_text)

    def enter_password(self, password_text):
        self.driver.find_element(By.ID, self.password_field_id).click()
        self.driver.find_element(By.ID, self.password_field_id).clear()
        self.driver.find_element(By.ID, self.password_field_id).send_keys(password_text)

    def enter_confirm_password(self, confirm_password_text):
        self.driver.find_element(By.ID, self.confirm_password_field_id).click()
        self.driver.find_element(By.ID, self.confirm_password_field_id).clear()
        self.driver.find_element(By.ID, self.confirm_password_field_id).send_keys(confirm_password_text)

    def select_agree_checkbox_field(self):
        self.driver.find_element(By.NAME, self.agree_field_name).click()

    def click_on_continue_button(self):
        self.driver.find_element(By.XPATH, self.continue_button_xpath).click()
        return AccountSuccessPage(self.driver)

    def click_on_yes_radio_button_option(self):
        self.driver.find_element(By.XPATH, self.yes_radio_button_xpath).click()

    def register_an_account(self,first_name_text,last_name_text,email_text,telephone_text,password_text,confirm_password_text,yes_or_no,privacy_policy):
        self.enter_first_name(first_name_text)
        self.enter_last_name(last_name_text)
        self.enter_email(email_text)
        self.enter_telephone(telephone_text)
        self.enter_password(password_text)
        self.enter_confirm_password(confirm_password_text)
        if yes_or_no.__eq__("yes"):
            self.click_on_yes_radio_button_option()
        if privacy_policy.__eq__("select"):
            self.select_agree_checkbox_field()
        return self.click_on_continue_button()


    def retrieve_duplicate_email_warning_message(self):
        return self.driver.find_element(By.XPATH, self.email_warning_message_xpath).text

    def retrieve_privacy_policy_warning_message(self):
        return self.driver.find_element(By.XPATH, self.privacy_policy_message_xpath).text

    def retrieve_first_name_warning_message(self):
        return self.driver.find_element(By.XPATH, self.first_name_warning_message_xpath).text

    def retrieve_last_name_warning_message(self):
        return self.driver.find_element(By.XPATH, self.last_name_warning_message_xpath).text

    def retrieve_register_email_warning_message(self):
        return self.driver.find_element(By.XPATH, self.register_email_warning_message_xpath).text

    def retrieve_telephone_warning_message(self):
        return self.driver.find_element(By.XPATH, self.telephone_warning_message_xpath).text

    def retrieve_password_warning_message(self):
        return self.driver.find_element(By.XPATH, self.password_warning_message_xpath).text

    def verify_all_warnings(self,expected_privacy_policy_warning_message,expected_first_name_warning_message,expected_last_name_warning_message,expected_email_warning_message,expected_telephone_warning_message,expected_password_warning_message):
        actual_privacy_policy_warning= self.retrieve_privacy_policy_warning_message()
        actual_first_name_warning=self.retrieve_first_name_warning_message()
        actual_last_name_warning=self.retrieve_last_name_warning_message()
        actual_register_email_warning=self.retrieve_register_email_warning_message()
        actual_telephone_warning= self.retrieve_telephone_warning_message()
        actual_password_warning=self.retrieve_password_warning_message()
        status = False

        if expected_privacy_policy_warning_message.__contains__(actual_privacy_policy_warning):
            if expected_first_name_warning_message.__eq__(actual_first_name_warning):
                if expected_last_name_warning_message.__eq__(actual_last_name_warning):
                    if expected_email_warning_message.__eq__(actual_register_email_warning):
                        if expected_telephone_warning_message.__eq__(actual_telephone_warning):
                            if expected_password_warning_message.__eq__(actual_password_warning):
                                status=True
        return status

