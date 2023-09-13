'''
CS 5001 Fall 2022
Milestone 2
Yunke Li

This program tests the DrinkingFountains class in Class_DrinkingFountains.py
'''

import unittest
from Class_Parks import *
from Class_DrinkingFountains import *


class DrinkingFountainsTest(unittest.TestCase):
    '''
    Test class DrinkingFountains's __init__, __str__ and __eq__.
    '''
    # test __init__()
    def test_init_variables(self):
        fountain_1 = DrinkingFountains(['Almond Park', 'Kitsilano', 'S-side of playground', 'spring to fall'])
        self.assertEqual(fountain_1.name, 'Almond Park')
        self.assertEqual(fountain_1.neighbourhood, 'Kitsilano')
        self.assertEqual(fountain_1.location, 'S-side of playground')
        self.assertEqual(fountain_1.open_time, 'spring to fall')
        
    def test_init_variables_type_error(self):
        with self.assertRaises(TypeError):
            fountain_2 = DrinkingFountains(('Almond Park', 'Kitsilano', 'S-side of playground', 'spring to fall'))

    def test_init_variables_index_error(self):
        with self.assertRaises(IndexError):
            fountain_3 = DrinkingFountains(['Almond Park', 'Kitsilano', 'S-side of playground'])       


    # test __str__()
    def test_str_method(self):
        fountain_4 = DrinkingFountains(['Almond Park', 'Kitsilano', 'S-side of playground', 'spring to fall'])
        actual_str = str(fountain_4)
        target_str = "Almond Park public drinking fountain locates in Kitsilano neighbourhood. Its precise location is at S-side of playground, and open time is spring to fall."
        self.assertEqual(actual_str, target_str)


    # test __eq__()
    def test_eq_method(self):
        fountain_5 = DrinkingFountains(['Almond Park', 'Kitsilano', 'S-side of playground', 'spring to fall'])
        fountain_6 = DrinkingFountains(['Almond Park', 'Kitsilano', 'S-side of playground', 'spring to fall'])
        self.assertEqual(fountain_5, fountain_6)

    def test_eq_method_type_error(self):
        with self.assertRaises(TypeError):
            fountain_7 = DrinkingFountains(['Almond Park', 'Kitsilano', 'S-side of playground', 'spring to fall'])
            fountain_8 = Parks(['Arbutus Village Park', 'Arbutus-Ridge', 'has washroom'])
            self.assertEqual(fountain_7, fountain_8)


def main():

     unittest.main(verbosity = 3)

main()




