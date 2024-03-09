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

class TestManagerViewStudentSelection():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_managerViewStudentSelection(self):
    self.driver.get("http://127.0.0.1:8000?test_name=student_selection")
    self.driver.find_element(By.LINK_TEXT, "My Pickr↗").click()
    self.driver.find_element(By.ID, "user_name").click()
    self.driver.find_element(By.ID, "user_name").send_keys("Joojo")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("123456")
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".submit-button").click()
    time.sleep(1)
    self.driver.find_element(By.LINK_TEXT, "Process").click()
    time.sleep(1)
    self.driver.find_element(By.ID, "fail_students").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".close").click()
    time.sleep(1)
    self.driver.find_element(By.LINK_TEXT, "Refresh").click()
    time.sleep(1)
    self.driver.find_element(By.LINK_TEXT, "Custom Topics").click()
    time.sleep(1)
    self.driver.find_element(By.LINK_TEXT, "Check").click()
    time.sleep(1)
    self.driver.find_element(By.ID, "type").click()
    time.sleep(1)
    dropdown = self.driver.find_element(By.ID, "type")
    time.sleep(1)
    dropdown.find_element(By.XPATH, "//option[. = 'type6']").click()
    time.sleep(1)
    self.driver.find_element(By.ID, "description").click()
    time.sleep(1)
    self.driver.find_element(By.ID, "description").send_keys("custom description add something")
    time.sleep(1)
    self.driver.find_element(By.ID, "status").click()
    time.sleep(1)
    dropdown = self.driver.find_element(By.ID, "status")
    time.sleep(1)
    dropdown.find_element(By.XPATH, "//option[. = 'Passed Verify']").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".submit-button").click()
    time.sleep(1)
    self.driver.find_element(By.LINK_TEXT, "System").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".small_link:nth-child(3) > em").click()
  
