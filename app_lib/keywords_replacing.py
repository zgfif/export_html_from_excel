import re



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
        # print(modified_html)
        for row in self.keywords:
            keyword, value = row[0], row[1]

            if not keyword:
                continue
            
            # res = re.findall(rf"{keyword}", modified_html)
            # print(res)
            index = modified_html.find(keyword)
            if index != -1:
                print(f'find keyword: {keyword} . On position: {index} .')



        return []
        # return self._modified_html_body


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
