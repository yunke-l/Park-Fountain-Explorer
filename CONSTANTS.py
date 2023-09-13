'''
CS 5001 Fall 2022
Milestone 2
Yunke Li

This program includes all constants used by the whole project.
'''
#CONSTANTS

#urls
PARKS_URL = "https://opendata.vancouver.ca/explore/dataset/parks/download/?format=csv&timezone=America/Los_Angeles&lang=en&use_labels_for_header=true&csv_separator=%3B"
FOUNTAINS_URL = "https://opendata.vancouver.ca/explore/dataset/drinking-fountains/download/?format=csv&timezone=America/Los_Angeles&lang=en&use_labels_for_header=true&csv_separator=%3B"
REFF_LBL_URL = 'https://opendata.vancouver.ca/pages/home/'

#header for dataframe
HEADERS = ['Neighbourhood', 'Number of Parks', 'Number of Drinking Fountains']

#Parks
PARKS_LIST_LEN = 3

#DrinkingFountains
FOUNTAINS_LIST_LEN = 4

#Neighbourhoods
NEIGHBOURHOODS_LIST_LEN = 5

#Functions_clean_data
SPLIT_CHAR_1 = '\n'
SPLIT_CHAR_2 = ';'
SPLIT_CHAR_3 = ':'
START_FROM_ROW = 1
END_BY_ROW_1 = 217
END_BY_ROW_2 = 509
PARK_NAME_COL = 1
PARK_NEIGHBOURHOOD_COL = 11
WASHROOM_COL = 6
HAS_WASHROOM = 'Y'
HAS_WASHROOM_MESSAGE = 'has washroom'
HAS_NOT_WASHROOM = 'N'
HAS_NOT_WASHROOM_MESSAGE = "doesn't have washroom"

REPLACE_CHAR_1 = '"'
REPLACE_CHAR_2 = ''
REPLACE_CHAR_3 = 'unknown'
REPLACE_CHAR_4 = 'none'
ROW_LIST_MAX = 3
FIRST_COL = 0
LAST_COL = -1
CLEAN_DFENG_INDEX = 5
CLEAN_DFPB_INDEX = 4
DFENG_STR = 'DFENG'
DFPB_STR = 'DFPB'
CLEAN_COLON_CONTENTS_CHAR = ':'
FOUNTAIN_NAME_COL = 0
FOUNTAIN_NEIGHBOURHOOD_COL = -1
FOUNTAIN_LOCATION_COL = 1
FOUNTAIN_OPENTIME_COL = 3

#Matplotlib
#make_bar_graph_from_data_frame
FIG_WIDTH = 10
FIG_HEIGHT = 7
PLOT_KIND = 'bar'
PLOT_LEGEND = True
YLABEL = 'Number'
YLABEL_FONTSIZE = 12
TITLE_FONTSIZE = 14

#text_to_image
FONT_DICT = {'family': 'serif',
             'color':  'black',
             'weight': 'bold',
             'size': 10}
TEXT_BOTTOM = 0
TEXT_LEFT = 0

#Tkinter
#init
ROW_CONFIG = 0
ROW_MINSIZE = 200
ROW_WEIGHT = 1
COLUMN_CONFIG = 1
COLUMN_MINSIZE = 300
COLUMN_WEIGHT = 1
INIT_TITLE = "Parks and Puclic Drinking Fountains"
INIT_LBL_ROW = 0
INIT_LBL_COL = 1
INIT_LBL_WRAPLENGTH = 400
INIT_LBL_JUSTIFY = 'left'
INIT_LBL_TXT = "Hi! Still don't know where to relax? \nChoose a neighbourhood below! \nSee where you can find parks and public drinking fountains."

#overview button
OVERVIEW_BTN_1_ROW = 2
OVERVIEW_BTN_1_COL = 0
OVERVIEW_BTN_1_TXT = 'Overview: Parks'
OVERVIEW_BTN_1_PADX = 10
OVERVIEW_BTN_1_PADY = 10
OVERVIEW_BTN_1_CURSOR = 'hand2'

OVERVIEW_BTN_2_ROW = 3
OVERVIEW_BTN_2_COL = 0
OVERVIEW_BTN_2_TXT = 'Overview: Drinking Fountains'
OVERVIEW_BTN_2_PADX = 10
OVERVIEW_BTN_2_PADY = 10
OVERVIEW_BTN_2_CURSOR = 'hand2'

#combobox
COMBOBOX_LBL_TXT = 'Select a Neighbourhood:'
COMBOBOX_LBL_FONT = 'Times New Roman'
COMBOBOX_LBL_FONTSIZE = 15
COMBOBOX_LBL_ROW = 1
COMBOBOX_LBL_COL = 1
COMBOBOX_LBL_PADX = 10
COMBOBOX_LBL_PADY = 0

COMBOBOX_CHOSEN_WIDTH = 15
COMBOBOX_CHOSEN_CURSOR = 'hand2'
COMBOBOX_CHOSEN_STATE = 'readonly'
COMBOBOX_CHOSEN_ROW = 2
COMBOBOX_CHOSEN_COL = 1
COMBOBOX_CHOSEN_BIND = '<<ComboboxSelected>>'

#exit button
EXIT_BTN_TXT = 'Exit'
EXIT_BTN_CURSOR = 'hand2'
EXIT_BTN_ROW = 3
EXIT_BTN_COL = 2
EXIT_BTN_PADX = 10
EXIT_BTN_PADY= 10


#txts
REFF_LBL_TXT = '* DATA SOURCE: Open Data Portal - City of Vancouver'
REFF_LBL_WRAPLENGTH = 300
REFF_LBL_CURSOR = 'hand2'
REFF_LBL_FONT = 'Times New Roman''Times New Roman'
REFF_LBL_FONTSIZE = 9
REFF_LBL_ROW = 3
REFF_LBL_COL = 1
REFF_LBL_PADX = 0
REFF_LBL_PADY = 5
REFF_LBL_BIND = '<Button-1>'

