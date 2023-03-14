# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 12:43:37 2022

@author: thomas.michel
"""
'''
Created on 21.07.2021

@author: thomas.michel
'''
import os
import timeit

def write_Logfile(log_path,logfile_name,start,timestamp_log,schemaname,device,datasets,correct_datasets,log_status):
    if not os.path.exists(log_path):
        os.makedirs(log_path)
        
    folder_fileslist = [f for f in os.listdir(log_path) if os.path.isfile(os.path.join(log_path, f))]
    end = len(folder_fileslist)
    
    for i in range(0,end):
        if folder_fileslist[i] == logfile_name:
            logfile_active = True
            break
        else:
            logfile_active = False
    
    if folder_fileslist == []:
        logfile_active = False
    
    logfile = log_path +"\\"+logfile_name
    
    if logfile_active == False:
        if log_status == 'normal':
            file = open(logfile,'w+')
            stop = timeit.default_timer()
            file.write('\n'+'Timestamp:'+timestamp_log+',Status:Normal,Schema:'+schemaname+',Device_ID:'+device+',runtime:'+str(stop-start)+'s,Total_Datasets:'+str(datasets)+',Correct_Datasets:'+str(correct_datasets))
            file.close()
        elif log_status == 'error1':
            file = open(logfile,'w+')
            stop = timeit.default_timer()
            file.write('\n'+'Timestamp:'+timestamp_log+',Status:ERROR,Schema:'+schemaname+',Device_ID:'+device+',runtime:'+str(stop-start)+'s,Error_Message:wrong_DeviceID_in_Database')
            file.close()
    else:
        if log_status == 'normal':
            file = open(logfile,'a+')
            stop = timeit.default_timer()
            file.write('\n'+'Timestamp:'+timestamp_log+',Status:Normal,Schema:'+schemaname+',Device_ID:'+device+',runtime:'+str(stop-start)+'s,Total_Datasets:'+str(datasets)+',Correct_Datasets:'+str(correct_datasets))
            file.close()
        elif log_status == 'error1':
            file = open(logfile,'a+')
            stop = timeit.default_timer()
            file.write('\n'+'Timestamp:'+timestamp_log+',Status:ERROR,Schema:'+schemaname+',Device_ID:'+device+',runtime:'+str(stop-start)+'s,Error_Message:wrong_DeviceID_in_Database')
            file.close() 

if __name__ == "write_Logfile(log_path,logfile_name,start,timestamp_log,schemaname,device,datensaetze,empty_data_end,log_status)":
    write_Logfile()   
