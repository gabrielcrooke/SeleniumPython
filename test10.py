import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


horaGlobal = time.strftime('%H%M%S')
diaglobal = time.strftime("%y-%m-%d")


class Test_010(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

    def test_010(self):
        self.driver.get('https://www.globalsqa.com/demo-site/select-dropdown-menu/')

        elements = self.driver.find_element('xpath', '//*[@id="post-2646"]/div[2]/div/div/div/p/select')
        drop = Select(elements)
        #drop.select_by_visible_text('Botswana')
        #drop.select_by_index(0)
        drop.select_by_value('BWA')

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()