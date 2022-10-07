#Identificacon de la existencia de los elementos de la pagina

# -*- coding: utf-8 -*-
'''
Created on 04 oct. 2022

@author: Gabriel
'''
import unittest
import time
from selenium import webdriver


class Test_001(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)


    def test_001(self):
        # INGRESO A LA APP DE REGISTRO

        self.driver.get("https://demoqa.com/")
        self.driver.find_element('xpath', '//*[@id="app"]/header/a/img').is_displayed()
        self.driver.find_element('xpath', '//*[@id="app"]/div/div/div[1]/a/img').is_displayed()
        self.driver.find_element('xpath', '// *[ @ id = "app"] / div / div / div[2] / div / div[1]').is_displayed()
        self.driver.find_element('xpath', '// *[ @ id = "app"] / div / div / div[2] / div / div[2]').is_displayed()
        self.driver.find_element('xpath', '// *[ @ id = "app"] / div / div / div[2] / div / div[3]').is_displayed()
        self.driver.find_element('xpath', '// *[ @ id = "app"] / div / div / div[2] / div / div[4]').is_displayed()
        self.driver.find_element('xpath', '// *[ @ id = "app"] / div / div / div[2] / div / div[5]').is_displayed()
        self.driver.find_element('xpath', '// *[ @ id = "app"] / div / div / div[2] / div / div[6]').is_displayed()

    def tearDown(self):
        time.sleep(20)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()