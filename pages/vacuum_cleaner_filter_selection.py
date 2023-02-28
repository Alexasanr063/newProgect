
from argparse import Action
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
from pages.main_page import Main_page
#import allure

class Vacuum_cleaner_filter_selection(Main_page):
  
    

    def __init__(self,driver):
        object.__init__(driver)
        self.driver = driver


    #scroll page
    def scroll1(self):
       action = ActionChains(self.driver)
       red_t_short = self.driver.find_element(By.XPATH,"//*[@id='content']/main/app-page-catalog-section/div/div[3]/div[1]/div[2]/app-catalog-filter/div/app-filter-group[6]/app-ui-form-item/app-ui-type-checkbox/div/div[3]/label/span[1]")
       action.move_to_element(red_t_short).perform()
       print("scroll1")

    def chose(self):
       action = ActionChains(self.driver)
       red_t_short = self.driver.find_element(By.XPATH,"//*[@id='content']/main/app-page-catalog-section/div/div[3]/div[1]/div[2]/app-catalog-filter/div/app-filter-group[1]/app-ui-form-item/app-ui-type-range/div[1]/ngx-slider/span[5]")
       action.click_and_hold(red_t_short).move_by_offset(150,0).release().perform()
     
    def get_chois_product_vacuum_cleaner_pickup_dream(self):
        return WebDriverWait(self.driver , 30).until(EC.element_to_be_clickable((By.XPATH,self.chois_product_vacuum_cleaner_pickup_dream)))

    def get_chois_product_vacuum_cleaner_pickup_dream_clining(self):
        return WebDriverWait(self.driver , 30).until(EC.element_to_be_clickable((By.XPATH,self.chois_product_vacuum_cleaner_pickup_dream_clining)))

    def click_select_product_2(self):
        #with allure.step("click_select_product_2"):
            self.chose()
            time.sleep(3)
        
            self.scroll1()
            self.get_chois_product_vacuum_cleaner_pickup_dream().click()
            time.sleep(2)
            self.get_chois_product_vacuum_cleaner_pickup_dream_clining().click()
            time.sleep(2)