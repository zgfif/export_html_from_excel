import re

def extract_href_value(text: str) -> str:
    """
    Return value of href
    
    Arg:
        text(str) - text to extract href value.

    Example:
        >>> href = extract_href_value('<a href="https://www.topeintl.com/en/bending-machine.html" >Bending Machine</a>')
        >>> href
        >>> "https://www.topeintl.com/en/bending-machine.html"
    """
    if not isinstance(text, str):
        raise ValueError(f'Argument {text} have to be string.')

    if not text:
        return ''

    pattern = r"href=\"(.*)\""

    result = re.search(pattern, text)

    if result:
        return result[1]

    return text
