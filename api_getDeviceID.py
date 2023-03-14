# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 12:37:55 2022

@author: thomas.michel
"""
'''
Created on 20.07.2021

@author: thomas.michel
'''
import requests
def api_getDeviceID(url,api_key,datemin,datemax,page):
    resp = requests.get (url + '/devices', headers = {'API-Key': api_key},
                            params = {'measurementDate[after]' : datemin,  # more parameters can be add, please see documentation
                                    'measurementDate[before]' : datemax,
                                    'itemsPerPage' : 5000,
                                    'page' : page})
    data_device = resp.json()['hydra:member']
    return data_device

if __name__ == "api_getDeviceID(url,api_key,datemin,datemax,page)":
    api_getDeviceID()

