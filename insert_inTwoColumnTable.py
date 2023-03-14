# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 12:42:04 2022

@author: thomas.michel
"""
'''
Created on 19.07.2021

@author: thomas.michel
'''
import psycopg2
def insert_inTwoColumnTable(cursor,conn,schema,table,col1,col2,val1,val2):
    """ insert a valuesr into the a variable table """
    sql = """
    INSERT INTO """+schema+"""."""+table+"""("""+col1+""","""+col2+""")
    VALUES(%s,%s) 
    """
    try:
        cursor.execute(sql, (val1,val2))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return None

if __name__ == "insert_inTwoColumnTable(cursor,conn,schema,table,col1,col2,val1,val2)":
    insert_inTwoColumnTable()
