from app_lib.xlsx import Xlsx
from app_lib.helpers.group_elements_by_two import group_elements_by_two



class KeywordsPairs:
    """
    This class extracts keywords pairs from file 'keywords.xlsx'.
    """


    def __init__(self,) -> None:
        """
        Initialize with path to keywords file.
        """
        self._filepath = 'sources/keywords.xlsx'

    

    def extract(self) -> list[list[str, str],]:
        """
        Read XLSX file and return list of keyword, value pairs.
        """
        grouped_list = []
        data = Xlsx(self._filepath).data_rows()

        
        for row in data:
            lst = list(row)
            lst = group_elements_by_two(lst)
            grouped_list.extend(lst)
        return grouped_list
        

        