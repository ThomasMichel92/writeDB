# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 12:41:30 2022

@author: thomas.michel
"""
'''
Created on 19.07.2021

@author: thomas.michel
'''
def get_timestamp(date):
    string_now = date.__str__()
    pointpos = string_now.find(".")
    timestamp = string_now[0:pointpos]
    return timestamp

if __name__ == "get_timestamp(date)":
    get_timestamp()
