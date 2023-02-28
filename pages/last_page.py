from argparse import Action
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
from pages.main_page import Main_page
#import allure

class Last_page(Main_page):
    def __init__(self,driver):
        self.driver = driver
    

#getting url

    def get_current_url(self):
        get_url = self.driver.current_url
        print("current_url " + get_url)

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

    def double_click(self):
        action = ActionChains(self.driver)
        red_t_short = self.driver.find_element(By.XPATH,"//*[@id='headerId']/div/div[1]/div[2]/div/div/div/div[5]/app-catalog-cart-header/div/a/div/div[2]/span")
        action.double_click(red_t_short).perform()
   

    def click_select_product_3(self):
        #with allure.step("click_select_product_3"):
            self.get_chois_cart1().click()
            time.sleep(2)
            self.get_chois_cart2().click()
            time.sleep(2)
            self.double_click()
            time.sleep(2)
            self.get_chois_cart5().click()
            time.sleep(4)
            self.get_chois_cart5().click()
            time.sleep(4)
            self.get_chois_cart4().click()
            time.sleep(4)

    