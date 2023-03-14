# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 12:43:13 2022

@author: thomas.michel
"""
'''
Created on 19.07.2021

@author: thomas.michel
'''
def set_TableOwner(cursor,conn,schema,table,role_name):
    cursor.execute("""
    ALTER TABLE """+schema+"""."""+table+"""
    OWNER TO """+role_name+""";
    """)
    conn.commit()

if __name__ == "set_TableOwner(cursor,conn,schema,table,role_name)":
    set_TableOwner()
