# -*- coding: utf-8 -*-
'''
Created on 06 oct. 2022

@author: Gabriel
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class test002(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    # Probando Text Box
    def test002(self):
        self.driver.get('https://demoqa.com/')
        self.driver.execute_script('window.scroll(0,400)', "")
        self.driver.find_element('xpath', '//*[@id="app"]/div/div/div[2]/div/div[2]').click()
        self.driver.find_element('xpath', '//*[@id="app"]/div/div/div[2]/div[1]/div/div/div[1]/span/div').click()
        self.driver.find_element('xpath', '//*[@id="item-0"]').click()
        self.driver.execute_script('window.scroll(0,300)', "")
        self.driver.find_element('id', 'userName').send_keys('Gabriel Crooke' + Keys.TAB + 'gabrielcrooke@gmail.com'
        + Keys.TAB + 'Calle Caonabo, #125, Santo Domingo Este' + Keys.TAB + 'Calle bobadilla, #08, Distrito Nacional' + Keys.TAB)

        self.driver.find_element('xpath', '//*[@id="submit"]').click()

    # Probando Check Box
    def test003(self):
        self.driver.get('https://demoqa.com/')
        self.driver.execute_script('window.scroll(0,400)', "")
        self.driver.find_element('xpath', '//*[@id="app"]/div/div/div[2]/div/div[2]').click()
        self.driver.find_element('xpath', '//*[@id="app"]/div/div/div[2]/div[1]/div/div/div[1]/span/div').click()
        self.driver.find_element('xpath', '//*[@id="item-1"]/span').click()
        self.driver.find_element('xpath', '//*[@id="tree-node"]/ol/li/span/button').click()
        self.driver.find_element('xpath', '//*[@id="tree-node"]/ol/li/ol/li[1]/span/button').click()
        self.driver.find_element('xpath', '//*[@id="tree-node"]/ol/li/ol/li[2]/span/button').click()
        self.driver.find_element('xpath', '//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/span/label').click()
        time.sleep(2)
        self.driver.find_element('xpath', '//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/span/label').click()

    def tearDown(self):
        time.sleep(10)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()