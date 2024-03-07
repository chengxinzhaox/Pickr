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

class TestManagerSetDeadlin():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_managerSetDeadlin(self):
    self.driver.get("http://127.0.0.1:8000?test_name=login")
    self.driver.find_element(By.LINK_TEXT, "My Pickr↗").click()
    self.driver.find_element(By.ID, "user_name").click()
    self.driver.find_element(By.ID, "user_name").send_keys("Joojo")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("123456")
    self.driver.find_element(By.CSS_SELECTOR, ".submit-button").click()
    time.sleep(1)
    self.driver.find_element(By.ID, "round1-submit-button").click()
    time.sleep(1)
    self.driver.find_element(By.ID, "round1-submit").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".open .today").click()
    time.sleep(1)
    self.driver.find_element(By.ID, "round1-submit").send_keys("2024-03-07 12:00")
    time.sleep(1)
    self.driver.find_element(By.ID, "round1-result").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".open .flatpickr-day:nth-child(33)").click()
    time.sleep(1)
    self.driver.find_element(By.ID, "round1-result").send_keys("2024-03-28 12:00")
    time.sleep(1)
    self.driver.find_element(By.ID, "round1-title").click()
    time.sleep(1)
    self.driver.find_element(By.ID, "round1-title").send_keys("Round I")
    time.sleep(1)
    self.driver.find_element(By.ID, "round1-submit-button").click()
    time.sleep(1)
    self.driver.find_element(By.ID, "round2-submit").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".open .flatpickr-day:nth-child(26)").click()
    time.sleep(1)
    self.driver.find_element(By.ID, "round2-submit").send_keys("2024-03-21 12:00")
    time.sleep(1)
    self.driver.find_element(By.ID, "round2-result").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".open .flatpickr-day:nth-child(28)").click()
    time.sleep(1)
    self.driver.find_element(By.ID, "round2-result").send_keys("2024-03-23 12:00")
    time.sleep(1)
    self.driver.find_element(By.ID, "round2-title").click()
    time.sleep(1)
    self.driver.find_element(By.ID, "round2-title").send_keys("Round II")
    time.sleep(1)
    self.driver.find_element(By.ID, "round2-submit-button").click()
    time.sleep(1)
    self.driver.find_element(By.ID, "round2-submit-button").click()
    time.sleep(1)
    self.driver.find_element(By.ID, "round1-submit-button").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".small_link:nth-child(3) > em").click()
  
