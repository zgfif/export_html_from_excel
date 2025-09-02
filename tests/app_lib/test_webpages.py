import unittest
from app_lib.webpages import Webpages
import os



class TestWebpages(unittest.TestCase):
    def setUp(self):
        self.filepath = 'sources/webpage.xlsx'
        self.output_dir = 'results'


    def tearDown(self):
        if os.path.exists(self.output_dir):
            for _, _, files in os.walk(self.output_dir):
                for file in files:
                    os.remove(self.output_dir + '/' + file)

            os.rmdir(self.output_dir)


    def test_generate_webpages(self):
        Webpages(filepath=self.filepath, output_directory=self.output_dir).generate()

        self.assertTrue(os.path.isdir(self.output_dir))

        for _, _, files in os.walk(self.output_dir):
            self.assertEqual(len(files), 10)


    def test_raise_error(self):
        output_dir = 234234
        
        with self.assertRaises(ValueError) as cm:
            Webpages(filepath=self.filepath, output_directory=output_dir).generate()
        self.assertIn(f'Output directory {output_dir} must be string.', str(cm.exception))
