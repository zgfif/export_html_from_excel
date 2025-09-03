import unittest
from app_lib.helpers.replace_href import replace_href



class TestReplaceHref(unittest.TestCase):
    def test_successfully_replacing(self):
        text = r'<a href="主页.html" class="w3-bar-item w3-button w3-mobile" style="padding:0 5% 0 10%" ><img src="../images/logo.png" style="width:100%; max-width:150px"/></a>'
        expected = r'<a href="https://www.topeintl.com/cn/主页.html" class="w3-bar-item w3-button w3-mobile" style="padding:0 5% 0 10%" ><img src="../images/logo.png" style="width:100%; max-width:150px"/></a>'
        self.assertEqual(replace_href(text=text, key="主页", new_href_value="https://www.topeintl.com/cn/主页.html"), expected)
    

    def test_successfully_replacing_with_empty_string(self):
        text = r'<a href="主页.html" class="w3-bar-item w3-button w3-mobile" style="padding:0 5% 0 10%" ><img src="../images/logo.png" style="width:100%; max-width:150px"/></a>'
        expected = r'<a href="" class="w3-bar-item w3-button w3-mobile" style="padding:0 5% 0 10%" ><img src="../images/logo.png" style="width:100%; max-width:150px"/></a>'
        self.assertEqual(replace_href(text=text, key="主页", new_href_value=""), expected)
    

    def test_when_cant_find(self):
        text = r'<a href="主页.html" class="w3-bar-item w3-button w3-mobile" style="padding:0 5% 0 10%" ><img src="../images/logo.png" style="width:100%; max-width:150px"/></a>'
        expected = r'<a href="主页.html" class="w3-bar-item w3-button w3-mobile" style="padding:0 5% 0 10%" ><img src="../images/logo.png" style="width:100%; max-width:150px"/></a>'
        self.assertEqual(replace_href(text=text, key="aaaa", new_href_value=""), expected)


    def test_successfully_replacing_when_multiple_matches(self):
        text = r'<a href="主页.html" class="w3-bar-item w3-button w3-mobile" style="padding:0 5% 0 10%" ><img src="../images/logo.png" style="width:100%; max-width:150px"/></a><a href="主页.html">主页</a>'
        expected = r'<a href="https://www.topeintl.com/cn/主页.html" class="w3-bar-item w3-button w3-mobile" style="padding:0 5% 0 10%" ><img src="../images/logo.png" style="width:100%; max-width:150px"/></a><a href="https://www.topeintl.com/cn/主页.html">主页</a>'
        self.assertEqual(replace_href(text=text, key="主页", new_href_value="https://www.topeintl.com/cn/主页.html"), expected)
    