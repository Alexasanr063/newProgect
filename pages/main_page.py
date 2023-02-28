#import allure
from argparse import Action
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
#from pages.vacuum_cleaner_filter_selection import Vacuum_cleaner_filter_selection
#from pages.last_page import Last_page
from base.base_class import Base
#from utilities.loger import Logger


class Main_page(Base):
    url = 'https://www.maunfeld.ru/'
    

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver


    #Locators
    chois_product_1 = "//*[@id='headerId']/div/div[1]/div[2]/div/div/div/div[2]/div[1]/span[2]"
    chois_product_vacuum_cleaner = "//*[@id='headerId']/div/div[1]/div[2]/div/div/div/div[2]/div[2]/app-catalog-menu-header/div/div/div[4]/a/span[2]"
    chois_product_vacuum_cleaner_pickup = "//*[@id='content']/main/app-page-catalog-section/div/div[3]/div[1]/div/app-catalog-filter/app-catalog-menu-sidebar/div/div[4]/div/div[3]/a"
    chois_product_vacuum_cleaner_pickup_dream = "//*[@id='content']/main/app-page-catalog-section/div/div[3]/div[1]/div[2]/app-catalog-filter/div/app-filter-group[3]/app-ui-form-item/app-ui-type-checkbox/div/div[1]/label/span[1]"
    chois_product_vacuum_cleaner_pickup_dream_clining = "//*[@id='content']/main/app-page-catalog-section/div/div[3]/div[1]/div[2]/app-catalog-filter/div/app-filter-group[5]/app-ui-form-item/app-ui-type-checkbox/div/div[2]/label/span[1]"
    chois_cart1 = "//*[@id='content']/main/app-page-catalog-section/div/div[3]/div[2]/app-catalog-section[1]/div/app-catalog-cards/app-catalog-cards-grid/div/div[1]/div/app-catalog-card/div/a/div[1]/div/img"
    chois_cart2 = "//*[@id='content']/main/app-page-catalog-detail/div/div[1]/div[2]/div/div/div[3]/span"
    chois_cart3 = "//*[@id='headerId']/div/div[1]/div[2]/div/div/div/div[5]/app-catalog-cart-header/div/a/div/div[2]/span"
    word = "//*[@id='headerId']/div/div[1]/div[1]/div/div[1]/div[1]/a"
    resalt = "/html/body/app-root/div/app-block-page-header/div/div[1]/div[2]/div/div/div/div[2]/div[1]/span[2]"
              
  

    #Gettors
    def get_select_product_1(self):
        return WebDriverWait(self.driver , 30).until(EC.presence_of_element_located((By.XPATH,self.chois_product_1)))
        
    def get_select_product_vacuum_cleaner(self):
        return WebDriverWait(self.driver , 30).until(EC.element_to_be_clickable((By.XPATH,self.chois_product_vacuum_cleaner)))

    def get_chois_product_vacuum_cleaner_pickup(self):
        return WebDriverWait(self.driver , 30).until(EC.element_to_be_clickable((By.XPATH,self.chois_product_vacuum_cleaner_pickup)))
    
    #def get_chois_product_vacuum_cleaner_pickup_dream(self):
    #    return WebDriverWait(self.driver , 30).until(EC.element_to_be_clickable((By.XPATH,self.chois_product_vacuum_cleaner_pickup_dream)))

    #def get_chois_product_vacuum_cleaner_pickup_dream_clining(self):
    #    return WebDriverWait(self.driver , 30).until(EC.element_to_be_clickable((By.XPATH,self.chois_product_vacuum_cleaner_pickup_dream_clining)))
    
    def get_chois_cart1(self):     
        return WebDriverWait(self.driver , 30).until(EC.element_to_be_clickable((By.XPATH,self.chois_cart1)))

    def get_chois_cart2(self):     
        return WebDriverWait(self.driver , 30).until(EC.element_to_be_clickable((By.XPATH,self.chois_cart2)))

    def get_chois_cart3(self):     
        return WebDriverWait(self.driver , 30).until(EC.element_to_be_clickable((By.XPATH,self.chois_cart3)))
        

    def get_chois_cart4(self):     
        return  WebDriverWait(self.driver , 30).until(EC.element_to_be_clickable((By.XPATH,self.word)))
        

    def get_chois_cart5(self):     
        return  WebDriverWait(self.driver , 30).until(EC.element_to_be_clickable((By.XPATH,self.resalt)))
    
  
    #Actions
   
    def click_select_product_1(self):
        #Logger.add_start_step(method = "click_select_product_1")
        #self.get_current_url()
        self.get_select_product_1().click()
        time.sleep(2)
        self.get_select_product_vacuum_cleaner().click()
        time.sleep(2)
        self.scroll()
        time.sleep(2)
        self.get_chois_product_vacuum_cleaner_pickup().click()
        time.sleep(2)
        self.close()
        self.close1()
        time.sleep(2)
        #Logger.add_end_step(url = self.driver.current_url, method = "click_select_product_1")
        #self.chose()
        #time.sleep(3)
        
        #self.scroll1()
        #self.get_chois_product_vacuum_cleaner_pickup_dream().click()
        #time.sleep(2)
        #self.get_chois_product_vacuum_cleaner_pickup_dream_clining().click()
        #time.sleep(2)
        
        #self.get_chois_cart1().click()
        #time.sleep(2)
        #self.get_chois_cart2().click()
        #time.sleep(2)
        #self.double_click()
        #time.sleep(2)
        #self.get_chois_cart5().click()
        #time.sleep(4)
        #self.get_chois_cart5().click()
        #time.sleep(4)
        #self.get_chois_cart4().click()
        #time.sleep(4)
 
        #print("click select product_1")


    #Methods
    def select_products_1(self):
        #with allure.step("select_products_1"):
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_select_product_1()
            #self.click_select_product_2()
            #self.click_select_product_3()

