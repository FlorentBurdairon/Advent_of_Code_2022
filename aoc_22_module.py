#import numpy as np
import generic_module as gmod

def read_input_file(filepath):
    with open(filepath) as myfile:
        read_data = myfile.readlines()
    return read_data

def strip_newline(data):
    return data.replace('\n', '')

def fancyup_data(rawdata):
    fancy_data = []
    for element in rawdata:
        fancy_element = strip_newline(element)
        fancy_data.append(fancy_element)
    return fancy_data

def load_data(directory, status):
    #directory = "./"
    if status=="dev":
        filename = "input_data_test.txt"
    else:
        filename = "input_data.txt"
    filepath = directory + filename
    rawdata = read_input_file(filepath)
    data = fancyup_data(rawdata)
    return data
