# Generated by Selenium IDE
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium_test import SeleniumTest


class TestStudentSelectTopics(SeleniumTest):
    """
    This test method tests the student's ability to select topics

    1. The student logs in
    2. The student selects the topics and deselect the topics
    3. The student logs out
    """

    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_studentSelectTopics(self):
        self.driver.get("http://127.0.0.1:8000?test_name=student_select_topics")
        time.sleep(2)

        self.driver.find_element(By.LINK_TEXT, "My Pickr↗").click()
        self.driver.find_element(By.ID, "user_name").click()
        self.driver.find_element(By.ID, "user_name").send_keys("202018020317")
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("123456")
        self.driver.find_element(By.CSS_SELECTOR, ".submit-button").click()
        time.sleep(1)
        self.driver.find_element(By.NAME, "choose1").click()
        self.driver.find_element(By.NAME, "choose1").send_keys("1")
        self.driver.find_element(By.NAME, "choose1").send_keys(Keys.ENTER)
        time.sleep(1)
        self.driver.find_element(By.NAME, "choose2").click()
        self.driver.find_element(By.NAME, "choose2").send_keys("3")
        self.driver.find_element(By.NAME, "choose2").send_keys(Keys.ENTER)
        time.sleep(1)
        self.driver.find_element(By.NAME, "choose3").click()
        self.driver.find_element(By.NAME, "choose3").send_keys("5")
        self.driver.find_element(By.NAME, "choose3").send_keys(Keys.ENTER)
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "#choose3_form > .submit-button").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "#choose2_form > .submit-button").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "#choose1_form > .submit-button").click()
        time.sleep(1)
        self.driver.find_element(By.NAME, "choose1").click()
        self.driver.find_element(By.NAME, "choose1").send_keys("3")
        self.driver.find_element(By.NAME, "choose1").send_keys(Keys.ENTER)
        time.sleep(1)
        self.driver.find_element(By.NAME, "choose2").click()
        self.driver.find_element(By.NAME, "choose2").send_keys("5")
        self.driver.find_element(By.NAME, "choose2").send_keys(Keys.ENTER)
        time.sleep(1)
        self.driver.find_element(By.NAME, "choose3").click()
        self.driver.find_element(By.NAME, "choose3").send_keys("7")
        self.driver.find_element(By.NAME, "choose3").send_keys(Keys.ENTER)
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".small_link:nth-child(3) > em").click()
