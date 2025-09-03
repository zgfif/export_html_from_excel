from app_lib.helpers.extract_href_value import extract_href_value
from app_lib.helpers.replace_href import replace_href



class KeywordsReplacing:
    """
    This class is used to find all keywords from and replace them with values from 'sources/keywords.xlsx'.
    """
    
    def __init__(self, html: str, keywords: list[list[str, str]]) -> None:
        self._html = html # html code to perform replacing
        self._keywords = keywords # contains the list [[key1, value1], [key2, value2],...[keyN,valueN]]


    def perform(self) -> str:
        """
        Replaces all found keywords in 'html' string with values from 'sources/keywords.xlsx'.
        """
        if not self.keywords:
            return self.html_body
        
        modified_html = self._html

        for row in self.keywords:
            keyword, value = row[0], row[1]

            if not keyword or not value:
                continue

            new_href = extract_href_value(value)
            
            if not new_href:
                new_href = ''
            
            modified_html = replace_href(text=modified_html, key=keyword, new_href_value=new_href)

        return modified_html


    @property
    def keywords(self) -> list[list[str | None]]:
        """
        Return the list of keywords pairs.
        """
        return self._keywords


    @property
    def html(self)  -> str:
        """
        Return the string with html.
        """
        return self._html
