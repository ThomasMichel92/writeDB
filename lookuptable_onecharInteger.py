# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 12:42:42 2022

@author: thomas.michel
"""
'''
Created on 19.07.2021

@author: thomas.michel
'''
def lookuptable_onecharInteger(int_str):
    integer = int(int_str)
    if integer == 1:
        int_str = "01"
        return int_str
    elif integer == 2:
        int_str = "02"
        return int_str
    elif integer == 3:
        int_str = "03"
        return int_str
    elif integer == 4:
        int_str = "04"
        return int_str
    elif integer == 5:
        int_str = "05"
        return int_str
    elif integer == 6:
        int_str = "06"
        return int_str
    elif integer == 7:
        int_str = "07"
        return int_str
    elif integer == 8:
        int_str = "08"
        return int_str
    elif integer == 9:
        int_str = "09"
        return int_str
    elif integer == 0:
        int_str = "00"
        return int_str
    else:
        return int_str

if __name__ == "lookuptable_onecharInteger(int_str)":
    lookuptable_onecharInteger()
