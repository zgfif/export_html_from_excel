from app_lib.xlsx import Xlsx
from app_lib.html import Html
from app_lib.keywords_replacing import KeywordsReplacing
from app_lib.keywords_pairs import KeywordsPairs
import os
from typing import Sequence



class Webpages:
    """
    Generate HTML webpages using data from an XLSX file.
    """

    def __init__(self, filepath: str, output_directory: str = 'results') -> None:
        """
        Initialize the generator with an XLSX file and an output directory.
        
        Args:
            filepath (str): Path to the XLSX file with webpage content.
            output_directory (str): Directory where generated HTML files will be saved. 
                Defaults to 'results'.
        """
        self._filepath = filepath
        self._output_directory = output_directory

    
    def generate(self) -> None:
        """
        Generate HTML files from the content of the XLSX file.
        """
        self._validate_output_directory()

        data = Xlsx(filepath=self._filepath).data_rows()

        keywords_pairs = self._keywords_pairs()

        for row in data:
            content = KeywordsReplacing(html=row[1], keywords=keywords_pairs).perform()

            html_filepath = self._output_directory + '/' + row[0]

            Html(filepath=html_filepath).write(content=content)


    
    def _validate_output_directory(self) -> None:
        """
        Ensure that the output directory exists. 
        If it does not exist, create it.

        Raises:
            ValueError: If output_directory is not a string.
        """
        if not isinstance(self._output_directory, str):
            raise ValueError(f'Output directory {self._output_directory} must be string.')

        os.makedirs(self._output_directory, exist_ok=True)



    def _keywords_pairs(self) -> Sequence[tuple[str, str]]:
        """
        Return the sequence of key, value pairs.

        Example:
            [(key1, value1), (key2, value2), ... (keyN, valueN),]
        """
        return KeywordsPairs().extract()

