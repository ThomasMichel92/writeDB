# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 12:39:01 2022

@author: thomas.michel
"""
'''
Created on 16.07.2021

@author: thomas.michel
'''
import psycopg2
import sys
from psycopg2 import OperationalError, errorcodes, errors

def print_psycopg2_exception(err):
    
    err_type, err_obj, traceback = sys.exc_info()
    # get the line number when exception occured
    line_num = traceback.tb_lineno
    print ("\npsycopg2 ERROR:", err, "on line number:", line_num)
    print ("psycopg2 traceback:", traceback, "-- type:", err_type)

    # psycopg2 extensions.Diagnostics object attribute
    print ("\nextensions.Diagnostics:", err.diag)

    # print the pgcode and pgerror exceptions
    print ("pgerror:", err.pgerror)
    print ("pgcode:", err.pgcode, "\n")
    
def connection(password_s, server_deployment, information):
    
    try:
        if server_deployment == True:
            conn = psycopg2.connect(
            host="localhost",
            database="****",
            user="****",
            password=password_s)
        else:
            conn = psycopg2.connect(
            host="****",
            database="****",
            user="****",
            password=password_s)
    except OperationalError as err:
        if information == True:
            print_psycopg2_exception(err)
        conn = None
    
    return conn

if __name__ == "connection":
    connection()
    

