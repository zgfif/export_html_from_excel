import unittest
from lib.xlsx import Xlsx
# from tests.html_example import HTML_EXAMPLE


class TestXlsx(unittest.TestCase):
    def test_retrieve_column_names(self):
        column_names = Xlsx('sources/webpage.xlsx').column_names()

        self.assertListEqual(column_names, ['url|cn', 'html|cn'], 'Incorrect column names')


    def test_retrieve_data_rows(self):
        data_rows = Xlsx('sources/webpage.xlsx').data_rows()
        self.assertEqual(data_rows[0][0], '1.html')


    def test_retrieve_data_rows(self):
        retrieved_rows = Xlsx('sources/keywords.xlsx').data_rows()

        expected_row = ['Bending Machine',	'<a href="https://www.topeintl.com/en/bending-machine.html" >Bending Machine</a>',	
                        '折弯机',	'<a href="https://www.topeintl.com/cn/折弯机.html" >折弯机</a>', 
                        'La Maquina Dobladora Universal', '<a href="https://www.topeintl.com/maquinas-para-doblar.html" >La Maquina Dobladora Universal</a>',
                        'A Máquina Para Curvar Tubo',	'<a href="https://www.topeintl.com/pt/maquinas-para-dobrar.html" >A Máquina Para Curvar Tubo</a>',	
                        'La Cintreuse',	'<a href="https://www.topeintl.com/fr/cintreuse.html" >La Cintreuse</a>', 
                        'La Macchina Piegatrice	', '<a href="https://www.topeintl.com/it/piegatrice.html" >La Macchina Piegatrice</a>'
                        ]
        # print(len(expected_row))
        self.assertEqual(retrieved_rows[0][0], expected_row[0])
        self.assertEqual(retrieved_rows[0][1], expected_row[1])