from app_lib.xlsx_file import XlsxFile
from app_lib.html_file import HtmlFile
from app_lib.keywords_replacing import KeywordsReplacing
from app_lib.keywords_pairs import KeywordsPairs
from app_lib.logger import Logger
import os




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
        self._logger = Logger(filepath='logs/app.log').setup()

    

    def generate(self) -> None:
        """
        Generate HTML files from the content of the XLSX file.
        """
        self._validate_output_directory()

        with XlsxFile(filepath=self._filepath) as xf:
            data = xf.data_rows()
        
        keywords_pairs = self._keywords_pairs()

        for row in data:
            
            html_name, html_content = row[0], row[1]
        
            self._logger.info('Start processing \'%s\' ...', html_name)
        
            content = KeywordsReplacing(html=html_content, keywords=keywords_pairs).perform()

            html_filepath = os.path.join(self._output_directory, html_name)

            HtmlFile(filepath=html_filepath).write(content=content)

        self._logger.info('Congratulations! We have finished processing!')


    
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



    def _keywords_pairs(self) -> tuple[tuple[str, str], ...]:
        """
        Return the sequence of key, value pairs.

        Example:
            ((key1, value1), (key2, value2), ... (keyN, valueN))
        """
        return KeywordsPairs().extract()
