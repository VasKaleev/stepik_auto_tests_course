import pytest
from selenium import webdriver
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='Chrome',
        help="Choose browser: Chrome or Firefox")
@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name").capitalize()
    print(f'\nStarting browser {browser_name}.')
    if browser_name == "Chrome":
        browser = webdriver.Chrome()
    elif browser_name == "Firefox":
        browser = webdriver.Firefox()
    else:
        print(f'\nWhoopsie! {browser_name} browser is not supported. Starting Chrome instead')
        browser = webdriver.Chrome()
    yield browser
    print('\nBrowser shutdown.')
    browser.quit()