'''
CS 5001 Fall 2022
Milestone 2
Yunke Li

This program is the driver file of the whole project.
'''


from Functions_MVC import *


def main():
    '''
    Function: main
        call the functions in Functions.py
        display analysis results in targeted format
        print error messages when error happens
    '''
    try:
        call_functions_and_display_analysis_results(PARKS_URL, FOUNTAINS_URL, HEADERS)
        
   
    #test if there is import error
    except ImportError as error_import:
        print("There is an error", type(error_import), error_import)    
    #test if the requests from web url is successfull
    except HTTPError as error_http:
        print("There is an error: ", type(error_http), error_http) 
    #test if name correct
    except NameError as error_name:
        print("There is an error: ", type(error_name), error_name)  
    #test if index exceeded the range 
    except IndexError as error_index:
        print("There is an error: ", type(error_index), error_index)
    #test if there is type errors
    except TypeError as error_type:
        print("There is an error: ", type(error_type), error_type)
    #test if value available
    except ValueError as error_value:
        print("There is an error: ", type(error_value), error_value)
    # test if keyboard is interrupted
    except KeyboardInterrupt as error_keyboard_interruption:
        print("There is an error: ", type(error_keyboard_interruption), error_keyboard_interruption)
        
if __name__ == "__main__":
    main()
