import unittest
import os
from lib.html_handler import HtmlHandler


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


class TestHtmlHandler(unittest.TestCase):
    def tearDown(self):
        filepath = 'some_html.html'
        
        if os.path.exists(filepath):
            os.remove(filepath)


    def test_create_html_file(self):
        filepath = 'some_html.html'
        self.assertFalse(os.path.exists(filepath))

        hh = HtmlHandler(filepath=filepath)
        hh.write(content=HTML_CONTENT)

        self.assertTrue(os.path.exists(filepath))

        with open(file=filepath, mode='r', newline='', encoding='utf-8') as file:
            lines = file.readlines()
            self.assertEqual(lines[0], '<!DOCTYPE html>\n')
            self.assertEqual(lines[1], '<html>\n')
            self.assertEqual(lines[2], '<head>\n')
