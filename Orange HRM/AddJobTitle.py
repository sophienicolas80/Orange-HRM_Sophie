# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AddJobTitle(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        
    def test_add_job_title(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        
        
    def login(self, username, password):
        self.driver.get("  /")
        self.driver.find_element(By.NAME, "username").clear()
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").clear()
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
    
    
        
        
    def test(self):
        driver = self.driver

        # Partie 1 - Login
        self.login("Admin", "admin123")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div/div/div/div[2]").click()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div/div/div/div[2]").click()
        driver.find_element(By.NAME,"password").click()
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div/aside/nav/div[2]/ul/li/a/span").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div/header/div[2]/nav/ul/li[2]/span").click()
        driver.find_element(By.LINK_TEXT,"Job Titles").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewJobTitleList")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/div/div/button/i").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/saveJobTitle")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div/div[2]/input").click()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div/div[2]/input").clear()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div/div[2]/input").send_keys("Product Definition")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/form/div[2]/div/div[2]/textarea").click()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/form/div[2]/div/div[2]/textarea").clear()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/form/div[2]/div/div[2]/textarea").send_keys("_analyse requirements\n_ specify needs\n_ manage bugs\n_coordinate projects")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/form/div[4]/div/div[2]/textarea").click()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/form/div[4]/div/div[2]/textarea").clear()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/form/div[4]/div/div[2]/textarea").send_keys("good communication skills needed")
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewJobTitleList")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/div[3]/div/div[2]/div[17]/div/div[4]/div/button[2]/i").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/saveJobTitle/33")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/form/div[5]/button").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewJobTitleList")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/div[3]/div/div[2]/div[17]/div/div[4]/div/button/i").click()
        driver.find_element(By.XPATH,"//div[@id='app']/div[3]/div/div/div/div[3]/button[2]").click()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div/header/div/div[2]/ul/li/span/i").click()
        driver.find_element(By.LINK_TEXT,"Logout").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
