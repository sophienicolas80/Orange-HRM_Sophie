# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
import unittest, time, re

class TestSauceLab(unittest.TestCase):

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
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test(self):
        driver = self.driver

        # Partie 1 - Login
        self.login("Admin", "admin123")

        # Partie 2 - 
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div/aside/nav/div[2]/ul/li/a/span").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div/header/div[2]/nav/ul/li[2]/span").click()
        driver.find_element(By.LINK_TEXT,"Job Titles").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewJobTitleList")
       
        
        #self.assertTrue(self.driver.find_element(By.XPATH,"////div[@class='orangehrm-container']/div/div/div/div/div/div/div/div/div[@class='header']").is_displayed())
        
        #elements_liste_jobTitles = driver.find_elements(By.CLASS_NAME, "//div[@class='oxd-table-card --mobile']")
        #print("nombre de jobs", len(elements_liste_jobTitles))
        #assert len(elements_liste_jobTitles) == 26, "Le nombre d'éléments dans le panier n'est pas égal à 26"
        
        # Compte le nombre d'elements selon la pagination (numeros de pages)
        total_count = 0
        while True:

            # Enregistrez le contenu de la liste avant l'ajout de l'élément
            job_titles = driver.find_elements(By.XPATH, "//div[@class='oxd-table-card']")

            count_on_page = len(job_titles)

            # Accumuler le total
            total_count += count_on_page

            print(f'Page actuelle: {count_on_page} éléments sur la premiere page | Total jusqu à présent: {total_count} éléments')
            
            if count_on_page < 50 :
                break
            else :
                next_page_button = self.driver.find_element(By.XPATH, "//button[@class='oxd-pagination-page-item oxd-pagination-page-item--previous-next']")

                if 'disabled' in next_page_button.get_attribute('class'):
                    # Pas de page suivante, sortie de la boucle
                    break

                next_page_button.click()

        self.assertEqual(total_count, 32)
        
        
        
        
        
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
        

        
        
        
        total_count = 0
        while True:

            # Enregistrez le contenu de la liste avant l'ajout de l'élément
            job_titles = driver.find_elements(By.XPATH, "//div[@class='oxd-table-card']")

            count_on_page = len(job_titles)

            # Accumuler le total
            total_count += count_on_page

            print(f'Page actuelle: {count_on_page} éléments sur la premiere page | Total jusqu à présent: {total_count} éléments')
            
            if count_on_page < 50 :
                break
            else :
                next_page_button = self.driver.find_element(By.XPATH, "//button[@class='oxd-pagination-page-item oxd-pagination-page-item--previous-next']")

                if 'disabled' in next_page_button.get_attribute('class'):
                    # Pas de page suivante, sortie de la boucle
                    break

                next_page_button.click()

        self.assertEqual(total_count, 33)     
        
        
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/div[3]/div/div[2]/div[17]/div/div[4]/div/button[2]/i").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/saveJobTitle/33")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/form/div[5]/button").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewJobTitleList")
        
       
        
        
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/div[3]/div/div[2]/div[17]/div/div[4]/div/button/i").click()
        driver.find_element(By.XPATH,"//div[@id='app']/div[3]/div/div/div/div[3]/button[2]").click()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div/header/div/div[2]/ul/li/span/i").click()
        
        # Partie 4 - Logout
        self.logout(driver)
        
       
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
     unittest.main()