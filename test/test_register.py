from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from pages.AccountSuccessPage import AccountSuccessPage
from pages.HomePage import HomePage
from pages.RegisterPage import RegisterPage
from test.BaseTest import BaseTest


class TestRegister(BaseTest):
    def test_register_with_mandatory_fields(self):
        home_page = HomePage(self.driver)
        register_page= home_page.navigate_to_register_page()
        account_success_page= register_page.register_an_account("vijay","pawar",self.generate_email_with_time_stamp(),"9850331183","12345","12345","no","select")
        expected_text = "Your Account Has Been Created!"
        assert account_success_page.retrieve_account_creation_message().__eq__(expected_text)

    def test_register_with_all_fields(self):
        home_page = HomePage(self.driver)
        register_page= home_page.navigate_to_register_page()
        account_success_page= register_page.register_an_account("vijay","pawar",self.generate_email_with_time_stamp(),"9850331183","12345","12345","yes","select")
        expected_text = "Your Account Has Been Created!"
        assert account_success_page.retrieve_account_creation_message().__eq__(expected_text)

    def test_register_with_duplicate_email(self):
        home_page = HomePage(self.driver)
        register_page= home_page.navigate_to_register_page()
        register_page.register_an_account("vijay","pawar","pawarvijaymanik@gmail.com","9850331183","12345","12345","yes","select")
        expected_warning_message ="Warning: E-Mail Address is already registered!"
        assert register_page.retrieve_duplicate_email_warning_message().__contains__(expected_warning_message)

    def test_register_without_entering_any_fields(self):
        home_page = HomePage(self.driver)
        register_page=home_page.navigate_to_register_page()
        register_page.register_an_account("","","","","","","no","no")
        assert register_page.verify_all_warnings("Warning: You must agree to the Privacy Policy!","First Name must be between 1 and 32 characters!","Last Name must be between 1 and 32 characters!","E-Mail Address does not appear to be valid!","Telephone must be between 3 and 32 characters!","Password must be between 4 and 20 characters!")



