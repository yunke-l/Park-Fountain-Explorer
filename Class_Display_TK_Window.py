'''
CS 5001 Fall 2022
Milestone 2
Yunke Li

This program create the Display_TK_Window class with many methods.
'''

import tkinter as tk
from tkinter import ttk
from Functions_display_data_by_Matplotlib import *
from CONSTANTS import *
import webbrowser

class Display_TK_Window:
    '''
    Class: Display_TK_Window
    It knows how to create a Display_TK_Window object and implement relevant methods. 
    '''
    def __init__(self, master, data_frame, xticklabels, neighbourhoods_str_dict):
        self.master = master
        self.data_frame = data_frame
        self.xticklabels = xticklabels
        self.neighbourhoods_str_dict = neighbourhoods_str_dict
        self.title = INIT_TITLE

        # greeting label
        self.label = ttk.Label(master, text = INIT_LBL_TXT, wraplengt = INIT_LBL_WRAPLENGTH, justify = INIT_LBL_JUSTIFY)
        self.label.grid(row = INIT_LBL_ROW, column = INIT_LBL_COL)

        # overview button 1, show dataframe plot (sort by number of parks)
        self.overview_btn_1 = ttk.Button(master, text = OVERVIEW_BTN_1_TXT, cursor = OVERVIEW_BTN_1_CURSOR, command = self.overview_sort_by_parks)
        self.overview_btn_1.grid(row = OVERVIEW_BTN_1_ROW, column = OVERVIEW_BTN_1_COL, padx = OVERVIEW_BTN_1_PADX, pady = OVERVIEW_BTN_1_PADY)

        # overview button 2, show dataframe plot (sort by number of drinking fountains)
        self.overview_btn_2 = ttk.Button(master, text = OVERVIEW_BTN_2_TXT, cursor = OVERVIEW_BTN_2_CURSOR, command = self.overview_sort_by_fountains)
        self.overview_btn_2.grid(row = OVERVIEW_BTN_2_ROW, column = OVERVIEW_BTN_2_COL, padx = OVERVIEW_BTN_2_PADX, pady = OVERVIEW_BTN_2_PADY)

        # neighbourhood combobox
        self.combobox_lbl = ttk.Label(master, text = COMBOBOX_LBL_TXT, font = (COMBOBOX_LBL_FONT, COMBOBOX_LBL_FONTSIZE))
        self.combobox_lbl.grid(row = COMBOBOX_LBL_ROW, column = COMBOBOX_LBL_COL, padx = COMBOBOX_LBL_PADX, pady = COMBOBOX_LBL_PADY)
  
        self.selected_neighbourhood = tk.StringVar() # create a StringVar object to manage value of 
        self.combobox_chosen = ttk.Combobox(master, width = COMBOBOX_CHOSEN_WIDTH, textvariable = self.selected_neighbourhood, cursor = COMBOBOX_CHOSEN_CURSOR)
        self.combobox_chosen['value'] = self.xticklabels
        self.combobox_chosen['state'] = COMBOBOX_CHOSEN_STATE
        self.combobox_chosen.grid(row = COMBOBOX_CHOSEN_ROW, column = COMBOBOX_CHOSEN_COL)
        self.combobox_chosen.bind(COMBOBOX_CHOSEN_BIND, self.show_chosen_neighbourhood_info)

        # exit button
        self.exit_btn = ttk.Button(master, text = EXIT_BTN_TXT, cursor = EXIT_BTN_CURSOR, command = self.master.destroy)
        self.exit_btn.grid(row = EXIT_BTN_ROW, column = EXIT_BTN_COL, padx = EXIT_BTN_PADX, pady = EXIT_BTN_PADY)

        # referrence label
        self.reff_lbl = ttk.Label(master, text = REFF_LBL_TXT, wraplengt = REFF_LBL_WRAPLENGTH, cursor = REFF_LBL_CURSOR, font = (REFF_LBL_FONT, REFF_LBL_FONTSIZE))
        self.reff_lbl.grid(row = REFF_LBL_ROW, column = REFF_LBL_COL, padx = REFF_LBL_PADX, pady = REFF_LBL_PADY)
        self.reff_lbl.bind(REFF_LBL_BIND, lambda e: self.open_reff_url(REFF_LBL_URL))

        
    def overview_sort_by_parks(self):
        '''
        Draw a bar graph from data frame, sort the dataframe by number of parks.
        '''
        data_frame_sort_by_parks = self.data_frame.sort_values('Number of Parks')
        x_labels = data_frame_sort_by_parks.iloc[:, 0]
        return make_bar_graph_from_data_frame(data_frame_sort_by_parks, x_labels, self.title)


    def overview_sort_by_fountains(self):
        '''
        Draw a bar graph from data frame, sort the dataframe by number of fountains.
        '''
        data_frame_sort_by_fountains = self.data_frame.sort_values('Number of Drinking Fountains')
        x_labels = data_frame_sort_by_fountains.iloc[:, 0]
        return make_bar_graph_from_data_frame(data_frame_sort_by_fountains, x_labels, self.title)


    def open_reff_url(self, url):
        '''
        Open a given url
        '''
        webbrowser.open_new(url)


    def show_chosen_neighbourhood_info(self, event):
        '''
        Draw a text graph base on the combobox selection
        '''
        return text_to_image(self.neighbourhoods_str_dict[self.selected_neighbourhood.get()])
