from django.test import TestCase
from .search import search, search_t
from .translate import translate_tr, translate_rt
from selenium import webdriver

class SeacrhTestCase(TestCase):

    def test_search(self):
        results, n_result = search('Агач')
        test = type(results)
        test2 = type(n_result)
        self.assertEqual(test, list)
        self.assertEqual(test2, int)

    def test_search_t(self):
        results, n_result = search_t('Дерево')
        test = type(results)
        test2 = type(n_result)
        self.assertEqual(test, list)
        self.assertEqual(test2, int)

class TranslateTestCase(TestCase):

    def test_translate_tr_true(self):
        query = translate_tr('Агач')
        self.assertEqual(query, 'Дерево')

    def test_translate_tr_false(self):
        query = translate_tr('Агач')
        self.assertNotEqual(query, 'Агач')

    def test_translate_rt_true(self):
        query = translate_rt('Дерево')
        self.assertEqual(query, 'Агач')

    def test_translate_rt_false(self):
        query = translate_rt('Дерево')
        self.assertNotEqual(query, 'Дерево')

class UITestCase(TestCase):

    def test_selenium_search(self):
        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:8000/")
        elem_name = driver.find_element_by_name("query")
        elem_name.send_keys('Агач')
        elem = driver.find_element_by_name("search")
        elem.click()
        self.assertTrue(True)

    def test_selenium_open_statistic(self):
        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:8000/statistic")
        assert "Статистика" in driver.title