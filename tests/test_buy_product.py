
import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import Main_page
from selenium.webdriver.common.action_chains import ActionChains
from pages.vacuum_cleaner_filter_selection import Vacuum_cleaner_filter_selection
from pages.last_page import Last_page
#import allure


#@allure.description("Test buy product 1")
def test_buy_product_1():
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        g = Service('C:\\Users\\nskfo\source\repos\resourse\\chromedriver.exe')
        driver = webdriver.Chrome(options=options, service=g)
     
        
        print("Start test 1")


        mp = Main_page(driver)
        mp.select_products_1()

        csp = Vacuum_cleaner_filter_selection(driver)
        csp.click_select_product_2()

        ls = Last_page(driver)
        ls.click_select_product_3()
        #mp.assert_url("https://www.maunfeld.ru/blog")


        print("finish test 1")
        




