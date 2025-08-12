class HtmlHandler:
    def __init__(self, filepath: str) -> None:
        self._filepath = filepath
        self._create_html(filepath)


    def _create_html(self, filepath: str ='') -> None:
        if not isinstance(filepath, str):
            return
        

    def write(self, content: str ='') -> None:
        if not content or not isinstance(content, str):
            return
        
        with open(file=self._filepath, mode='w', encoding='UTF-8') as f:
            f.write(content.strip('\n'))
