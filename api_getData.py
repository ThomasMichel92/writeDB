# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 12:37:08 2022

@author: thomas.michel
"""
'''
Created on 19.07.2021

@author: thomas.michel
'''
import requests
def api_getData(url,api_key,datemin,datemax,device_id,page):
    data_messung= []
    while 1:
        resp = requests.get (url + '/measurements', headers = {'API-Key': api_key},
                                         params = {'measurementDate[after]' : datemin,  # more parameters can be add, please see documentation
                                                   'measurementDate[before]' : datemax,
                                                   'device' : device_id,
                                                   'itemsPerPage' : 5000,
                                                   'page' : page})
        
        data_messung += resp.json()['hydra:member']
        page += 1
        
        if (resp.status_code!=200) or (resp.json()['hydra:member'] == []):
                break
    return data_messung    

if __name__ == "api_getData(url,api_key,datemin,datemax,device_id,page)":
    api_getData()
