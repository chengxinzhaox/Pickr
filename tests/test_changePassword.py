# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium_test import SeleniumTest


class TestChangePassword(SeleniumTest):
    """
    Test the change password feature

    1. Login
    2. Click on the username
    3. Click on the change password link
    4. Enter the old password
    5. Enter the new password
    6. Confirm the new password
    7. Click on the submit button
    8. Logout
    """

    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_changePassword(self):
        self.driver.get("http://127.0.0.1:8000?test_name=change_password")
        time.sleep(1)
        self.driver.set_window_size(1800, 1043)
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, "My Pickr↗").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "user_name").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "user_name").send_keys("202018020317")
        time.sleep(1)
        self.driver.find_element(By.ID, "password").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "password").send_keys("123456")
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".submit-button").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "section:nth-child(4)").click()
        time.sleep(1)
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        ".paragraph:nth-child(6)").text == "In this page,you can full the application form and check your topic apply result."
        self.driver.find_element(By.CSS_SELECTOR, ".small_link:nth-child(4) > em").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "password").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "password").send_keys("1234567890")
        time.sleep(1)
        self.driver.find_element(By.ID, "confirm").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "confirm").send_keys("1234567890")
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".submit-button").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//em[contains(.,\'Logout↗\')]").click()
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, "My Pickr↗").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "user_name").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "user_name").send_keys("202018020317")
        time.sleep(1)
        self.driver.find_element(By.ID, "password").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "password").send_keys("1234567890")
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".submit-button").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//em[contains(.,\'Logout↗\')]").click()
