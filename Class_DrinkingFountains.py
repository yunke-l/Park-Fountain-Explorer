'''
CS 5001 Fall 2022
Milestone 2
Yunke Li

This program create the DrinkingFountains class with many methods, incuding __str__ and __eq__.
'''
from CONSTANTS import *


class DrinkingFountains:
    '''
    Class: DrinkingFountains
    It knows how to create a DrinkingFountains object with a given list, print object's attributes,
    and compare different objects (for equality). 
    '''
    def __init__(self, fountains_list):
        '''
        Create instances of DrinkingFountains.
        Variables:
            fountains_list - list, the items of the list are: fountain's name, neighbourhood, location and open time.
        If fountains_list is not a list, raise type error.
        If fountains_list's length is not equal to 4, raise index error.
        If fountains's items are not all strings, raise type error.
        '''
        if type(fountains_list) != list:
            raise TypeError("Error happens in class DrinkingFountains file, in __init__, fountains_list must be a list.")
        if len(fountains_list) != FOUNTAINS_LIST_LEN:
            raise IndexError("Error happens in class DrinkingFountains file, in __init__, fountains_list's length must be 4.")

        self.name = fountains_list[0]
        self.neighbourhood = fountains_list[1]
        self.location = fountains_list[2]
        self.open_time = fountains_list[3]

    def __str__(self):
        '''
        Returns a string representation of DrinkingFountains instances
        '''
        return f"{self.name} public drinking fountain locates in {self.neighbourhood} neighbourhood. Its precise location is at {self.location}, and open time is {self.open_time}."


    def __eq__(self, other_fountain):
        '''
        Compares current DrinkingFountains object to another one.
        If other_fountain does not belong to DrinkingFountains class, raise type error.
        Returns True if their name are equal, and False otherwise
        '''
        if not isinstance(other_fountain, DrinkingFountains):
            raise TypeError("Error happens in class DrinkingFountains file, in __eq__, other_fountain should also belong to DrinkingFountains class.")
        else:
            return self.name == other_fountain.name
