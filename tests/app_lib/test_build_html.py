import unittest
from app_lib.build_html import BuildHtml
# from bs4 import BeautifulSoup
from tests.app_lib.html_example import HTML_EXAMPLE
from app_lib.xlsx import Xlsx
from app_lib.helpers.group_elements_by_two import group_elements_by_two




class TestBuildHtml(unittest.TestCase):
    def test_building(self):

        rows = Xlsx('sources/keywords.xlsx').data_rows()

        # for i,row in enumerate(rows):
            # print(i)
            # print(row)

        keywords_list = []

        for row in rows:
            grouped = group_elements_by_two(row)
            # print(grouped)
            keywords_list.append(grouped)
        
        
        
        
        html_code = BuildHtml(html_body=HTML_EXAMPLE, keywords=keywords_list).perform()

        # bs = BeautifulSoup(html_code, 'html.parser')

        # title = bs.find('<title>').get_text()

        # print(title)
        # self.assertEqual(extracted_keyword, keyword)