'''
CS 5001 Fall 2022
Milestone 2
Yunke Li

This program calls all functions to display GUI and show analysis results.
'''
from CONSTANTS import *
from Class_Parks import *
from Class_DrinkingFountains import *
from Class_Neighbourhoods import *
from Class_Display_TK_Window import *
from Functions_read_and_clean_data import *
from Functions_combine_and_process_data import *
from Functions_display_data_by_Matplotlib import *



def call_functions_and_display_analysis_results(parks_url, fountains_url, headers):
    '''
    Function -- call_functions_and_display_analysis_results
        call the functions to implement data extraction, cleaning, analysis, and display results.
    Parameters:
        parks_url -- str
        fountains_url -- str
        headers -- list
    Return nothing but display the Tkinter GUI.
    '''
    # Model
    # get the response of a url link of a csv file, read its values and store it as a long string
    parks_url_data = read_url(parks_url)
    fountains_url_data = read_url(fountains_url)

    # clean the csv data of parks and drinking fountains
    parks_data = clean_parks_data(parks_url_data)
    fountains_data = clean_fountains_data(fountains_url_data)

    # create lists of objects of Parks and DrinkingFountains classes
    park_objects_list = construct_class_objects_list(parks_data, Parks)
    fountain_objects_list = construct_class_objects_list(fountains_data, DrinkingFountains)

    # create dictionaries with neighbourhood names as keys and number of Parks/DrinkingFountains as values
    parks_per_neighbourhood_dict = count_objects_per_neighbourhood(park_objects_list)
    fountains_per_neighbourhood_dict = count_objects_per_neighbourhood(fountain_objects_list)  

    # create associated lists of neighbourhood names, number of parks, and number of drinking fountains 
    neighbourhoods_list = construct_neighbourhoods_list(park_objects_list)
    parks_num_list = construct_items_num_list(neighbourhoods_list, parks_per_neighbourhood_dict)
    fountains_num_list = construct_items_num_list(neighbourhoods_list, fountains_per_neighbourhood_dict)
    
    # create a nested list of the 3 associated lists above
    neighbourhoods_data_list = construct_neighbourhoods_data_list(neighbourhoods_list, parks_num_list, fountains_num_list)

    # create a dictionary with headers as keys and the 3 list above as values.
    neighbourhoods_data_dict = construct_neighbourhoods_data_dict(headers, neighbourhoods_data_list)

    # turn neighbourhoods_data_dict into data frame
    data_frame = construct_data_frame(neighbourhoods_data_dict)
    
    # create a dictionaries with neighbourhood names as keys and list of associated Parks/DrinkingFountains objects as values
    neighbourhoods_parks_dict = construct_neighbourhoods_items_dict(neighbourhoods_list, park_objects_list)
    neighbourhoods_fountains_dict = construct_neighbourhoods_items_dict(neighbourhoods_list, fountain_objects_list)

    # create a list, each item of the list includes: neighbourhood name, num of parks and fountains, lists of Parks objects and DrinkingFountains objects
    neighbourhoods_data = construct_neighbourhoods_class_input_list(neighbourhoods_list, parks_num_list, fountains_num_list, neighbourhoods_parks_dict, neighbourhoods_fountains_dict)

    # create lists of objects of Neighbourhoods class
    neighbourhoods_objects_list = construct_class_objects_list(neighbourhoods_data, Neighbourhoods)

    # create a dictionary with neibourhood names as keys and __str__ of Neighbourhood object as values
    neighbourhoods_str_dict = construct_neighbourhoods_str_dict(neighbourhoods_objects_list)


 
    # Controller (View functions are called inside Tkinter class)
    # initiation of Tk window
    root = tk.Tk()
    root.title(INIT_TITLE)
    root.rowconfigure(ROW_CONFIG, minsize = ROW_MINSIZE, weight = ROW_WEIGHT)
    root.columnconfigure(COLUMN_CONFIG, minsize = COLUMN_MINSIZE, weight = COLUMN_WEIGHT)
    # create a Display_TK_Window object
    window = Display_TK_Window(root, data_frame, neighbourhoods_list, neighbourhoods_str_dict)
    root.mainloop()

    
