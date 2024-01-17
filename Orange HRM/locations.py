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

        # Partie 2 - Aller dans Admin/Organization/Locations
        # Search Texas
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div/aside/nav/div[2]/ul/li/a/span").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div/header/div[2]/nav/ul/li[3]/span").click()
        driver.find_element(By.LINK_TEXT,"Locations").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewLocations")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div/div/div[2]/input").click()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div/div/div[2]/input").clear()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div/div/div[2]/input").send_keys("Texas")
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(3)
        #vérifier qu'il y a Texas dans City
        self.assertTrue(self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[3]/div").is_displayed())
        
        x = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[3]/div").text
        print("x=", x)
        self.assertEqual(x, "Texas")
        #self.assertEqual(repr(x), "Texas")
        
        
        
         # Compte le nombre d'elements selon la pagination (numeros de pages)
        total_count = 0
        while True:

            # Enregistrez le contenu de la liste 
            locations_list = driver.find_elements(By.CLASS_NAME, "oxd-table-card")

            count_on_page = len(locations_list)

            # Accumuler le total
            total_count += count_on_page

            print(f'Page actuelle: {count_on_page} éléments sur la premiere page | Total jusqu à présent: {total_count} éléments')
           
            if count_on_page < 50 :
                # Pas de page suivante, sortie de la boucle
                break

            next_page_button = self.driver.find_element(By.XPATH, "//button[@class='oxd-pagination-page-item oxd-pagination-page-item--previous-next']")
            # next_page_button.click()
            elements = driver.find_elements(By.XPATH, "//button[@class='oxd-pagination-page-item oxd-pagination-page-item--previous-next']/i[@class='oxd-icon bi-chevron-right']")
            
            # //ul[@class='oxd-pagination__ul']/li
            elementsCount = driver.find_elements(By.XPATH, "//ul[@class='oxd-pagination__ul']/li")
            print("COUNT li", len(elementsCount))

            if len(elements) == 1:
                next_page_button.click()
            else :
                # Pas de page suivante, sortie de la boucle
                break
        
        

        self.assertEqual(total_count, 1)
        
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewLocations")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div[2]/div/div/button").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/saveLocation")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div/div/div/div[2]/input").click()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div/div/div/div[2]/input").clear()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div/div/div/div[2]/input").send_keys("Sophie")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/form/div[2]/div/div/div/div[2]/input").click()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/form/div[2]/div/div/div/div[2]/input").clear()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/form/div[2]/div/div/div/div[2]/input").send_keys("Antibes")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/form/div[2]/div/div[3]/div/div[2]/input").click()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/form/div[2]/div/div[3]/div/div[2]/input").clear()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/form/div[2]/div/div[3]/div/div[2]/input").send_keys("06600")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/form/div[2]/div/div[5]/div/div[2]/input").click()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/form/div[2]/div/div[5]/div/div[2]/input").clear()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/form/div[2]/div/div[5]/div/div[2]/input").send_keys("99999")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/form/div[2]/div/div[7]/div/div[2]/textarea").click()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/form/div[2]/div/div[7]/div/div[2]/textarea").clear()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/form/div[2]/div/div[7]/div/div[2]/textarea").send_keys("1ere avenue")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/form/div[2]/div/div[4]/div/div[2]/div/div/div[2]/i").click()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/form/div[2]/div/div[4]/div/div[2]/div/div").click()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/form/div[2]/div/div[4]/div/div[2]/div/div").click()
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewLocations")
          # Compte le nombre d'elements selon la pagination (numeros de pages)
        total_count = 0
        while True:

            # Enregistrez le contenu de la liste 
            locations_list = driver.find_elements(By.CLASS_NAME, "oxd-table-card")

            count_on_page = len(locations_list)

            # Accumuler le total
            total_count += count_on_page

            print(f'Page actuelle: {count_on_page} éléments sur la premiere page | Total jusqu à présent: {total_count} éléments')
           
            if count_on_page < 50 :
                # Pas de page suivante, sortie de la boucle
                break

            next_page_button = self.driver.find_element(By.XPATH, "//button[@class='oxd-pagination-page-item oxd-pagination-page-item--previous-next']")
            # next_page_button.click()
            elements = driver.find_elements(By.XPATH, "//button[@class='oxd-pagination-page-item oxd-pagination-page-item--previous-next']/i[@class='oxd-icon bi-chevron-right']")
            
            # //ul[@class='oxd-pagination__ul']/li
            elementsCount = driver.find_elements(By.XPATH, "//ul[@class='oxd-pagination__ul']/li")
            print("COUNT li", len(elementsCount))

            if len(elements) == 1:
                next_page_button.click()
            else :
                # Pas de page suivante, sortie de la boucle
                break
        
        

        self.assertEqual(total_count, 5)
        
        
        
        
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div/div/div[2]/input").click()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div/div/div[2]/input").clear()
    
        
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