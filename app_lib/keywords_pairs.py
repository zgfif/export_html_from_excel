from app_lib.xlsx import Xlsx
from app_lib.helpers.group_elements_by_two import group_elements_by_two
from typing import Sequence



class KeywordsPairs:
    """
    This class extracts keywords pairs from file 'keywords.xlsx'.
    """


    def __init__(self) -> None:
        """
        Initialize with path to keywords file.
        """
        self._filepath = 'sources/keywords.xlsx'

    

    def extract(self) -> Sequence[tuple[str, str]]:
        """
        Read XLSX file and return list of keyword, value pairs.
        """
        grouped_pairs = []
        data = Xlsx(self._filepath).data_rows()

        for row in data:
            new_grouped_pairs = group_elements_by_two(row)
            grouped_pairs.extend(new_grouped_pairs)
        
        return tuple(grouped_pairs)

        