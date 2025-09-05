from app_lib.helpers.extract_href_value import extract_href_value
from app_lib.helpers.replace_href import replace_href



class KeywordsReplacing:
    """
    This class replaces keywords in the provided HTML with values 
    from 'sources/keywords.xlsx'.
    """

    def __init__(self, html: str, keywords: tuple[tuple[str, str], ...]) -> None:
        self._html = html # html code to perform replacing
        self._keywords = keywords # contains the list [(key1, value1), (key2, value2),...(keyN,valueN)]


    def perform(self) -> str:
        """
        Replaces all found keywords in 'html' string with values from 'sources/keywords.xlsx'.
        """
        if not self._keywords:
            return self._html
        
        modified_html = self._html

        for keyword, value in self._keywords:
            if not keyword or not value:
                continue

            new_href = extract_href_value(value) or ""
            
            modified_html = replace_href(text=modified_html, key=keyword, new_href_value=new_href)

        return modified_html
