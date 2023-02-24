from datetime import datetime
#from lib2to3.pgen2 import driver
import time
import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.service import Service 


class Base():
    def __init__(self,driver):
        self.driver = driver
    

#getting url

    def get_current_url(self):
        get_url = self.driver.current_url
        print("current_url " + get_url)
   

#getting url correctli

    def assert_url(self,resalt):
        get_url = self.driver.current_url
        assert get_url == resalt
        print("Good value url")

#scroll page

    def scroll(self):
       action = ActionChains(self.driver)
       red_t_short = self.driver.find_element(By.XPATH,"//*[@id='content']/main/app-page-catalog-section/div/div[3]/div[1]/div/app-catalog-filter/app-catalog-menu-sidebar/div/div[6]/a")
       action.move_to_element(red_t_short).perform()
       print("scroll")

#ad closure

    def close(self):
     
       red_t_short = self.driver.find_element(By.XPATH,"//*[@id='popmechanic-form-134282']/div[3]")
       red_t_short.click()
       print("close")

    def close1(self):
    
       red_t_short = self.driver.find_element(By.XPATH,"/html/body/app-root/app-cookie-policy/div/div/div/div[2]/div")
       red_t_short.click()
       print("close")

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

# double_click      
    def double_click(self):
        action = ActionChains(self.driver)
        red_t_short = self.driver.find_element(By.XPATH,"//*[@id='headerId']/div/div[1]/div[2]/div/div/div/div[5]/app-catalog-cart-header/div/a/div/div[2]/span")
        action.double_click(red_t_short).perform()

