'''
CS 5001 Fall 2022
Milestone 2
Yunke Li

This program tests the Neighbourhoods class in Neighbourhoods.py
'''

import unittest
from Class_Parks import *
from Class_DrinkingFountains import *
from Class_Neighbourhoods import *


class NeighbourhoodsTest(unittest.TestCase):
    '''
    Test class Neighbourhoods's __init__, __str__ and __eq__.
    '''
    # test __init__()
    def test_init_variables(self):
        neighbourhood_1 = Neighbourhoods(['Kitsilano', 16, 17, ['Kitsilano Beach Park'], ['Almond Park']])
        self.assertEqual(neighbourhood_1.name, 'Kitsilano')
        self.assertEqual(neighbourhood_1.num_of_parks, 16)
        self.assertEqual(neighbourhood_1.num_of_fountains, 17)
        self.assertEqual(neighbourhood_1.parks, ['Kitsilano Beach Park'])
        self.assertEqual(neighbourhood_1.fountains, ['Almond Park'])
        
    def test_init_variables_type_error(self):
        with self.assertRaises(TypeError):
            neighbourhood_2 = Neighbourhoods(('Kitsilano', 16, 17, ['Kitsilano Beach Park'], ['Almond Park']))


    def test_init_variables_index_error(self):
        with self.assertRaises(IndexError):
            neighbourhood_3 = Neighbourhoods(['Kitsilano', 16, 17])


    # test __str__()
    def test_str_method(self):
        neighbourhood_4 = Neighbourhoods(['Kitsilano', 16, 17, ['Kitsilano Beach Park', 'Kitsilano Beach Park'], ['Almond Park', 'Almond Park']])
        actual_str = str(neighbourhood_4)
        new_line = '\n'
        description = f"Kitsilano has 16 parks and 17 public drinking fountains.\n" 
        parks_details = f"Parks: {new_line}{new_line.join(['Kitsilano Beach Park', 'Kitsilano Beach Park'])} \n"
        fountains_details = f"Fountains position: {new_line}{new_line.join(['Almond Park', 'Almond Park'])}"
        target_str = f"{description}{new_line}{parks_details}{new_line}{fountains_details}"

        self.assertEqual(actual_str, target_str)


    # test __eq__()
    def test_eq_method(self):
        neighbourhood_5 = Neighbourhoods(['Kitsilano', 16, 17, ['Kitsilano Beach Park'], ['Almond Park']])
        neighbourhood_6 = Neighbourhoods(['Kitsilano', 16, 17, ['Kitsilano Beach Park'], ['Almond Park']])        

        self.assertEqual(neighbourhood_5, neighbourhood_6)

    def test_eq_method_type_error(self):
        with self.assertRaises(TypeError):
            fountain_7 = DrinkingFountains(['Almond Park', 'Kitsilano', 'S-side of playground', 'spring to fall'])
            neighbourhood_7 = Neighbourhoods(['Kitsilano', 16, 17, ['Kitsilano Beach Park'], ['Almond Park']])
       
            self.assertEqual(neighbourhood_7, fountain_7)


def main():

     unittest.main(verbosity = 3)

main()




