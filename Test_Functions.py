'''
CS 5001 Fall 2022
Milestone 2
Yunke Li

This program tests the functions in these files:
Functions_read_and_clean_data.py
Functions_combine_and_process_data.py
'''

import unittest
import pandas as pd
from CONSTANTS import *
from Class_Parks import *
from Class_DrinkingFountains import *
from Class_Neighbourhoods import *
from Functions_read_and_clean_data import *
from Functions_combine_and_process_data import *


class FunctionsTest(unittest.TestCase):
    '''
    Test the functions in these files:
        Functions_read_and_clean_data.py
        Functions_combine_and_process_data.py
    '''
    # test Functions_read_and_clean_data.py
    # test read_url
    def test_read_url_type_error(self):
        with self.assertRaises(TypeError):
            url_data = read_url([])

    # test clean_parks_data
    def test_clean_parks_data(self):
        url_data = read_url(PARKS_URL)
        parks_data = clean_parks_data(url_data)
        self.assertEqual(parks_data[0], ['Arbutus Village Park', 'Arbutus-Ridge', "doesn't have washroom"])

    def test_clean_parks_data_type_error(self):
        with self.assertRaises(TypeError):
            parks_data = clean_parks_data([])

    # test clean_fountains_data
    def test_clean_fountains_data(self):
        url_data = read_url(FOUNTAINS_URL)
        fountains_data = clean_fountains_data(url_data)
        self.assertEqual(fountains_data[0], ['Almond Park', 'Kitsilano', 'S-side of playground', 'spring to fall'])

    def test_clean_fountains_data_type_error(self):
        with self.assertRaises(TypeError):
            fountains_data = clean_fountains_data([])


    # Functions_combine_and_process_data
    # test construct_class_objects_list
    def test_construct_class_objects_list(self):
        url_data = read_url(PARKS_URL)
        parks_data = clean_parks_data(url_data)
        park_obj_list = construct_class_objects_list(parks_data, Parks)

        self.assertEqual(park_obj_list[0].name, 'Arbutus Village Park')

    def test_construct_class_objects_list_type_error(self):
        with self.assertRaises(TypeError):
            park_obj_list = construct_class_objects_list('', Parks)


    #test construct_neighbourhoods_list
    def test_construct_neighbourhoods_list(self):
        url_data = read_url(PARKS_URL)
        parks_data = clean_parks_data(url_data)
        park_obj_list = construct_class_objects_list(parks_data, Parks)
        neighbourhoods_list = construct_neighbourhoods_list(park_obj_list)

        self.assertEqual(neighbourhoods_list[0], 'Arbutus-Ridge')

    def test_construct_neighbourhoods_list_type_error(self):
        with self.assertRaises(TypeError):
            neighbourhoods_list = construct_neighbourhoods_list('')


    #test count_objects_per_neighbourhood
    def test_count_objects_per_neighbourhood(self):
        url_data = read_url(PARKS_URL)
        parks_data = clean_parks_data(url_data)
        park_obj_list = construct_class_objects_list(parks_data, Parks)
        count_parks_dict = count_objects_per_neighbourhood(park_obj_list)

        self.assertEqual(count_parks_dict.get('Kitsilano'), 16)
                        
    def test_count_objects_per_neighbourhood_type_error(self):
        with self.assertRaises(TypeError):
            count_parks_dict = count_objects_per_neighbourhood('')
        
       
    # test construct_items_num_list
    def test_construct_items_num_list(self):
        url_data = read_url(PARKS_URL)
        parks_data = clean_parks_data(url_data)
        park_obj_list = construct_class_objects_list(parks_data, Parks)
        neighbourhoods_list = construct_neighbourhoods_list(park_obj_list)
        count_parks_dict = count_objects_per_neighbourhood(park_obj_list)
        parks_num_list = construct_items_num_list(neighbourhoods_list, count_parks_dict)

        self.assertEqual(parks_num_list[0], 10)

    def test_construct_items_num_list_type_error_1st_parameter(self):
        with self.assertRaises(TypeError):
            parks_num_list = construct_items_num_list('', {})

    def test_construct_items_num_list_type_error_2nd_parameter(self):
        with self.assertRaises(TypeError):
            parks_num_list = construct_items_num_list([], '')


    # test construct_neighbourhoods_data_list
    def test_construct_neighbourhoods_data_list(self):
        park_url_data = read_url(PARKS_URL)
        fountain_url_data = read_url(FOUNTAINS_URL)
        parks_data = clean_parks_data(park_url_data)
        fountains_data = clean_fountains_data(fountain_url_data)
        park_obj_list = construct_class_objects_list(parks_data, Parks)
        fountain_obj_list = construct_class_objects_list(fountains_data, DrinkingFountains)
        neighbourhoods_list = construct_neighbourhoods_list(park_obj_list)
        count_parks_dict = count_objects_per_neighbourhood(park_obj_list)
        count_fountains_dict = count_objects_per_neighbourhood(fountain_obj_list)
        parks_num_list = construct_items_num_list(neighbourhoods_list, count_parks_dict)
        fountains_num_list = construct_items_num_list(neighbourhoods_list, count_fountains_dict)
        neighbourhoods_data = construct_neighbourhoods_data_list(neighbourhoods_list, parks_num_list, fountains_num_list)

        self.assertEqual(neighbourhoods_data[0], neighbourhoods_list)
        self.assertEqual(neighbourhoods_data[1], parks_num_list)
        self.assertEqual(neighbourhoods_data[2], fountains_num_list)

    def test_construct_neighbourhoods_data_list_type_error_1st_parameter(self):
        with self.assertRaises(TypeError):
            neighbourhoods_data = construct_neighbourhoods_data_list('', [], [])
    
    def test_construct_neighbourhoods_data_list_type_error_2nd_parameter(self):
        with self.assertRaises(TypeError):
            neighbourhoods_data = construct_neighbourhoods_data_list([], '', [])

    def test_construct_neighbourhoods_data_list_type_error_3rd_parameter(self):
        with self.assertRaises(TypeError):
            neighbourhoods_data = construct_neighbourhoods_data_list([], [], '')


    # test construct_neighbourhoods_data_dict
    def test_construct_neighbourhoods_data_dict(self):
        park_url_data = read_url(PARKS_URL)
        fountain_url_data = read_url(FOUNTAINS_URL)
        parks_data = clean_parks_data(park_url_data)
        fountains_data = clean_fountains_data(fountain_url_data)
        park_obj_list = construct_class_objects_list(parks_data, Parks)
        fountain_obj_list = construct_class_objects_list(fountains_data, DrinkingFountains)
        neighbourhoods_list = construct_neighbourhoods_list(park_obj_list)
        count_parks_dict = count_objects_per_neighbourhood(park_obj_list)
        count_fountains_dict = count_objects_per_neighbourhood(fountain_obj_list)
        parks_num_list = construct_items_num_list(neighbourhoods_list, count_parks_dict)
        fountains_num_list = construct_items_num_list(neighbourhoods_list, count_fountains_dict)
        neighbourhoods_data = construct_neighbourhoods_data_list(neighbourhoods_list, parks_num_list, fountains_num_list)
        neighbourhoods_data_dict = construct_neighbourhoods_data_dict(HEADERS, neighbourhoods_data)

        self.assertEqual(neighbourhoods_data_dict.get('Neighbourhood'), neighbourhoods_list)          

    def test_construct_neighbourhoods_data_dict_type_error_1st_parameter(self):
        with self.assertRaises(TypeError):
            neighbourhoods_data_dict = construct_neighbourhoods_data_dict('', [])

    def test_construct_neighbourhoods_data_dict_type_error_1st_parameter(self):
        with self.assertRaises(TypeError):
            neighbourhoods_data_dict = construct_neighbourhoods_data_dict([], '')


    # test construct_data_frame
    def test_construct_data_frame(self):
        park_url_data = read_url(PARKS_URL)
        fountain_url_data = read_url(FOUNTAINS_URL)
        parks_data = clean_parks_data(park_url_data)
        fountains_data = clean_fountains_data(fountain_url_data)
        park_obj_list = construct_class_objects_list(parks_data, Parks)
        fountain_obj_list = construct_class_objects_list(fountains_data, DrinkingFountains)
        neighbourhoods_list = construct_neighbourhoods_list(park_obj_list)
        count_parks_dict = count_objects_per_neighbourhood(park_obj_list)
        count_fountains_dict = count_objects_per_neighbourhood(fountain_obj_list)
        parks_num_list = construct_items_num_list(neighbourhoods_list, count_parks_dict)
        fountains_num_list = construct_items_num_list(neighbourhoods_list, count_fountains_dict)
        neighbourhoods_data = construct_neighbourhoods_data_list(neighbourhoods_list, parks_num_list, fountains_num_list)
        neighbourhoods_data_dict = construct_neighbourhoods_data_dict(HEADERS, neighbourhoods_data)
        data_frame = construct_data_frame(neighbourhoods_data_dict)

        self.assertEqual(type(data_frame), pd.core.frame.DataFrame)    

    def test_construct_data_frame_type_error(self):
        with self.assertRaises(TypeError):
            data_frame = construct_data_frame([])


    # test construct_neighbourhoods_items_dict
    def test_construct_neighbourhoods_items_dict(self):
        park_url_data = read_url(PARKS_URL)
        parks_data = clean_parks_data(park_url_data)
        park_obj_list = construct_class_objects_list(parks_data, Parks)
        neighbourhoods_list = construct_neighbourhoods_list(park_obj_list)
        neighbourhoods_parks_obj_dict = construct_neighbourhoods_items_dict(neighbourhoods_list, park_obj_list)

        self.assertEqual(len(neighbourhoods_parks_obj_dict.get('Arbutus-Ridge')), 10)  
        
    def test_construct_neighbourhoods_items_dict_type_error_1st_parameter(self):
        with self.assertRaises(TypeError):
            neighbourhoods_parks_obj_dict = construct_neighbourhoods_items_dict('', [])
            
    def test_construct_neighbourhoods_items_dict_type_error_2nd_parameter(self):
        with self.assertRaises(TypeError):
            neighbourhoods_parks_obj_dict = construct_neighbourhoods_items_dict([], '')


    # test construct_neighbourhoods_class_input_list
    def test_construct_neighbourhoods_class_input_list(self):
        park_url_data = read_url(PARKS_URL)
        fountain_url_data = read_url(FOUNTAINS_URL)
        parks_data = clean_parks_data(park_url_data)
        fountains_data = clean_fountains_data(fountain_url_data)
        park_obj_list = construct_class_objects_list(parks_data, Parks)
        fountain_obj_list = construct_class_objects_list(fountains_data, DrinkingFountains)
        neighbourhoods_list = construct_neighbourhoods_list(park_obj_list)
        count_parks_dict = count_objects_per_neighbourhood(park_obj_list)
        count_fountains_dict = count_objects_per_neighbourhood(fountain_obj_list)
        parks_num_list = construct_items_num_list(neighbourhoods_list, count_parks_dict)
        fountains_num_list = construct_items_num_list(neighbourhoods_list, count_fountains_dict)
        neighbourhoods_data = construct_neighbourhoods_data_list(neighbourhoods_list, parks_num_list, fountains_num_list)
        neighbourhoods_data_dict = construct_neighbourhoods_data_dict(HEADERS, neighbourhoods_data)
        data_frame = construct_data_frame(neighbourhoods_data_dict)
        neighbourhoods_parks_obj_dict = construct_neighbourhoods_items_dict(neighbourhoods_list, park_obj_list)
        neighbourhoods_fountains_obj_dict = construct_neighbourhoods_items_dict(neighbourhoods_list, fountain_obj_list)
        neighbourhoods_data_list = construct_neighbourhoods_class_input_list(neighbourhoods_list, parks_num_list, fountains_num_list, neighbourhoods_parks_obj_dict, neighbourhoods_fountains_obj_dict)

        self.assertEqual(neighbourhoods_data_list[0][0], 'Arbutus-Ridge')
        self.assertEqual(neighbourhoods_data_list[0][1], 10)
        self.assertEqual(neighbourhoods_data_list[0][2], 4)

    def test_construct_neighbourhoods_class_input_list_type_error_1st_parameter(self):
        with self.assertRaises(TypeError):
            neighbourhoods_data_list = construct_neighbourhoods_class_input_list('', [], [], {}, {})        

    def test_construct_neighbourhoods_class_input_list_type_error_2nd_parameter(self):
        with self.assertRaises(TypeError):
            neighbourhoods_data_list = construct_neighbourhoods_class_input_list([], '', [], {}, {})

    def test_construct_neighbourhoods_class_input_list_type_error_3rd_parameter(self):
        with self.assertRaises(TypeError):
            neighbourhoods_data_list = construct_neighbourhoods_class_input_list([], [], '', {}, {})

    def test_construct_neighbourhoods_class_input_list_type_error_4th_parameter(self):
        with self.assertRaises(TypeError):
            neighbourhoods_data_list = construct_neighbourhoods_class_input_list([], [], [], [], {})

    def test_construct_neighbourhoods_class_input_list_type_error_5th_parameter(self):
        with self.assertRaises(TypeError):
            neighbourhoods_data_list = construct_neighbourhoods_class_input_list([], [], [], {}, []) 


    # test construct_neighbourhoods_str_dict
    def test_construct_neighbourhoods_str_dict(self):
        park_url_data = read_url(PARKS_URL)
        fountain_url_data = read_url(FOUNTAINS_URL)
        parks_data = clean_parks_data(park_url_data)
        fountains_data = clean_fountains_data(fountain_url_data)
        park_obj_list = construct_class_objects_list(parks_data, Parks)
        fountain_obj_list = construct_class_objects_list(fountains_data, DrinkingFountains)
        neighbourhoods_list = construct_neighbourhoods_list(park_obj_list)
        count_parks_dict = count_objects_per_neighbourhood(park_obj_list)
        count_fountains_dict = count_objects_per_neighbourhood(fountain_obj_list)
        parks_num_list = construct_items_num_list(neighbourhoods_list, count_parks_dict)
        fountains_num_list = construct_items_num_list(neighbourhoods_list, count_fountains_dict)
        neighbourhoods_data = construct_neighbourhoods_data_list(neighbourhoods_list, parks_num_list, fountains_num_list)
        neighbourhoods_data_dict = construct_neighbourhoods_data_dict(HEADERS, neighbourhoods_data)
        data_frame = construct_data_frame(neighbourhoods_data_dict)
        neighbourhoods_parks_obj_dict = construct_neighbourhoods_items_dict(neighbourhoods_list, park_obj_list)
        neighbourhoods_fountains_obj_dict = construct_neighbourhoods_items_dict(neighbourhoods_list, fountain_obj_list)
        neighbourhoods_data_list = construct_neighbourhoods_class_input_list(neighbourhoods_list, parks_num_list, fountains_num_list, neighbourhoods_parks_obj_dict, neighbourhoods_fountains_obj_dict)
        neighbourhood_obj_list = construct_class_objects_list(neighbourhoods_data_list, Neighbourhoods)
        neighbourhoods_str_dict = construct_neighbourhoods_str_dict(neighbourhood_obj_list)

        self.assertEqual(neighbourhoods_str_dict.get('Arbutus-Ridge'), (neighbourhood_obj_list[0]).__str__())

    def test_construct_neighbourhoods_str_dict_type_error(self):
        with self.assertRaises(TypeError):
            eighbourhoods_str_dict = construct_neighbourhoods_str_dict({})



def main():

     unittest.main(verbosity = 3)

main()




