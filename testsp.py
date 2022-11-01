from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import  By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException


#driver=webdriver.Chrome(executable_path= "C:\gcooke\Drivers\chromedriver.exe")

driver = webdriver.Chrome()
driver.get("https://www.supercarros.com/vender/particulares-1/?uid=12ad6084-70a2-4fb3-a72f-9f4acf0bd5d4")
driver.maximize_window()
#driver.implicitly_wait(10)
t=3

driver.find_element(By.ID, "Customer_FirstName").send_keys("Raydel")
driver.find_element(By.XPATH, '//*[@id="Customer_LastName"]').send_keys("Suarez" + Keys.TAB + "Dorado 3, Jacobo")
driver.find_element(By.ID, "Customer_Number").send_keys("29" + Keys.TAB + "frente a ciudad modelo")
driver.find_element(By.XPATH, '//*[@id="Customer_Phone"]').send_keys("8298908641" + Keys.TAB + "8098459311")
driver.find_element(By.XPATH, '//*[@id="Customer_ReferralType"]').send_keys(("Por redes sociales"))
driver.execute_script("window.scrollBy(0,500)","")
prov_select= driver.find_element(By.XPATH, '//*[@id="Customer_Location"]')
prov=Select(prov_select)
prov.select_by_value("7")

driver.find_element(By.XPATH, '//*[@id="Customer_Email"]').send_keys("ray-suarez@hotmail.com" + Keys.TAB + "ray-suarez@hotmail.com")



time.sleep(10)
driver.close()
