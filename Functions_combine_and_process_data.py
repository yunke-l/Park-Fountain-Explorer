'''
CS 5001 Fall 2022
Milestone 2
Yunke Li

This program includes all the functions for data analysis.
'''

import pandas as pd

def construct_neighbourhoods_list(park_objects_list):
    '''
    Function -- construct_neighbourhoods_list
        create a list of neighbourhood names.
    Parameter:
        park_objects_list -- list, a list of objects of Parks class
    Return neighbourhoods_list, a list of neighbourhood names.
    If park_objects_list is not a list, raise type error.
    '''
    if type(park_objects_list) != list:
        raise TypeError("Error happens in construct_neighbourhoods_list(), parameter is not a list.")
    
    neighbourhoods_list = []
    
    for park in park_objects_list:
        if park.neighbourhood not in neighbourhoods_list:
            neighbourhoods_list.append(park.neighbourhood)
            
    return neighbourhoods_list


def construct_class_objects_list(data_list, class_name):
    '''
    Function -- construct_class_objects_list
        use a list to generate class objects.
    Parameters:
        data_list -- list, a list of data
        class_name -- str, name of a class
    Return objects_list, a list of objects created from the given class.
    If data_list is not a list, raise type error.
    '''
    if type(data_list) != list:
        raise TypeError("Error happens in construct_class_objects_list(), parameter is not a list.")
    
    objects_list = []
    
    for data in data_list:
        obj = class_name(data)
        objects_list.append(obj)

    return objects_list


def count_objects_per_neighbourhood(objects_list):
    '''
    Function -- count_objects_per_neighbourhood
        count the number of objects in same neighbourhood.
    Parameter:
        objects_list -- list, a list of objects for a class
    Return count_dict, a dictionary with neighbourhood names as keys and number of target objects as values. 
    If objects_list is not a list, raise type error.
    '''
    if type(objects_list) != list:
        raise TypeError("Error happens in count_objects_per_neighbourhood(), parameter is not a list.")
    
    count_dict = {}
    
    for obj in objects_list:
        if obj.neighbourhood in count_dict:
            count_dict[obj.neighbourhood] += 1
        else:
            count_dict[obj.neighbourhood] = 1
                
    return count_dict
            


def construct_items_num_list(neighbourhoods_list, items_per_neighbourhood):
    '''
    Function -- construct_items_num_list
        create a list of items numbers, associated with neibourhoods_list.
    Parameters:
        neighbourhoods_list -- list, a list of neighbourhood names
        items_per_neighbourhood -- dict, a dictionary with neighbourhood names as keys and number of items as values. 
    Return items_num_list, a list of items numbers, associated with neibourhoods_list.
    If neighbourhoods_list is not a list, raise type error.
    If items_per_neighbourhood is not a dictionary, raise type error.
    '''
    if type(neighbourhoods_list) != list:
        raise TypeError("Error happens in construct_items_num_list(), parameter neighbourhoods_list is not a list.")
    if type(items_per_neighbourhood) != dict:
        raise TypeError("Error happens in construct_items_num_list(), parameter items_per_neighbourhood is not a dictionary.")

    items_num_list = []
    
    for neighbourhood in neighbourhoods_list:
        for neighbourhood_of_items, num_of_items in items_per_neighbourhood.items():
            if neighbourhood_of_items == neighbourhood:
                items_num_list.append(num_of_items)
                
    return items_num_list


def construct_neighbourhoods_data_list(neighbourhoods_list, parks_num_list, fountains_num_list):
    '''
    Function -- construct_neighbourhoods_data_list
        create a nested list of neighbourhood data with 3 associated lists.
        the inner lists are: a list of neighbourhood names, a list of park numbers, a list of fountain numbers.
    Parameters:
        neighbourhoods_list -- list, a list of neighbourhood names
        parks_num_list -- list, a list of park numbers
        fountains_num_list -- list, a list of fountain numbers
    Return neighbourhoods_data, a nested list of the 3 given lists.
    If any of the given list is not a list, raise type error.
    '''
    if type(neighbourhoods_list) != list or type(parks_num_list) != list or type(fountains_num_list) != list:
        raise TypeError("Error happens in construct_neighbourhoods_data_list, all of the parameters must be lists.")
    
    neighbourhoods_data = [neighbourhoods_list, parks_num_list, fountains_num_list]
    return neighbourhoods_data


def construct_neighbourhoods_data_dict(headers, neighbourhoods_data_list):
    '''
    Function -- construct_neighbourhoods_data_dict
        create a dictionary with headers as keys and list as values.
    Parameters:
        headers -- list, a list of headers
        neighbourhoods_data_list -- list, a nested list of neighbourhood data with 3 associated lists.
                                    the inner lists are: a list of neighbourhood names, a list of park numbers, a list of fountain numbers.
    Return neighbourhoods_data_dict, a dictionary with headers as keys and inner lists as values.
    If any of the given list is not a list, raise type error.
    '''
    if type(neighbourhoods_data_list) != list or type(headers) != list:
        raise TypeError("Error happens in construct_neighbourhoods_data_dict, all of the parameters must be lists.")
    
    neighbourhoods_data_dict = dict(zip(headers, neighbourhoods_data_list))
    
    return neighbourhoods_data_dict


def construct_data_frame(data_dict):
    '''
    Function -- construct_data_frame
        turn a dictionary into data frame
    Parameters:
        data_dict -- dict
    Return data_frame, a pandas DataFrame
    If the given data_dict is not a dictionary, raise type error.
    '''
    if type(data_dict) != dict:
        raise TypeError("Error happens in construct_data_frame, the parameter must be a dictionary.")
    
    data_frame = pd.DataFrame(data_dict)
    
    return data_frame


def construct_neighbourhoods_items_dict(neighbourhoods_list, objects_list):
    '''
    Function -- construct_neighbourhoods_items_dict
        create a dictionary with neighbourhood names as keys and list of other objects as values
    Parameters:
        neighbourhoods_list -- list, a list of neighbourhood names
        objects_list -- list, a list of objects
    Return neighbourhoods_items_dict, a dictionary with neighbourhood names as keys and list of other objects as values
    If the inputs are not lists, raise type error.
    '''
    if type(neighbourhoods_list) != list or type(objects_list) != list:
       raise TypeError("Error happens in construct_neighbourhoods_items_dict, all of the parameters must be lists.")
      
    neighbourhoods_items_dict = {}
    
    for neighbourhood in neighbourhoods_list:
        neighbourhoods_item_list = []
        for obj in objects_list:
            if obj.neighbourhood == neighbourhood:
                neighbourhoods_item_list.append(obj.name)
        neighbourhoods_items_dict[neighbourhood] = neighbourhoods_item_list

    return neighbourhoods_items_dict
            


def construct_neighbourhoods_class_input_list(neighbourhoods_list, parks_num_list, fountains_num_list, neighbourhoods_parks_dict, neighbourhoods_fountains_dict):
    '''
    Function -- construct_neighbourhoods_class_input_list
        create a list, each item of the list includes the information of a Neighbourhoods object.
    Parameters:
        neighbourhoods_list -- list, a list of neighbourhood names
        parks_num_list -- list, a list of park numbers per neighbourhood
        fountains_num_list -- list, a list of public drinking fountain numbers per neighbourhood
        neighbourhoods_parks_dict -- dict, a dictionary with neighbourhood names as keys and list of Parks objects as values
        neighbourhoods_fountains_dict -- dict, a dictionary with neighbourhood names as keys and list of DrinkingFountains objects as values
    Return neighbourhoods_data_list, a nested list made by the given informations.
    If the inputs are not lists or dictionaries, raise type error.
    '''
    if type(neighbourhoods_list) != list or type(parks_num_list) != list or type(fountains_num_list) != list:
        raise TypeError("Error happens in construct_neighbourhoods_class_input_list, the first three parameters must be lists.")
    if type(neighbourhoods_parks_dict) != dict or type(neighbourhoods_fountains_dict) != dict:
        raise TypeError("Error happens in construct_neighbourhoods_class_input_list, the last two parameters must be dictionaries.")
    
    neighbourhoods_data_list = [0]*len((neighbourhoods_list))
    for i in range(len(neighbourhoods_list)):
        neighbourhoods_data_list[i] = [neighbourhoods_list[i], parks_num_list[i], fountains_num_list[i]]

        for key, value in neighbourhoods_parks_dict.items():
            if key == neighbourhoods_list[i]:
                neighbourhoods_data_list[i].append(value)
        for key, value in neighbourhoods_fountains_dict.items():
            if key == neighbourhoods_list[i]:
                neighbourhoods_data_list[i].append(value)
            
    return neighbourhoods_data_list


def construct_neighbourhoods_str_dict(neighbourhoods_objects_list):
    '''
    Function -- construct_neighbourhoods_str_dict
        create a dictionary with neighourhood names as keys and Neighbourhoods object __str__() outputs as values.
    Parameters:
        neighbourhoods_objects_list -- list, a list of Neighbourhoods objects
    Return neighbourhoods_str_dict, a dictionary with neighourhood names as keys and Neighbourhoods object __str__() outputs as values.
    If the input is not a list, raise type error.
    '''
    if type(neighbourhoods_objects_list) != list:
        raise TypeError("Error happens in construct_neighbourhoods_str_dict, the parameter must be a list.")
    
    neighbourhoods_str_dict = {}
    
    for neighbourhood_obj in neighbourhoods_objects_list:
        neighbourhoods_str_dict[neighbourhood_obj.name] = neighbourhood_obj.__str__()

    return neighbourhoods_str_dict
        
    

