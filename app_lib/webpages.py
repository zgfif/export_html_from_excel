from app_lib.xlsx import Xlsx
from app_lib.html import Html
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

    
    def generate(self) -> None:
        """
        Generate HTML files from the content of the XLSX file.
        """
        self._validate_output_directory()

        data = Xlsx(filepath=self._filepath).data_rows()

        for row in data:
            Html(filepath=self._output_directory + '/' + row[0]).write(content=row[1])


    
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
