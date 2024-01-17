# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
import unittest, time, re
from selenium.webdriver import Chrome, ChromeOptions





class TestLocations(unittest.TestCase):

    def login(self, username, password):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element(By.NAME, "username").clear()
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").clear()
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
    
    # Fonction pour le processus de déconnexion
    def logout(self, driver):
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,"//div[@id='app']/div/div/header/div/div[2]/ul/li/span/i").click()
        driver.find_element(By.LINK_TEXT,"Logout").click()
        driver.implicitly_wait(10)
   
    
    def setUp(self):
        opts = ChromeOptions()
        opts.add_argument("--window-size=2560,1440")
        self.driver = webdriver.Chrome(options=opts)
        self.driver.implicitly_wait(10)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test(self):
        driver = self.driver

        # Partie 1 - Login
        self.login("Admin", "admin123")

        # Partie 2 - Créer un employe avec location=Texas
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div[2]/div/button").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee")
        driver.find_element(By.NAME,"firstName").click()
        driver.find_element(By.NAME,"firstName").clear()
        driver.find_element(By.NAME,"firstName").send_keys("AAASophie")
        driver.find_element(By.NAME,"lastName").click()
        driver.find_element(By.NAME,"lastName").clear()
        driver.find_element(By.NAME,"lastName").send_keys("France")
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/54")
        driver.find_element(By.LINK_TEXT,"Job").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewJobDetails/empNumber/54")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div/div/div[6]/div/div[2]/div/div/div[2]/i").click()
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        
        
        
        
        # Search Texas
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
        
        time.sleep(3)
        #vérifier qu'il y a Texas dans City
        self.assertTrue(self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[3]/div").is_displayed())
        
        x = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[3]/div").text
        print("x=", x)
        self.assertEqual(x, "Texas")
        #self.assertEqual(repr(x), "Texas")
        
        
        
         
       
        
        

        self.assertEqual(total_count, 1)
        
        
            
        
        

        
        
        
        
        
    
        
        #Vérifier que Location Sophie a bien été ajouté
        a = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[4]/div/div[2]/div").text
        print("location Sophie=", a)
        self.assertEqual(a, "Sophie")
        
        

        # Partie 4 - Logout
        self.logout(driver)
        
       
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
     unittest.main()