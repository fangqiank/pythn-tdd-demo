import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class E2ETests(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        self.driver.get('http://localhost:5000')

    def tearDown(self) -> None:
        self.driver.quit()

    def test_browser_title_contains_app_name(self):
        self.assertIn('Named Entity Recognition', self.driver.title)

    def test_page_heading_is_named_entity_finder(self):
        heading = self._find('heading').text
        self.assertEqual('Named Entity Finder', heading)

    def test_page_has_input_for_text(self):
        element = self._find('input-text')
        self.assertIsNotNone(element)

    def test_page_has_button_for_submit_text(self):
        element = self._find('find-button')
        self.assertIsNotNone(element)

    def test_page_has_ner_table(self):
        input_element = self._find('input-text')
        submit_button = self._find('find-button')
        input_element.send_keys('hello world')
        submit_button.click()
        table = self._find('ner-table')
        self.assertIsNotNone(table)

    def _find(self, val):
        return self.driver.find_element(By.CSS_SELECTOR, f'[data-test-id="{val}"]')


