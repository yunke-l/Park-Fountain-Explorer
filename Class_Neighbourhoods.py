'''
CS 5001 Fall 2022
Milestone 2
Yunke Li

This program create the Neighbourhoods class with many methods, incuding __str__ and __eq__.
'''
from CONSTANTS import *


class Neighbourhoods:
    '''
    Class: Neighbourhoods
    It knows how to create a Neighbourhoods object with a given list, print object's attributes,
    and compare different objects (for equality). 
    '''
    def __init__(self, neighbourhoods_class_input_list):
        if type(neighbourhoods_class_input_list) != list:
            raise TypeError("Error happens in class Neighbourhoods file, in __init__, neighbourhoods_class_input_list must be a list.")
        if len(neighbourhoods_class_input_list) != NEIGHBOURHOODS_LIST_LEN:
            raise IndexError("Error happens in class Neighbourhoods, in __init__, neighbourhoods_class_input_list's length must be 5.")

        self.name = neighbourhoods_class_input_list[0]
        self.num_of_parks = neighbourhoods_class_input_list[1]
        self.num_of_fountains = neighbourhoods_class_input_list[2]
        self.parks = neighbourhoods_class_input_list[3]
        self.fountains = neighbourhoods_class_input_list[4]


    def __str__(self):
        '''
        Returns a string representation of Neighbourhoods instances
        '''    
        new_line = '\n'
        description = f"{self.name} has {self.num_of_parks} parks and {self.num_of_fountains} public drinking fountains.\n"            
        parks_details = f"Parks: {new_line}{new_line.join(self.parks)} \n"
        fountains_details = f"Fountains position: {new_line}{new_line.join(self.fountains)}"
        output = f"{description}{new_line}{parks_details}{new_line}{fountains_details}"
        return output

  
    def __eq__(self, other_neighbourhood):
        '''
        Compares current Neighbourhoods object to another Neighbourhoods object.
        If other_neighbourhood does not belong to Neighbourhoods class, raise type error.
        Returns True if their name are equal, and False otherwise
        '''
        if not isinstance(other_neighbourhood, Neighbourhoods):
            raise TypeError("Error happens in class Neighbourhoods file, in __eq__, other_neighbourhood should also belong to Neighbourhoods class.")
        else:
            return self.name == other_neighbourhood.name


