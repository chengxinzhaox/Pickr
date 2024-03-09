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


class TestManagerSetNotesTypes():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_managerSetNotesTypes(self):
        self.driver.get("http://127.0.0.1:8000?test_name=login")
        self.driver.find_element(By.LINK_TEXT, "My Pickr↗").click()
        self.driver.find_element(By.ID, "user_name").click()
        self.driver.find_element(By.ID, "user_name").send_keys("Joojo")
        self.driver.find_element(By.ID, "password").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "password").send_keys("123456")
        self.driver.find_element(By.CSS_SELECTOR, ".submit-button").click()
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, "+ New Note").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "title").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "title").send_keys("test title")
        self.driver.find_element(By.ID, "content").click()
        self.driver.find_element(By.ID, "content").send_keys("test content")
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".submit-button").click()
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, "Edit").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "title").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "title").send_keys("test title 1")
        time.sleep(1)
        self.driver.find_element(By.ID, "content").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "content").send_keys("test content1")
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".submit-button").click()
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, "Delete").click()
        time.sleep(1)
        assert self.driver.switch_to.alert.text == "Are you sure you want to delete this topic?"
        self.driver.switch_to.alert.accept()
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, "+ New Type").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "name").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "name").send_keys("4D Game")
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".submit-button").click()
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, "Edit").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "name").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "name").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "name").send_keys("3D Game")
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".submit-button").click()
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, "Delete").click()
        time.sleep(1)
        assert self.driver.switch_to.alert.text == "Are you sure you want to delete this type?"
        time.sleep(1)
        self.driver.switch_to.alert.accept()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.find_element(By.CSS_SELECTOR, ".small_link:nth-child(3) > em").click()
