#Identificacon de la existencia de los elementos de la pagina

# -*- coding: utf-8 -*-
'''
Created on 04 oct. 2022

@author: Gabriel
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

horaGlobal = time.strftime('%H%M%S')



class Test_001(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)


    def test_001(self):
        # INGRESO A LA APP DE REGISTRO

        self.driver.get("https://www.google.com.do/")
        self.driver.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('Documentacion de python')
        self.driver.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.BACK_SPACE, Keys.BACK_SPACE)
        self.driver.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)


        self.driver.get_screenshot_as_file(f"../data/capturas/SendKey-{horaGlobal}.png")

    def tearDown(self):
        time.sleep(20)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()