import unittest
from app_lib.helpers.group_elements_by_two import group_elements_by_two




class TestGroupByTwo(unittest.TestCase):
    def test_group_elements_by_two(self):
        main_row = [
            'Bending Machine',	'<a href="https://www.topeintl.com/en/bending-machine.html" >Bending Machine</a>',	
            '折弯机',	'<a href="https://www.topeintl.com/cn/折弯机.html" >折弯机</a>', 
            'La Maquina Dobladora Universal', '<a href="https://www.topeintl.com/maquinas-para-doblar.html" >La Maquina Dobladora Universal</a>',
            'A Máquina Para Curvar Tubo',	'<a href="https://www.topeintl.com/pt/maquinas-para-dobrar.html" >A Máquina Para Curvar Tubo</a>',	
            'La Cintreuse',	'<a href="https://www.topeintl.com/fr/cintreuse.html" >La Cintreuse</a>', 
            'La Macchina Piegatrice', '<a href="https://www.topeintl.com/it/piegatrice.html" >La Macchina Piegatrice</a>'
        ]
        
        result = group_elements_by_two(main_row)

        self.assertListEqual(result[0], ['Bending Machine',	'<a href="https://www.topeintl.com/en/bending-machine.html" >Bending Machine</a>',])
        self.assertListEqual(result[1], ['折弯机',	'<a href="https://www.topeintl.com/cn/折弯机.html" >折弯机</a>',])
        self.assertListEqual(result[2], ['La Maquina Dobladora Universal', '<a href="https://www.topeintl.com/maquinas-para-doblar.html" >La Maquina Dobladora Universal</a>',])
        self.assertListEqual(result[3], ['A Máquina Para Curvar Tubo',	'<a href="https://www.topeintl.com/pt/maquinas-para-dobrar.html" >A Máquina Para Curvar Tubo</a>',])
        self.assertListEqual(result[4], ['La Cintreuse',	'<a href="https://www.topeintl.com/fr/cintreuse.html" >La Cintreuse</a>',])
        self.assertListEqual(result[5], ['La Macchina Piegatrice', '<a href="https://www.topeintl.com/it/piegatrice.html" >La Macchina Piegatrice</a>',])


    
    def test_when_odd_count_of_elements(self):
        with self.assertRaises(ValueError) as cm:
            group_elements_by_two(['a', 'b', 'c', 'd', 'e'])

        self.assertIn('The list must have an even count of elements.', str(cm.exception))



    def test_when_no_elements(self):
        result = group_elements_by_two([])

        self.assertEqual(len(result), 0)
