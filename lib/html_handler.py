class HtmlHandler:
    def __init__(self, filepath: str) -> None:
        """Initialization with filepath variable."""
        self._filepath = filepath
        self._create_html(filepath)


    def _create_html(self, filepath: str ='') -> None:
        """Create an 'filepath.html' file."""
        if not isinstance(filepath, str):
            return
        

    def write(self, content: str ='') -> None:
        """Create 'filepath.html' file and save the content to it."""
        if not content or not isinstance(content, str):
            return
        
        with open(file=self._filepath, mode='w', encoding='UTF-8') as f:
            f.write(content.strip('\n'))
