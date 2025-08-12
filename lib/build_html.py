class BuildHtml:
    def __init__(self, html_body: str, keywords: list[list[str, str]]) -> None:
        self._html_body = html_body
        self._keywords = keywords


    def perform(self) -> str:
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
