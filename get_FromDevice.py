# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 12:39:27 2022

@author: thomas.michel
"""
'''
Created on 19.07.2021

@author: thomas.michel
'''
def get_FromDevice(cursor,schema,table):
    sql = """
    SELECT id, deviceid FROM """+schema+"""."""+table+"""
    """
    cursor.execute(sql)
    tuples = cursor.fetchall()
    
    end = len(tuples)
    id_list = []
    for i in range(0, end):
        id_list.append(tuples[i][0])
    
    device_list = []
    for i in range(0, end):
        device_list.append(tuples[i][1])
    return id_list,device_list

if __name__ == "get_FromDevice(cursor,schema,table)":
    get_FromDevice()
