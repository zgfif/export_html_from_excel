class HtmlFile:
    """
    A helper class for creating and writing to an HTML file.

    Attributes:
        filepath (str): Path where the HTML file will be created.
    """

    def __init__(self, filepath: str) -> None:
        """
        Initialize the Html object with a file path.

        Args:
            filepath (str): Path to the HTML file to be created or overwritten.
        """
        self._filepath = filepath
        

    def write(self, content: str = '') -> None:
        """
        Write content to the HTML file.

        The file will be created or overwritten at the specified path.
        Leading and trailing whitespace characters are removed before writing.

        Args:
            content (str): The text content to write into the file. Defaults to an empty string.

        Raises:
            ValueError: If content is not a string.
        """
        if not isinstance(content, str):
            raise ValueError(f'Content for {self._filepath} must be a string.')
        
        with open(self._filepath, 'w', encoding='UTF-8') as f:
            f.write(content.strip('\n'))
