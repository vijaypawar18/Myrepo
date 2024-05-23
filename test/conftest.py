import pytest
from selenium import webdriver

from utilities import ReadConfigurations


@pytest.fixture()
def setup_and_teardown(request):
    browser = ReadConfigurations.read_configurations("basic info","browser")
    if browser.__eq__("edge"):
        from selenium.webdriver.edge.service import Service as EdgeService
        from webdriver_manager.microsoft import EdgeChromiumDriverManager
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    else:
        print("provide valid browser name from this list chrome/firefox/edge")

    driver.maximize_window()
    app_url= ReadConfigurations.read_configurations("basic info","url")
    driver.get(app_url)
    request.cls.driver=driver
    yield
    driver.quit()