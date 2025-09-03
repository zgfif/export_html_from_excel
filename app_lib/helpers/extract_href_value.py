import re

def extract_href_value(text: str) -> str | None:
    """
    Extract the value of the first href attribute from the given text.

    Args:
        text (str): Input text containing an HTML element.

    Returns:
        str | None: The href value if found, otherwise None.

    Example:
        >>> extract_href_value('<a href="https://example.com">Link</a>')
        'https://example.com'
    """
    if not isinstance(text, str):
        raise ValueError(f'Argument {text!r} must be a string.')

    if not text:
        return None

    pattern = r'href="(.*?)"'

    result = re.search(pattern, text)

    if result:
        return result.group(1)

    return None
