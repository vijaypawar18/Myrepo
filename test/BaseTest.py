from datetime import datetime

import pytest


@pytest.mark.usefixtures("setup_and_teardown")
class BaseTest:

    def generate_email_with_time_stamp(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "pawarvijaymanik" + time_stamp + "@gmail.com"