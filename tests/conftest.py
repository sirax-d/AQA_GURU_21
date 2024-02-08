import os
import pytest

from appium import webdriver
from dotenv import load_dotenv
from appium.options.android import UiAutomator2Options
from selene import browser

load_dotenv()
login = os.environ.get('user_name')
password = os.environ.get('access_key')


@pytest.fixture(scope='function')
def mobile_management_android():
    options = UiAutomator2Options().load_capabilities({
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",

        "app": "bs://sample.app",

        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",

            "userName": login,
            "accessKey": password
        }
    })

    browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)

    yield
    browser.quit()