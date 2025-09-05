import unittest
from app_lib.keywords_replacing import KeywordsReplacing
from app_lib.keywords_pairs import KeywordsPairs
from app_lib.xlsx_file import XlsxFile



class TestKeywordsReplacing(unittest.TestCase):
    def test_replacing_for_one_file(self):
        
        with XlsxFile(filepath='sources/webpage.xlsx') as xf:
            html_content = xf.data_rows()[0][1]
        
        keyword_pairs = KeywordsPairs().extract()
        
        result = KeywordsReplacing(html=html_content, keywords=keyword_pairs).perform()

        self.assertNotEqual(html_content, result)
