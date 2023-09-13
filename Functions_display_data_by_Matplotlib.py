'''
CS 5001 Fall 2022
Milestone 2
Yunke Li

This program includes all the functions for data displaying by matplotlib.
'''

import pandas as pd
import matplotlib.pyplot as plt
from CONSTANTS import *


def make_bar_graph_from_data_frame(df1, xticklabels, title):
    '''
    Function -- make_bar_graph_from_data_frame
        create a graph of neighbourhood data frame.
    Parameter:
        df1 -- pandas DataFrame
        xticklabels -- a list of neighbourhood names
        title -- a string of graph title
    Return nothing, but create a graph of neighbourhood data frame.
    '''
    # create a Figure with an Axes
    figure1, ax1 = plt.subplots(figsize = (FIG_WIDTH, FIG_HEIGHT))

    # plot bar chart with legend
    df1.plot(kind = PLOT_KIND, legend = PLOT_LEGEND, ax = ax1)

    # decorate the bar chart
    ax1.set_ylabel(YLABEL, fontsize = YLABEL_FONTSIZE)
    ax1.set_xticklabels(xticklabels)
    ax1.set_title(title, fontsize = TITLE_FONTSIZE)

    # align plot elements
    figure1.autofmt_xdate()
    
    plt.show()


def text_to_image(txt):
    '''
    Function -- text_to_image
        create a graph of the given text string.
    Parameter:
        txt -- a string
    Return nothing, but create a graph of the given text string.
    '''
    # create an empty Figure
    fig = plt.figure(figsize = (FIG_WIDTH, FIG_HEIGHT))

    # plot text on it
    fig.text(TEXT_LEFT, TEXT_BOTTOM, txt, fontdict = FONT_DICT)
    
    plt.show()







