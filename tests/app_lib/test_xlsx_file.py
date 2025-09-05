import unittest
from app_lib.xlsx_file import XlsxFile




class TestXlsx(unittest.TestCase):
    def test_retrieve_column_names(self):
        with XlsxFile('sources/webpage.xlsx') as xf:
            column_names = xf.column_names()

        self.assertTupleEqual(column_names, ('url|cn', 'html|cn'), 'Incorrect column names')



    def test_retrieve_data_first_row_first_cell(self):
        with XlsxFile('sources/webpage.xlsx') as xf:
            data_rows = xf.data_rows()

        self.assertEqual(data_rows[0][0], '1.html')



    def test_retrieve_all_data_rows(self):
        with XlsxFile('sources/keywords.xlsx') as xf:
            data_rows = xf.data_rows()

        expected_row = (
            'Bending Machine', 
            '<a href="https://www.topeintl.com/en/bending-machine.html" >Bending Machine</a>',	
            '折弯机', 
            '<a href="https://www.topeintl.com/cn/折弯机.html" >折弯机</a>', 
            'La Maquina Dobladora Universal', 
            '<a href="https://www.topeintl.com/maquinas-para-doblar.html" >La Maquina Dobladora Universal</a>',
            'A Máquina Para Curvar Tubo',	
            '<a href="https://www.topeintl.com/pt/maquinas-para-dobrar.html" >A Máquina Para Curvar Tubo</a>',	
            'La Cintreuse',	
            '<a href="https://www.topeintl.com/fr/cintreuse.html" >La Cintreuse</a>', 
            'La Macchina Piegatrice	', 
            '<a href="https://www.topeintl.com/it/piegatrice.html" >La Macchina Piegatrice</a>'
        )

        self.assertIsInstance(data_rows, tuple)
        self.assertEqual(data_rows[0][0], expected_row[0])
        self.assertEqual(data_rows[0][1], expected_row[1])
