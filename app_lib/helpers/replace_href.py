import re


def replace_href(text: str, key: str, new_href_value: str) -> str:
    """
    Return the text with replaced value.

    Args:
        text (str): text in which we find and replace href values.
        key (str): base filename (without '.html') to match in the href attribute;
        new_href_value (str): this is new value for found href.
    
    Example:
        >>> text = '<a href="主页.html" class="w3-bar-item w3-button w3-mobile" style="padding:0 5% 0 10%" ><img src="../images/logo.png" style="width:100%; max-width:150px"/></a>'
        >>> key ='主页'
        >>> new_href_value = 'https://www.topeintl.com/cn/主页.html'
        >>> replace_href(text=text, key=key, new_href_value=new_href_value)
        >>> '<a href="https://www.topeintl.com/cn/主页.html" class="w3-bar-item w3-button w3-mobile" style="padding:0 5% 0 10%" ><img src="../images/logo.png" style="width:100%; max-width:150px"/></a>'
    """
    pattern = fr'href="{re.escape(key)}\.html"'
    return re.sub(pattern, f'href="{new_href_value}"', text)

