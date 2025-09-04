import unittest
from app_lib.keywords_replacing import KeywordsReplacing
from app_lib.keywords_pairs import KeywordsPairs
from app_lib.xlsx import Xlsx



class TestKeywordsReplacing(unittest.TestCase):
    def test_replacing_for_one_file(self):
        keyword_pairs = KeywordsPairs().extract()
        
        first_html = Xlsx(filepath='sources/webpage.xlsx').data_rows()[0][1]

        result = KeywordsReplacing(html=first_html, keywords=keyword_pairs).perform()

        self.assertNotEqual(first_html, result)

