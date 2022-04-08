import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

service = Service('C:/Drivers/chromedriver98_win32/chromedriver')
driver = webdriver.Chrome(service=service)


class Iteractions_Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        driver.get('https://jqueryui.com/')
        driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        driver.close()

    @classmethod
    def tearDown(self):
        driver.back()

    def test_dragAnd_drop(self):
        driver.find_element(By.XPATH, '//*[@id="sidebar"]/aside[1]/ul/li[1]/a').click()
        time.sleep(1)
        driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
        source_element = driver.find_element(By.ID, "draggable")
        source_element_locations = source_element.location
        action = ActionChains(driver)
        action.drag_and_drop_by_offset(source_element, 373, 126).perform()
        target_element_locations = source_element.location
        self.assertNotEqual(source_element_locations, target_element_locations)

    def test_droppable(self):
        driver.find_element(By.XPATH, '//*[@id="sidebar"]/aside[1]/ul/li[2]/a').click()
        time.sleep(1)
        driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
        source_element = driver.find_element(By.ID, "draggable")
        target_element = driver.find_element(By.ID, "droppable")
        action = ActionChains(driver)
        action.drag_and_drop(source_element, target_element).perform()
        self.assertEqual(target_element.text, "Dropped!")

    def test_resizable(self):
        driver.find_element(By.XPATH, '//*[@id="sidebar"]/aside[1]/ul/li[3]/a').click()
        time.sleep(1)
        driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
        source_element = driver.find_element(By.XPATH, '//*[@id="resizable"]/div[3]')
        source_element_locations = source_element.location
        action = ActionChains(driver)
        action.drag_and_drop_by_offset(source_element, 40, 60).perform()
        target_element_locations = source_element.location
        self.assertNotEqual(source_element_locations, target_element_locations)

    def test_selectable(self):
        driver.find_element(By.XPATH, '//*[@id="sidebar"]/aside[1]/ul/li[4]/a').click()
        time.sleep(1)
        driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
        all_buttons = driver.find_elements(By.XPATH, '//*[@id="selectable"]/li')
        for i in all_buttons:
            print(i.text)
            i.click()

    def test_sortable(self):
        driver.find_element(By.XPATH, '//*[@id="sidebar"]/aside[1]/ul/li[5]/a').click()
        time.sleep(1)
        driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
        source_element = driver.find_element(By.XPATH, '//*[@id="sortable"]/li[1]')
        action = ActionChains(driver)
        action.drag_and_drop_by_offset(source_element, 123, 139).perform()
        target_element = source_element.location
        self.assertNotEqual(source_element, target_element)


if __name__ == "__main__":
    unittest.main()
