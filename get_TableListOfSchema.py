# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 12:41:04 2022

@author: thomas.michel
"""
'''
Created on 19.07.2021

@author: thomas.michel
'''
def get_TableListOfSchema(cursor,schema_name):
    cursor.execute("""
SELECT table_name
FROM information_schema.tables
WHERE table_name != 'pg_catalog'
AND table_schema = '"""+schema_name+"""'
AND table_name != 'information_schema'
AND table_type ='BASE TABLE'
ORDER BY table_name
""") 
    tuples = cursor.fetchall() 
    
    end = len(tuples)
    table_list = []
    for i in range(0, end):
        table_list.append(tuples[i][0])
    
    return table_list

if __name__ == "get_TableListOfSchema(cursor,schema_name)":
    get_TableListOfSchema()
