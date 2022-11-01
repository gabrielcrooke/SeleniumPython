import unittest
from selenium import webdriver
import time


class test_004(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def test_004(self):

        self.driver.get('https://qainterview.pythonanywhere.com/')
        self.driver.find_element('id', 'number').send_keys('25')
        time.sleep(2)
        self.driver.find_element('id', 'number').clear()
        time.sleep(2)
        self.driver.find_element('id', 'number').send_keys('50')
        time.sleep(2)
        self.driver.find_element('id', 'getFactorial').click()

    def tearDown(self):
        time.sleep(15)

    if __name__ == '__main__':
        unittest.main()
