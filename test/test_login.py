from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from pages.AccountPage import AccountPage
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from test.BaseTest import BaseTest


class TestLogin(BaseTest):
    def test_login_with_valid_credentials(self):
        home_page = HomePage(self.driver)
        login_page=home_page.navigate_to_login_page()
        login_page.login_to_application("pawarvijaymanik@gmail.com","12345")
        expected_text="My Account"
        assert login_page.display_status_of_my_account_option().__contains__(expected_text)

    def test_login_with_invalid_email_and_valid_password(self):
        home_page = HomePage(self.driver)
        login_page=home_page.navigate_to_login_page()
        login_page.login_to_application(self.generate_email_with_time_stamp(),"12345")
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message().__contains__(expected_warning_message)

    def test_login_with_valid_email_and_invalid_password(self):
        home_page = HomePage(self.driver)
        login_page=home_page.navigate_to_login_page()
        login_page.login_to_application("pawarvijaymanik@gmail.com","123456")
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message().__contains__(expected_warning_message)

    def test_login_without_entering_credentials(self):
        home_page = HomePage(self.driver)
        login_page= home_page.navigate_to_login_page()
        login_page.login_to_application("","")
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message().__contains__(expected_warning_message)
