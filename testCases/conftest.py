from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
        print("launching Chome Browser")
    elif browser=='firefox':
        driver=webdriver.Firefox()
        print("launching firefox Browser")
    else:
        driver =webdriver.Edge()
        print("launching edge Browser")
    return driver


def pytest_addoption(parser): # this will get the value from CLI / Hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): # this will return the browser value to setup method
    return request.config.getoption("--browser")


# it is hooks for Adding Environment info to HTML Reports

def pytest_configure(config):
    config.addinivalue_line('markers', 'Project Name: nop commerce')
    config.addinivalue_line('markers', 'Module Name: Customer')
    config.addinivalue_line('markers', 'Tester Name: Akash Jadhav')

@pytest.mark.optionhooks
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)