#import numpy as np
import generic_module as gmod
import sys
sys.path.append('..')
import aoc_22_module as aoc22

def convert_2_num(element):
    if element=="A" or element=="X":
        num = 1 # rock
    elif element=="B" or element=="Y":
        num = 2 # paper
    elif element=="C" or element=="Z":
        num = 3 # scissors
    else:
        num = -1
    return num

def rps_give_status(p1, p2):
    if p1==p2:
        status = "D"
    else:
        if (p1==1 and p2==2) or (p1==2 and p2==3) or (p1==3 and p2==1):
            status = "W"
        else:
            status = "L"
    return status

def rps_give_shape(p1, status):
    if status=="D":
        p2 = p1
    else:
        if status=="W":
            p2 = p1+1
            if p2==4:
                p2=1
        else:
            p2 = p1-1
            if p2==0:
                p2=3
    return p2

def strategy_rules_1(p1,p2):
    s1 = p1
    s2 = p2
    status = rps_give_status(p1,p2)
    return status

def strategy_rules_2(p1,p2):
    if p2==1: #lose
        status = "L"
    elif p2==2: #draw
        status = "D"
    elif p2==3: #win
        status = "W"
    else: #unknown
        exit()
    p2 = rps_give_shape(p1, status)
    return p2, status

def scores(data):
    score = 0
    for element in data:
        p1 = convert_2_num(element[0])
        p2 = convert_2_num(element[2])
        status = strategy_rules_1(p1,p2)
        p2, status = strategy_rules_2(p1,p2)
        if status=="D":
            score += 3
        elif status=="W":
            score += 6
        elif status=="L":
            score += 0
        else:
            exit()
        score += p2
    return score

def main():
    directory = "./"
    filename = "input_data.txt"
    filepath = directory + filename
    rawdata = aoc22.read_input_file(filepath)
    data = aoc22.fancyup_data(rawdata)
    #print(data)
    score = scores(data)
    print(score)

if __name__=="__main__":
    main()
