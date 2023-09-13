'''
CS 5001 Fall 2022
Milestone 2
Yunke Li

This program tests the Parks class in Class_Parks.py
'''

import unittest
from Class_Parks import *
from Class_DrinkingFountains import *


class ParksTest(unittest.TestCase):
    '''
    Test class Parks's __init__, __str__ and __eq__.
    '''
    # test __init__()
    def test_init_variables(self):
        park_1 = Parks(['Arbutus Village Park', 'Arbutus-Ridge', 'has washroom'])
        self.assertEqual(park_1.name, 'Arbutus Village Park')
        self.assertEqual(park_1.neighbourhood, 'Arbutus-Ridge')
        self.assertEqual(park_1.washroom, 'has washroom')
        
    def test_init_variables_type_error(self):
        with self.assertRaises(TypeError):
            park_2 = Parks(('Arbutus Village Park', 'Arbutus-Ridge', 'has washroom'))

    def test_init_variables_index_error(self):
        with self.assertRaises(IndexError):
            park_3 = Parks(['Arbutus Village Park', 'Arbutus-Ridge'])       


    # test __str__()
    def test_str_method(self):
        park_4 = Parks(['Arbutus Village Park', 'Arbutus-Ridge', 'has washroom'])
        actual_str = str(park_4)
        target_str = "Arbutus Village Park is in Arbutus-Ridge neighbourhood, it has washroom."
        self.assertEqual(actual_str, target_str)


    # test __eq__()
    def test_eq_method(self):
        park_5 = Parks(['Arbutus Village Park', 'Arbutus-Ridge', 'has washroom'])
        park_6 = Parks(['Arbutus Village Park', 'Arbutus-Ridge', 'has washroom'])
        self.assertEqual(park_5, park_6)

    def test_eq_method_type_error(self):
        with self.assertRaises(TypeError):
            park_7 = Parks(['Arbutus Village Park', 'Arbutus-Ridge', 'has washroom'])
            park_8 = DrinkingFountains(['Almond Park', 'Kitsilano', 'S-side of playground', 'spring to fall'])
            self.assertEqual(park_7, park_8)


def main():

     unittest.main(verbosity = 3)

main()




