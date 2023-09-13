'''
CS 5001 Fall 2022
Milestone 2
Yunke Li

This program create the Parks class with many methods, incuding __str__ and __eq__.
'''
from CONSTANTS import *


class Parks:
    '''
    Class: Parks
    It knows how to create a Parks object with a given list, print object's attributes,
    and compare different objects (for equality). 
    '''
    def __init__(self, parks_list):
        '''
        Create instances of Parks class.
        Variables:
            parks_list - list, the items of the list are: park's name, neighbourhood and washroom status.
        If parks_list is not a list, raise type error.
        If parks_list's length is not equal to 3, raise index error.
        If parks_list's items are not all strings, raise type error.
        '''
        if type(parks_list) != list:
            raise TypeError("Error happens in class Parks file, in __init__, parks_list must be a list.")
        if len(parks_list) != PARKS_LIST_LEN:
            raise IndexError("Error happens in class Parks file, in __init__, parks_list's length must be 3.")
            
        self.name = parks_list[0]
        self.neighbourhood = parks_list[1]
        self.washroom = parks_list[2]


    def __str__(self):
        '''
        Returns a string representation of Parks instances
        '''
        return f"{self.name} is in {self.neighbourhood} neighbourhood, it {self.washroom}."


    def __eq__(self, other_park):
        '''
        Compares current Parks object to another Parks object.
        If other_park does not belong to Parks class, raise type error.
        Returns True if their name are equal, and False otherwise
        '''
        if not isinstance(other_park, Parks):
            raise TypeError("Error happens in class Parks file, in __eq__, other_park should also belong to Parks class.")
        else:
            return self.name == other_park.name
            

