import unittest
from app_lib.helpers.extract_href_value import extract_href_value

class TestExtractHrefValue(unittest.TestCase):
    def test_correct_extracting(self):
        text = '<a href="https://www.topeintl.com/en/bending-machine.html" >Bending Machine</a>'
        expected = 'https://www.topeintl.com/en/bending-machine.html'

        self.assertEqual(extract_href_value(text), expected)


    def test_when_href_is_empty(self):
        text = '<a href="" >PVC管</a>'
        expected = ''

        self.assertEqual(extract_href_value(text), expected)


    def test_when_no_href_attribute(self):
        text = '高温布'
        expected = '高温布'

        self.assertEqual(extract_href_value(text), expected)


    def test_empty_string(self):
        text = ''
        expected = ''

        self.assertEqual(extract_href_value(text), expected)
