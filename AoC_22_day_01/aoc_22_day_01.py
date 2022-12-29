#import numpy as np
import generic_module as gmod
import sys
sys.path.append('..')
import aoc_22_module as aoc22

class elf(object):
    def __init__(self, number, calories):
        self.elf_number = number
        self.calories = calories
        self.total = sum(calories)

def build_elf_list(list_of_calories):
    elf_list = []
    sublist = []
    n=0
    for calorie in list_of_calories:
        if calorie == '':
            n+=1
            new_elf = elf(n, sublist)
            elf_list.append(new_elf)
            sublist = []
        else:
            cal = int(calorie)
            sublist.append(cal)
    return elf_list

def count_most_carrier(elf_list, nb_of_carriers):
    totals = [e.total for e in elf_list]
    totals.sort()
    total = sum(totals[-nb_of_carriers:])
    print(total)

def main():
    directory = "./"
    filename = "input_data.txt"
    filepath = directory + filename
    rawdata = aoc22.read_input_file(filepath)
    data = aoc22.fancyup_data(rawdata)
    elf_list = build_elf_list(data)
    nb_of_carriers = 3
    count_most_carrier(elf_list, nb_of_carriers)



if __name__=="__main__":
    main()
