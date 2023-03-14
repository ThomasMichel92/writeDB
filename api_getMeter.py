# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 12:38:31 2022

@author: thomas.michel
"""
'''
Created on 19.07.2021

@author: thomas.michel
'''
import requests
def api_getMeter(url,api_key,datemin,datemax,page):
    resp = requests.get (url + '/meters', headers = {'API-Key': api_key},
                                params = {'measurementDate[after]' : datemin,  # more parameters can be add, please see documentation
                                        'measurementDate[before]' : datemax,
                                        'itemsPerPage' : 5000,
                                        'page' : page})
    data_meter = resp.json()['hydra:member']
    return data_meter

if __name__ == "api_getMeter(url,api_key,datemin,datemax,page)":
    api_getMeter()
