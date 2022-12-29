#import numpy as np
import generic_module as gmod
import sys
sys.path.append('..')
import aoc_22_module as aoc22
import string

def build_table_score():
    alphabet = [s for s in string.ascii_letters]
    table = dict()
    for letter in alphabet:
        key = letter
        value = alphabet.index(key)+1
        table[key] = value
    return table

class rucksack(object):
    def __init__(self, content, table):
        self.content = content
        self.split()
        self.item, self.score = search_duplicate(self.compartments, table)
    def split(self):
        n = len(self.content)
        self.compartments = [self.content[0:int(n/2)]]
        self.compartments.append(self.content[int(n/2):])
        #return compartments

def search_duplicate(strings, table):
    n=0
    score=0
    while score==0:
        item1 = strings[0][n]
        for item2 in strings[1]:
            if item1==item2:
                score=table[item1]
        n+=1
    return item1, score

def duplicate_item(data, table):
    total = 0
    for element in data:
        ruck = rucksack(element, table)
        total += ruck.score
    print(total)

def search_badge(content_list, table):
    #print(content_list)
    duplicate_list = ''
    for item1 in content_list[0]:
        for item2 in content_list[1]:
            if item1==item2:
                duplicate_list += item1
    #print(duplicate_list)
    strings = [duplicate_list, content_list[2]]
    item, score = search_duplicate(strings, table)
    return item, score

class elf_group(object):
    def __init__(self, contents, table):
        self.contents = contents
        rucksacks = []
        #print('-'*50)
        for c in self.contents:
            ruck = rucksack(c, table)
            rucksacks.append( ruck )
        self.badge, self.badge_score = search_badge(self.contents, table)
        #print(f"Common badge is {self.badge} => score is {self.badge_score}")

def security_badge(data, table):
    total = 0
    for n in range(0,len(data),3):
        group = elf_group(data[n:n+3], table)
        total += group.badge_score
    print(total)

def main():
    table = build_table_score()
    #print(table)
    directory = "./"
    data = aoc22.load_data(directory, "")
    #duplicate_item(data, table)
    security_badge(data, table)

if __name__=="__main__":
    main()
