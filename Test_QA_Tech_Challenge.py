#Importing libraries
import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class TechChallenge(unittest.TestCase):

    #Test fixture: preparation/inicialization
    def setUp(self):
        global driver
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-popup-blocking")
        #chrome_options.add_argument("headless")

        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://rahulshettyacademy.com/AutomationPractice/')
        driver.implicitly_wait(10)

    #Challenge example test cases
    def test1_RadioButton(self):
        radioButton = driver.find_element(By.CSS_SELECTOR,"[value='radio2']")
        if radioButton is not None:
            radioButton.click()
            time.sleep(1)
            radioButton = driver.find_element(By.CSS_SELECTOR,"[value='radio3']")
            if radioButton is not None:
                radioButton.click()
                time.sleep(1)
                radioButton = driver.find_element(By.CSS_SELECTOR,"[value='radio1']")
                if radioButton is not None:
                    radioButton.click()
                    time.sleep(1)

    def test2_SuggestionClass(self):
        suggest = driver.find_element(By.XPATH,"//*[@id='autocomplete']")
        if suggest is not None:
            suggest.send_keys("Me")
            time.sleep(1)
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//li[@class='ui-menu-item']/div[contains(@id, 'ui-id-')][text()='Mexico']")))
            drop = driver.find_element(By.XPATH, "//li[@class='ui-menu-item']/div[contains(@id, 'ui-id-')][text()='Mexico']")
            drop.click()
            time.sleep(2)

    def test3_DropDown(self):
        drop = driver.find_element(By.XPATH,"//select[@name='dropdown-class-example']")
        if drop is not None:
            Option = Select(drop)
            Option.select_by_index(2)
            time.sleep(2)
            Option.select_by_index(3)
            time.sleep(2)

    def test4_CheckBox(self):
        checkOne = driver.find_element(By.CSS_SELECTOR, "input#checkBoxOption1")
        checkTwo = driver.find_element(By.CSS_SELECTOR, "input#checkBoxOption2")
        if checkOne and checkTwo is not None:
            checkOne.click() 
            checkTwo.click()
            time.sleep(2)

    def test5_Switchtoalert(self):
        switch = driver.find_element(By.XPATH,"//*[@id='name']")
        if switch is not None:
            switch.send_keys("Stori Card")
            time.sleep(1)
            Button = driver.find_element(By.CSS_SELECTOR,"input#alertbtn")
            Button.click()
            time.sleep(2)
            alerta = driver.switch_to.alert
            alerta.accept()
            time.sleep(3)

    def test6_ElementDisplayed(self):
        element = driver.find_element(By.CSS_SELECTOR,"div.right-align>fieldset>input#displayed-text")
        if element is not None:
            #el atributo "style" indica la presencia del elemento
            if element.is_displayed():
                print("Element SHOWN")
            else:
                print("Element HIDDEN")

    #Test fixture: end
    def tearDown(self):
        driver.quit()

#Run main current module
if __name__=="__main__":
    unittest.main()

