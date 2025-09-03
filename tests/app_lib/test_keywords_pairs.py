import unittest
from app_lib.keywords_pairs import KeywordsPairs



class TestKeywordsPairs(unittest.TestCase):
    def test_extracting(self):
        kp = KeywordsPairs().extract()
        
        first_pair = [
            'Bending Machine', 
            '<a href="https://www.topeintl.com/en/bending-machine.html" >Bending Machine</a>'
        ]
        
        self.assertListEqual(kp[0], first_pair)
