from openpyxl import load_workbook



class Xlsx:
    def __init__(self, filepath: str) -> None:
        self._work_book = load_workbook(filepath, data_only=True)


    def column_names(self) -> list[str]:
        # Выбрать лист
        sheet = self._work_book.active  # или wb["ИмяЛиста"]

        reader = sheet.iter_rows(values_only=True)
        row = next(reader, None)

        return [cell for cell in row if cell]


    def data_rows(self) ->list[list[str]]:
        data = []
        sheet = self._work_book.active
        reader = sheet.iter_rows(values_only=True)
        next(reader, None)
        for row in reader:
            data.append(row)
        
        return data