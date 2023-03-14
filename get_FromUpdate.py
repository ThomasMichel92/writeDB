# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 12:39:55 2022

@author: thomas.michel
"""
'''
Created on 19.07.2021

@author: thomas.michel
'''
def get_FromUpdate(cursor,schema,table):
    sql = """
    SELECT id, lastdate FROM """+schema+"""."""+table+"""
    """
    cursor.execute(sql)
    tuples = cursor.fetchall()
    
    end = len(tuples)
    id_list = []
    for i in range(0, end):
        id_list.append(tuples[i][0])
    
    date_list = []
    for i in range(0, end):
        date_list.append(tuples[i][1])
    return id_list,date_list

if __name__ == "get_FromUpdate(cursor,schema,table)":
    get_FromUpdate()

