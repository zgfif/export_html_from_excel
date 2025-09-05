from app_lib.xlsx_file import XlsxFile
from app_lib.helpers.group_elements_by_two import group_elements_by_two



class KeywordsPairs:
    """
    This class extracts keywords pairs from file 'keywords.xlsx'.
    """


    def __init__(self) -> None:
        """
        Initialize with path to keywords file.
        """
        self._filepath = 'sources/keywords.xlsx'

    

    def extract(self) -> tuple[tuple[str | None], ...]:
        """
        Read XLSX file and return list of keyword, value pairs.
        """
        grouped_pairs = []

        with XlsxFile(self._filepath) as xf:
            data = xf.data_rows()

        for row in data:
            new_grouped_pairs = group_elements_by_two(row)
            grouped_pairs.extend(new_grouped_pairs)
        
        return tuple(grouped_pairs)
