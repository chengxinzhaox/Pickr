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


class TestChangePassword:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_changePassword(self):
        self.driver.get("http://127.0.0.1:8000?test_name=change_password")
        time.sleep(2)
        self.driver.set_window_size(1800, 1043)
        self.driver.find_element(By.LINK_TEXT, "My Pickr↗").click()
        self.driver.find_element(By.ID, "user_name").click()
        self.driver.find_element(By.ID, "user_name").send_keys("202018020317")
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("123456")
        self.driver.find_element(By.CSS_SELECTOR, ".submit-button").click()
        self.driver.find_element(By.CSS_SELECTOR, "section:nth-child(4)").click()
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        ".paragraph:nth-child(6)").text == "In this page,you can full the application form and check your topic apply result."
        self.driver.find_element(By.CSS_SELECTOR, ".small_link:nth-child(4) > em").click()
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("1234567890")
        self.driver.find_element(By.ID, "confirm").click()
        self.driver.find_element(By.ID, "confirm").send_keys("1234567890")
        self.driver.find_element(By.CSS_SELECTOR, ".submit-button").click()
        self.driver.find_element(By.XPATH, "//em[contains(.,\'Logout↗\')]").click()
        self.driver.find_element(By.LINK_TEXT, "My Pickr↗").click()
        self.driver.find_element(By.ID, "user_name").click()
        self.driver.find_element(By.ID, "user_name").send_keys("202018020317")
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("1234567890")
        self.driver.find_element(By.CSS_SELECTOR, ".submit-button").click()
        self.driver.find_element(By.XPATH, "//em[contains(.,\'Logout↗\')]").click()