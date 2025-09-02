import unittest
import os
from app_lib.html import Html



HTML_CONTENT = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>My Page</title>
</head>
<body>
    <h1>Hello, world!</h1>
</body>
</html>
"""


class TestHtml(unittest.TestCase):
    def setUp(self):
        self.filepath = 'some.html'
        self.html =Html(filepath=self.filepath)


    def tearDown(self):
        if os.path.exists(self.filepath):
            os.remove(self.filepath)


    def test_create_html_file_with_specific_content(self):
        self.assertFalse(os.path.exists(self.filepath))

        self.html.write(content=HTML_CONTENT)

        self.assertTrue(os.path.exists(self.filepath))

        with open(file=self.filepath, mode='r', newline='', encoding='utf-8') as file:
            lines = file.readlines()
            self.assertEqual(lines[0], '<!DOCTYPE html>\n')
            self.assertEqual(lines[1], '<html>\n')
            self.assertEqual(lines[2], '<head>\n')


    def test_create_an_emtpy_html_file(self):
        self.html.write(content='')

        with open(file=self.filepath, mode='r', newline='', encoding='utf-8') as file:
            lines = file.readlines()
        self.assertEqual(len(lines), 0)


    def test_raise_value_error_when_incorrect_type_of_content(self):
        with self.assertRaises(ValueError) as cm:
            self.html.write(content=3333)

        self.assertEqual(str(cm.exception), f'Content for {self.filepath} have to be string.')

        self.assertFalse(os.path.exists(self.filepath))

