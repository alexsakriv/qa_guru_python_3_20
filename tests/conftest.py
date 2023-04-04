import pytest
from selene.support.shared import browser
from qa_guru_python_3_20.utils import attach
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


@pytest.fixture(autouse=True)
def attach_video():
    options = Options()

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser.config.driver = driver

    yield

    attach.add_video(browser)
    browser.quit()
