class BuildHtml:
    """This class is used to find all keywords and replace them with values from sources/keywords.xlsx"""
    
    def __init__(self, html_body: str, keywords: list[list[str, str]]) -> None:
        self._html_body = html_body # html code to perform replacing
        self._keywords = keywords # contains the list [[key1, value1], [key2, value2],...[keyN,valueN]]


    def perform(self) -> str:
        """Replaces all found keywords with values from 'sources/keywords.xlsx'"""
        if not self._keywords:
            return self._html_body
        
        self._modified_html_body = self._html_body
        # print(len(self._keywords))
        for row in self._keywords:
            # print(row)
            for pair in row:
                # print(pair)
                keyword, value = pair[0], pair[1]

                if not keyword:
                    continue

            # self._modified_html_body = self._modified_html_body.replace(keyword, value)
                # index = self._modified_html_body.find(keyword)
                index = self._modified_html_body.find(f'<a href="{keyword}.html" >{keyword}</a>')
                if index != -1:
                    print(f"Keyword '<a href=\"{keyword}.html\" >{keyword}</a>' has been found on position: {index} !!!!!!!!!!")
                    print(f"Keyword '<a href=\"{keyword}.html\" >{keyword}</a>'will be repaced with '{value}'")

                else:
                    # print(f"Keyword '{pair[0]}' hasn't been found.")
                    pass


        return []
        # return self._modified_html_body
