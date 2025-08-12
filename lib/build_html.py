class BuildHtml:
    def __init__(self, html_body: str, keywords: list[list[str, str]]) -> None:
        self._html_body = html_body
        self._keywords = keywords


    def perform(self) -> str:
        pass
        # if not self._keywords:
            # return self._html_body
        
        # self._modified_html_body = self._html_body

        # for pair in self._keywords:
        #     keyword, value = pair[0], pair[1]

        #     # self._modified_html_body = self._modified_html_body.replace(keyword, value)
        #     index = self._modified_html_body.find(pair[0])
        #     if index != -1:
        #         print(f"Keyword '{pair[0]}' has been found on position: {index} !!!!!!!!!!")
        #     else:
        #         print(f"Keyword '{pair[0]}' hasn't been found.")


        # return self._modified_html_body
