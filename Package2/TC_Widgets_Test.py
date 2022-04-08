import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

service = Service('C:/Drivers/chromedriver98_win32/chromedriver')
driver = webdriver.Chrome(service=service)


class Widgets_Test(unittest.TestCase):

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

    def test_accordion(self):
        driver.find_element(By.LINK_TEXT, "Accordion").click()
        driver.execute_script('window.scrollBy(0,300)', "")
        driver.switch_to.frame(driver.find_element(By.TAG_NAME, 'iframe'))
        driver.find_element(By.ID, "ui-id-5").click()
        time.sleep(2)
        element = driver.find_element(By.ID, 'ui-id-6')
        time.sleep(2)
        all_text = element.text
        time.sleep(1)
        self.assertTrue("Nam enim risus, molestie et, porta ac, aliquam ac, risus. Quisque lobortis. Phasellus "
                        "pellentesque purus in massa. Aenean in pede. Phasellus ac libero ac tellus pellentesque "
                        "semper. Sed ac felis. Sed commodo, magna quis lacinia ornare, quam ante aliquam nisi, "
                        "eu iaculis leo purus venenatis dui." in all_text)

    def test_autocomplete(self):
        driver.find_element(By.LINK_TEXT, 'Autocomplete').click()
        driver.switch_to.frame(driver.find_element(By.TAG_NAME, 'iframe'))
        element = driver.find_element(By.ID, 'tags')
        element.send_keys('A')
        time.sleep(2)
        list_1 = driver.find_elements(By.XPATH, '//*[@id="ui-id-1"]/li')
        print(len(list_1))
        for i in list_1:
            print(i.text)
            if i.text == "BASIC":
                i.click()
                break

    def test_button(self):
        driver.find_element(By.LINK_TEXT, 'Button').click()
        driver.switch_to.frame(driver.find_element(By.TAG_NAME, 'iframe'))
        button1 = driver.find_element(By.XPATH, '/html/body/div/button')
        button1.click()

    def test_CheckboxRadio(self):
        driver.find_element(By.LINK_TEXT, 'Checkboxradio').click()
        driver.switch_to.frame(driver.find_element(By.TAG_NAME, 'iframe'))
        asd = driver.find_element(By.XPATH, '/html/body/div/fieldset[1]/label[1]/span[1]')
        asd.click()
        asd2 = driver.find_element(By.XPATH, '//*[@id="radio-1"]')
        self.assertTrue(asd2.is_selected())

    def test_CheckboxRadio_1(self):
        driver.find_element(By.LINK_TEXT, 'Checkboxradio').click()
        driver.execute_script('window.scrollBy(0, 200)', "")
        driver.switch_to.frame(driver.find_element(By.TAG_NAME, 'iframe'))
        all_checkboxes = driver.find_elements(By.XPATH, "/html/body/div/fieldset[2]/label")
        checkboxes_after_Click = driver.find_elements(By.XPATH, '/html/body/div/fieldset[2]/input')
        for i in all_checkboxes:
            i.click()
        time.sleep(2)
        for y in checkboxes_after_Click:
            self.assertTrue(y.is_selected())

    def test_controlGroup(self):
        driver.find_element(By.LINK_TEXT, 'Controlgroup').click()
        driver.execute_script('window.scrollBy(0,250), ""')
        driver.switch_to.frame(driver.find_element(By.TAG_NAME, 'iframe'))
        driver.find_element(By.XPATH, '//*[@id="car-type-button"]/span[1]').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="ui-id-5"]').click()
        var1 = driver.find_element(By.XPATH, '/html/body/div[1]/fieldset[1]/div/label[1]/span[1]')
        var1.click()
        var2 = driver.find_element(By.XPATH, '/html/body/div[1]/fieldset[1]/div/label[3]/span[1]')
        var2.click()
        var3 = driver.find_element(By.XPATH, '//*[@id="horizontal-spinner"]')
        var3.send_keys(20)
        self.assertTrue(var1.get_attribute('class'), 'ui-button ui-widget ui-checkboxradio-radio-label '
                                                     'ui-checkboxradio-label ui-controlgroup-item '
                                                     'ui-checkboxradio-checked ui-state-active')
        self.assertTrue(var2.get_attribute('class'), 'ui-button ui-widget ui-checkboxradio-radio-label '
                                                     'ui-checkboxradio-label ui-controlgroup-item '
                                                     'ui-checkboxradio-checked ui-state-active')

    def test_date_picker(self):
        driver.find_element(By.LINK_TEXT, 'Datepicker').click()
        driver.switch_to.frame(driver.find_element(By.TAG_NAME, 'iframe'))
        date_picker = driver.find_element(By.ID, 'datepicker')
        date_picker.click()
        element = driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div/a[1]')
        element.click()
        for i in range(1, 10):
            i = driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div/a[1]')
            i.click()
        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[3]/td[5]/a').click()

    def test_dialog(self):
        driver.find_element(By.LINK_TEXT, 'Dialog').click()
        driver.find_element(By.LINK_TEXT, 'Modal form').click()
        driver.execute_script('window.scrollBy(0,300)', "")
        driver.switch_to.frame(driver.find_element(By.TAG_NAME, 'iframe'))
        time.sleep(2)
        total_rows = len(driver.find_elements(By.XPATH, '//*[@id="users"]/tbody/tr'))
        print(f'Numbers of rows are: {total_rows}')
        total_column = len(driver.find_elements(By.XPATH, '//*[@id="users"]/thead/tr/th'))
        print(f'Numbers of columns are: {total_column}')
        for i in range(1, total_rows + 1):
            for y in range(1, total_column + 1):
                value1 = driver.find_element(By.XPATH, f'//*[@id="users"]/tbody/tr[{i}]/td[{y}]').text
                print(value1, end='  ')
            print()
        driver.find_element(By.XPATH, '//*[@id="create-user"]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="name"]').clear()
        driver.find_element(By.XPATH, '//*[@id="name"]').send_keys("Plamen Hristov")
        driver.find_element(By.XPATH, '//*[@id="email"]').clear()
        driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("test@abv.bg")
        driver.find_element(By.XPATH, '//*[@id="password"]').clear()
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("123456789")
        driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/button[1]').click()
        time.sleep(2)
        total_rows2 = len(driver.find_elements(By.XPATH, '//*[@id="users"]/tbody/tr'))
        print(f'Numbers of rows are: {total_rows2}')
        total_column2 = len(driver.find_elements(By.XPATH, '//*[@id="users"]/thead/tr/th'))
        print(f'Numbers of columns are: {total_column2}')
        for i in range(1, total_rows2 + 1):
            for y in range(1, total_column2 + 1):
                value2 = driver.find_element(By.XPATH, f'//*[@id="users"]/tbody/tr[{i}]/td[{y}]').text
                print(value2, end='  ')
            print()
        self.assertNotEqual(total_rows, total_rows2)

    def test_menu(self):
        driver.find_element(By.LINK_TEXT, 'Menu').click()
        driver.execute_script('window.scrollBy(0,350)', "")
        driver.switch_to.frame(driver.find_element(By.TAG_NAME, 'iframe'))
        books = driver.find_element(By.XPATH, '//*[@id="ui-id-2"]')
        clothing = driver.find_element(By.XPATH, '//*[@id="ui-id-3"]')
        electronics = driver.find_element(By.XPATH, '//*[@id="menu"]/li[4]')
        movies = driver.find_element(By.XPATH, '//*[@id="menu"]/li[5]')
        music = driver.find_element(By.XPATH, '//*[@id="menu"]/li[6]')
        rock = driver.find_element(By.ID, 'ui-id-10')
        classic = driver.find_element(By.ID, 'ui-id-12')
        actions = ActionChains(driver)
        actions.move_to_element(books).move_to_element(clothing).perform()
        actions.move_to_element(electronics).perform()
        time.sleep(1)
        actions.move_to_element(movies).perform()
        actions.move_to_element(music).perform()
        time.sleep(1)
        actions.move_to_element(rock).perform()
        time.sleep(1)
        actions.move_to_element(classic).click().perform()

    def test_select_menu(self):
        time.sleep(2)
        driver.execute_script('window.scrollBy(0, 400)', "")
        driver.find_element(By.LINK_TEXT, 'Selectmenu').click()
        driver.find_element(By.LINK_TEXT, 'Product Selection').click()
        time.sleep(2)
        driver.switch_to.frame(driver.find_element(By.TAG_NAME, 'iframe'))
        driver.find_element(By.XPATH, '//*[@id="radius-button"]').click()
        circle = driver.find_element(By.XPATH, '//*[@id="circle"]')
        circle_size = circle.size
        print(circle_size['width'])
        print(circle_size['height'])
        driver.find_element(By.ID, 'ui-id-5').click()
        circle2 = driver.find_element(By.XPATH, '//*[@id="circle"]')
        circle2_size = circle2.size
        print(circle2_size['width'])
        print(circle2_size['height'])
        self.assertNotEqual(circle_size, circle2_size)

    def test_slider(self):
        time.sleep(1)
        driver.execute_script('window.scrollBy(0, 400)', "")
        driver.find_element(By.LINK_TEXT, 'Slider').click()
        driver.find_element(By.LINK_TEXT, 'Colorpicker').click()
        time.sleep(1)
        driver.switch_to.frame(driver.find_element(By.TAG_NAME, 'iframe'))
        source_element1 = driver.find_element(By.XPATH, '//*[@id="red"]/span')
        source_element1_location_before = source_element1.location
        action = ActionChains(driver)
        action.drag_and_drop_by_offset(source_element1, -288, 83).perform()
        source_element1_location_after = source_element1.location
        time.sleep(2)
        source_element2 = driver.find_element(By.XPATH, '//*[@id="green"]/span')
        action.drag_and_drop_by_offset(source_element2, -153, 127).perform()
        time.sleep(2)
        source_element3 = driver.find_element(By.XPATH, '//*[@id="blue"]/span')
        action.drag_and_drop_by_offset(source_element3, 200, 161).perform()
        self.assertNotEqual(source_element1_location_before, source_element1_location_after)

    def test_spinner(self):
        driver.find_element(By.LINK_TEXT, 'Spinner').click()
        driver.execute_script('window.scrollBy(0,350)', "")
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, 'Currency').click()
        time.sleep(1)
        driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
        driver.find_element(By.ID, 'currency').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="currency"]/option[3]').click()
        time.sleep(1)
        for i in range(0, 20 + 1):
            i = driver.find_element(By.XPATH, '/html/body/p[1]/span/a[1]/span[1]')
            i.click()
        driver.switch_to.default_content()
        driver.find_element(By.LINK_TEXT, 'Decimal').click()
        driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
        driver.find_element(By.ID, 'culture').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="culture"]/option[3]').click()
        for y in range(0, 30):
            y = driver.find_element(By.XPATH, '/html/body/p[1]/span/a[1]/span[1]')
            y.click()

    def test_tabs(self):
        driver.execute_script('window.scrollBy(0,350)', "")
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, 'Tabs').click()
        driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
        tab_1 = driver.find_element(By.CSS_SELECTOR, '#tabs-1 > p')
        tab1_text = tab_1.text
        self.assertTrue('Proin elit arcu, rutrum commodo, vehicula tempus, commodo a, risus. Curabitur nec arcu.' in
                        tab1_text)
        driver.find_element(By.XPATH, '//*[@id="tabs"]/ul/li[2]').click()
        tab_2 = driver.find_element(By.CSS_SELECTOR, '#tabs-2 > p')
        tab2_text = tab_2.text
        self.assertTrue('Morbi tincidunt, dui sit amet facilisis feugiat, odio metus gravida ante, ut pharetra massa '
                        'metus id nunc. ' in
                        tab2_text)
        driver.find_element(By.XPATH, '//*[@id="tabs"]/ul/li[3]').click()
        tab_3 = driver.find_element(By.CSS_SELECTOR, '#tabs-3 > p')
        tab3_text = tab_3.text
        self.assertTrue('Mauris eleifend est et turpis.' in tab3_text)
        driver.switch_to.default_content()
        driver.find_element(By.LINK_TEXT, 'Simple manipulation').click()
        driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="add_tab"]').click()
        time.sleep(2)
        driver.find_element(By.ID, 'tab_title').clear()
        driver.find_element(By.ID, 'tab_title').send_keys("Test Title")
        driver.find_element(By.ID, 'tab_content').clear()
        driver.find_element(By.ID, 'tab_content').send_keys("Plamen Hristov Demo, Demo")
        driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/button[1]').click()
        driver.find_element(By.ID, 'ui-id-3').click()
        assert_element = driver.find_element(By.ID, 'ui-id-3')
        assert_element_text = assert_element.text
        assert_element2 = driver.find_element(By.CSS_SELECTOR, '#tabs-2 > p')
        assert_element2_text = assert_element2.text
        self.assertTrue(assert_element_text == "Test Title")
        self.assertTrue('Plamen Hristov Demo, Demo' in assert_element2_text)

    def test_tooltip(self):
        driver.execute_script('window.scrollBy(0, 400)', "")
        time.sleep(2)
        driver.find_element(By.LINK_TEXT, 'Tooltip').click()
        driver.find_element(By.LINK_TEXT, 'Forms').click()
        driver.switch_to.frame(driver.find_element(By.TAG_NAME, 'iframe'))
        time.sleep(2)
        element_1 = driver.find_element(By.ID, 'firstname')
        element_2 = driver.find_element(By.ID, 'lastname')
        element_3 = driver.find_element(By.ID, 'address')
        actions = ActionChains(driver)
        actions.move_to_element(element_1).perform()
        actions.drag_and_drop_by_offset(element_1, 317, 29).perform()
        self.assertTrue(element_1.get_attribute('title'), 'Please provide your firstname.')
        time.sleep(2)
        actions.move_to_element(element_2).perform()
        actions.drag_and_drop_by_offset(element_1, 311, 78).perform()
        self.assertTrue(element_1.get_attribute('title'), 'Please provide also your lastname.')
        time.sleep(2)
        actions.move_to_element(element_3).perform()
        actions.drag_and_drop_by_offset(element_1, 311, 129).perform()
        self.assertTrue(element_1.get_attribute('title'), 'Your home or work address.')
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, 'body > button').click()
        time.sleep(2)


if __name__ == "__main__":
    unittest.main()
