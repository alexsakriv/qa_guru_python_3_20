from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


options = UiAutomator2Options().load_capabilities({
    "platformName" : "android",
    "platformVersion" : "9.0",
    "deviceName" : "Google Pixel 3",

    "app" : "bs://c700ce60cf13ae8ed97705a55b8e022f13c5827c",

    'bstack:options' : {
        "projectName" : "First Python project",
        "buildName" : "browserstack-build-DEMO ",
        "sessionName" : "BStack first_test",

        "userName" : "bsuser_SVIJ06",
        "accessKey" : "Q1jNo6Qz6PWxi1WpwJ8e"
    }
})


def test_search_wikipedia():

    driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)

    search_element = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia"))
    )
    search_element.click()
    search_input = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text"))
    )
    search_input.send_keys("BrowserStack")
    time.sleep(5)
    search_results = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
    assert (len(search_results) > 0)

    driver.quit()


def test_search_allure():
    driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)

    search_element = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia"))
    )
    search_element.click()
    search_input = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text"))
    )
    search_input.send_keys("Allure")
    time.sleep(5)
    search_results = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
    assert (len(search_results) > 0)

    driver.quit()