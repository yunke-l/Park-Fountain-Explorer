'''
CS 5001 Fall 2022
Milestone 2 
Yunke Li

This program includes all the functions for reading a csv file from an url, and  data cleaning.
'''

import requests
from requests.exceptions import HTTPError
from CONSTANTS import *

def read_url(url):
    '''
    Function -- read_url
        get the response of a url link of a csv file, read its values and store it as a long string: url_data
    Parameter: url - str
    Return url_data, a long string that stores values for data analysis further.
    If url is not a string, raise type error.
    Raise HttpError if the requests from web url is unsuccessful.
    '''
    if type(url) != str:
        raise TypeError("Error happens in read_url(), parameter is not a string.")

    resp = requests.get(url)
    
    if resp.raise_for_status() == HTTPError:
        raise HTTPError
    else:
        url_data = resp.text

    return url_data


def clean_parks_data(url_data):
    '''
    Function -- clean_parks_data
        clean the csv data of parks.
    Parameter: url_data - str
    Return parks_data, a nested list of data we need, each inner list represents a park's attribute: name, neighbourhood and washroom status.
    If url_data is not a string, raise type error.
    '''
    if type(url_data) != str:
        raise TypeError("Error happens in clean_parks_data(), parameter is not a string.")
    
    parks_data = []

    rows = url_data.split(SPLIT_CHAR_1) # split each row by new line character
    
    for row in rows[START_FROM_ROW:END_BY_ROW_1]: # get rid of the first row, because its items are headers. The table has 217 valid rows
        
        row_list = row.split(SPLIT_CHAR_2) # split each row's items by semicolon

        # replace the value of washroom status to what we want
        if row_list[WASHROOM_COL] == HAS_WASHROOM:
            row_list[WASHROOM_COL] = HAS_WASHROOM_MESSAGE
        elif row_list[WASHROOM_COL] == HAS_NOT_WASHROOM:
            row_list[WASHROOM_COL] = HAS_NOT_WASHROOM_MESSAGE

        # form the nested list
        park = [row_list[PARK_NAME_COL], row_list[PARK_NEIGHBOURHOOD_COL], row_list[WASHROOM_COL]] 
        parks_data.append(park)

    return parks_data



def clean_fountains_data(url_data):
    '''
    Function -- clean_fountains_data
        clean the csv data of fountains.
    Parameter: url_data - str
    Return fountains_data, a nested list of data we need, each inner list represents a fountain's attribute: name, neighbourhood, location and open time.
    If url_data is not a string, raise type error.
    If inner list of fountains_data is empty, raise value error.
    '''
    if type(url_data) != str:
        raise TypeError("Error happens in clean_fountains_data, parameter is not a string.")

    fountains_data = []
    
    url_data = url_data.replace(REPLACE_CHAR_1, REPLACE_CHAR_2) # remove double quote characters
    
    rows = url_data.split(SPLIT_CHAR_1) # split each row by new line character
    
    for row in rows[START_FROM_ROW:END_BY_ROW_2]: # get rid of the first row, because its items are headers. The table has 509 valid rows  
        row_list = row.split(SPLIT_CHAR_2) # split each row's items by semicolon
        # get rid of rows whose length is less than 3
        if len(row_list) >= ROW_LIST_MAX: 
            for i in range(len(row_list)):

                # replace empty unit with 'unknown'
                if row_list[i] == REPLACE_CHAR_2:
                    row_list[i] = REPLACE_CHAR_3
                
            # get rid of the first item of each row if the item begins with 'DFENG' or 'DFPB' because they are useless
            if row_list[FIRST_COL][:CLEAN_DFENG_INDEX] == DFENG_STR or row_list[FIRST_COL][:CLEAN_DFPB_INDEX] == DFPB_STR:
                row_list = row_list[START_FROM_ROW::]
            
            # if the first item of each row contains a colon character, only keep the contents after colon
            if SPLIT_CHAR_3 in row_list[FIRST_COL]:
                row_list[FIRST_COL] = row_list[FIRST_COL].split(SPLIT_CHAR_3)[START_FROM_ROW]

            # if the last item of each row is not a valid neibourhood name, replace it with 'none'
            # else, delete the last character of the item string because its a '\r' character
            if len(row_list[LAST_COL]) > 1:
                row_list[LAST_COL] = row_list[LAST_COL][:LAST_COL]
            else:
                row_list[LAST_COL] = REPLACE_CHAR_4

            # form the nested list
            fountain = [row_list[FOUNTAIN_NAME_COL], row_list[FOUNTAIN_NEIGHBOURHOOD_COL], row_list[FOUNTAIN_LOCATION_COL], row_list[FOUNTAIN_OPENTIME_COL]]
            fountains_data.append(fountain)
            
    return fountains_data



