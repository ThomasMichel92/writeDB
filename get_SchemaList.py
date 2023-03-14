# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 12:40:31 2022

@author: thomas.michel
"""
'''
Created on 19.07.2021

@author: thomas.michel
'''
def get_SchemaList(cursor, debug_mode,debug_schema):
    if debug_mode == True:
        schema_list = []
        schema_list.append(debug_schema)
    else:
        cursor.execute("""
    SELECT schema_name
    FROM information_schema.schemata
    WHERE schema_name != 'pg_catalog'
    AND schema_name != 'information_schema'
    AND schema_name != 'pg_toast'
    AND schema_name != 'pg_temp_1'
    AND schema_name != 'pg_toast_temp_1'
    AND schema_name != 'public'
    ORDER BY schema_name
    """) 
        tuples = cursor.fetchall() 
        
        end = len(tuples)
        schema_list = []
        for i in range(0, end):
            schema_list.append(tuples[i][0])
    
    return schema_list

if __name__ == "get_SchemaList(cursor, debug_mode,debug_schema)":
    get_SchemaList()
