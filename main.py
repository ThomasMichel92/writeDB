# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 12:36:22 2022

@author: thomas.michel
"""

'''
Created on 16.07.2021

@author: thomas.michel
'''
from datetime import datetime
import time
import timeit
import json
import os

from connect import connection
from get_SchemaList import get_SchemaList
from get_TableListOfSchema import get_TableListOfSchema
from get_timestamp import get_timestamp
from get_FromUpdate import get_FromUpdate
from insert_inTwoColumnTable import insert_inTwoColumnTable
from get_FromDevice import get_FromDevice
from set_TableOwner import set_TableOwner
from api_getMeter import api_getMeter
from api_getData import api_getData
from api_getDeviceID import api_getDeviceID
from write_Logfile import write_Logfile
from calculate_date import calculate_date

########################CONFIG########################
#Toggle Debug Mode

debug_mode = True
#debug_mode = False

short_overview = True
#short_overview = False

#information = True
information = False

commit_mode = True
#commit_mode = False

#server_deployment = True
server_deployment = False

print_mode = True
#print_mode = False 

    
#######################################################

########################VARAIBLEN#######################
#Database Password HAS to Be EDITED
password = '*****'

log_path = r'C:\echtnetz\log'
logfile_name = '****_writeDatabase.log'

data_path = r'C:\****\data'

debug_QGIS_path = r'C:\Program Files\QGIS 3.16.8\bin'           #per Hand aendern bei upload
QGIS_path = r'C:\qgisserver\bin'

table_upload = 'upload'
col1_upload = 'id'
col2_upload = 'lastdate'

table_device = 'device'
col1_device = 'id'
col2_device = 'deviceid'

#debug_datemin = '2021-06-02T11:08'
#debug_datemax = '2021-06-09T17:31'

debug_datemin = '2023-02-26T00:00' #yyyy-mm-dd
debug_datemax = '2023-03-28T00:00' #14:50
debug_timestamp = '2022-03-10 00:00:00'

#debug_schema = 'debug_schema'


role_name = '****_role'
table_messfahrt_name = 'messungen'

#HAS to Be EDITED
api_key="******"
url = '******'
page = 1

json_filename = 'json_file.json'
geojson_filename = 'geojson_file.geojson'
#########################################################

#######################PROGRAMMSTART#######################
if print_mode == True:
        print ('Connect Database')
conn=connection(password, server_deployment, information)

counter_db_connection = 1
while conn is None:
    conn=connection(password, server_deployment, information)
    counter_db_connection = counter_db_connection + 1 
    time.sleep(2.5)
    
if conn is None:
    print("No valid Connection")
else:
    print("DB Connection established after " + str(counter_db_connection) + " attempts.")
    
cursor = conn.cursor()

user = conn.info.dsn_parameters['user']
database = conn.info.dsn_parameters['dbname']
host = conn.info.dsn_parameters['host']

#Get all Schemas
if print_mode == True:
        print ('Get Schemas')
schema_list = get_SchemaList(cursor, debug_mode,debug_schema)
end = len(schema_list) 
valid_schema_list = []
for i in range(0,end):
    if schema_list[i][0:9]=='echtnetz_':
        valid_schema_list.append(schema_list[i])

if print_mode == True:
        print ('Check Schemas')
#Check der Schemas ob Inhalte korrekt sind
end = len(valid_schema_list)
verified_schema_list = []

for i in range(0,end):
    table_list = get_TableListOfSchema(cursor, valid_schema_list[i])
    end_table_list = len(table_list)
    for j in range(0, end_table_list):
        if table_device == table_list[j] or table_upload == table_list[j]:
            verified_schema_list.append(valid_schema_list[i])
            break
            
end = len(verified_schema_list)
if print_mode == True:
    print('START')
#Loop over all schemas with the correct presettings
for i in range(0,end):
    if print_mode == True:
        print ('Start Loop')
    ################## DATA LOGFILE ########################
    #########################################################
    start = timeit.default_timer()

    now_log = datetime.now()
    timestamp_log = get_timestamp(now_log)     
         
    ################## Get Timestamp ########################
    #########################################################
    schemaname = verified_schema_list[i]
    if print_mode == True:
        print ('Schema: ' +schemaname)

    #Date Berechnungen
    id_list,date_list = get_FromUpdate(cursor,schemaname, table_upload)
    #write actual date
    datemin,datemax,timestamp = calculate_date(id_list,date_list)
    lastentry = len(id_list)
   
    if print_mode == True:
        if debug_mode == True:
            print('DEBUG MODE ENABLED')
            print('timestamp: '+debug_timestamp)
            print('datemin: '+debug_datemin)
            print('datemax: '+debug_datemax)
        else:
            print('NORMAL MODE ENABLED')
            print('timestamp: '+timestamp)
            print('datemin: '+datemin)
            print('datemax: '+datemax)
            
    #### WRITE UPLOAD TABLE
    if commit_mode == True:
        if debug_mode == True:
            insert_inTwoColumnTable(cursor,conn,schemaname,table_upload,col1_upload,col2_upload,lastentry + 1,debug_timestamp)
        else:
            insert_inTwoColumnTable(cursor,conn,schemaname,table_upload,col1_upload,col2_upload,lastentry + 1,timestamp)
    
    ################## Get DeviceID ########################
    ########################################################
    id_list,device_list = get_FromDevice(cursor,schemaname, table_device)
    lastentry = len(id_list)
    
    for d_ids in range(0,len(device_list)): 
        device_id = device_list[d_ids]
        if print_mode == True:
            print('devicenr: '+str(d_ids)+ ' with id: '+device_id)
    
    ################## API Abfrage ########################
    #######################################################
        if print_mode == True:
            print ('Downloading data via API')
        
    #### GET METER
        if debug_mode == True:
            data_meter = api_getMeter(url, api_key, debug_datemin, debug_datemax, page)
        else:
            data_meter = api_getMeter(url, api_key, datemin, datemax, page)
            
        json_dump_meter = json.dumps(data_meter)
        json_object_meter = json.loads(json_dump_meter)
        end_json_meter = len(json_object_meter)
    
        fakeID_meter = []
        realID_meter = []
        for i in range(0,end_json_meter):
            fakeID_meter.append(json_object_meter[i]['@id'])
            realID_meter.append(json_object_meter[i]['meterId'])
        
    #### GET DEVICE
        if debug_mode == True:
            data_device = api_getDeviceID(url, api_key, debug_datemin, debug_datemax, page)
        else:
            data_device = api_getDeviceID(url, api_key, datemin, datemax, page)
        
        json_dump_device = json.dumps(data_device)
        json_object_device = json.loads(json_dump_device)
        end_json_device = len(json_object_device)
        
        
        for i in range(0,end_json_device):
            if json_object_device[i]['deviceId'] == device_id: 
                search_device_id = json_object_device[i]['id']
                break
            else:
                search_device_id = 0
                
        if search_device_id == 0:
            if print_mode == True:
                print('ERROR: WRONG DEVICE ID IN DATABASE')
            #### LOG ERROR
            log_status = 'error1'
            datasets = 0
            correct_datasets = 0
            
            write_Logfile(log_path, logfile_name, start, timestamp_log, schemaname,device_id, datasets, correct_datasets, log_status)
                
    #### GET DATA
        if debug_mode == True:
            data_messung = api_getData(url, api_key, debug_datemin, debug_datemax, search_device_id, page)
            print("Data Debug Mode")
        else:
            data_messung = api_getData(url, api_key, datemin, datemax, search_device_id, page)
            print("Data Normal Mode")

        json_dump = json.dumps(data_messung)
        json_object = json.loads(json_dump)
        
        if print_mode == True:
            print ('Create Json File')
    #### OPEN JSON FILE
        if not os.path.exists(data_path):
            os.makedirs(data_path)
        
        json_file = data_path +"\\"+json_filename
        file = open(json_file,'w')
        
    #### MODIFY DATA TO ACCEPTABLE JSON DATA
    #DELETE UNUSED ARGUMENTS
        unused_arguments = ['@id','@type','client','operator','frequencyDownlink','frequencyUplink','frequency','channel','bsic','rxLevel','rxQuality','ta','psc','rscp','ecn0','drx','ura','pci','tac','ecio','rac','eutra','txPower','networkError','softwareVersion','deviceStatus','networkBtsLocationLat','networkBtsLocationLong']
        
        datasets = len(json_object)
        
    ##### DELETE EMPTY DATA
        json_object2 = []
        for i in range(0,len(json_object)):
            if ( ( (json_object[i]['latitude'] is not None) and (json_object[i]['longitude'] is not None) ) and ( (json_object[i]['latitude'] != 0) and (json_object[i]['longitude'] != 0) ) ):
                json_object2.append(json_object[i])
        
        del json_object
        json_object = json_object2
        del json_object2
        correct_datasets = len(json_object)
        
    ##### MODIFY DATA
        measurementDate = []
        for i in range(0,len(json_object)):
            #### Reload measurementDate
            pos_T = json_object[i]['measurementDate'].find('T')
            pos_point = json_object[i]['measurementDate'].find('.')
            json_object[i]['measurementDate'] = json_object[i]['measurementDate'][0:pos_T] +' '+json_object[i]['measurementDate'][pos_T+1:pos_point]
            string = json_object[i]['measurementDate'][0:pos_T] +' '+json_object[i]['measurementDate'][pos_T+1:pos_point]
            string2 = string[0:string.find(' ')]
            if len(measurementDate) > 0:
                if string2 != measurementDate[len(measurementDate)-1]:
                    measurementDate.append(string2)
            else:
                measurementDate.append(string2)
            
            #if print_mode == True:
            #    print ('Messung am: '+ measurementDate[len(measurementDate)-1])
            
            #### Reload deviceID and meterID
            for t in range(0,len(realID_meter)):
                if json_object[i]['meter'] == fakeID_meter[t]:
                    json_object[i]['meter'] = realID_meter[t]
            json_object[i]['device'] = device_id
            #### del unused arguments
            for j in range(0,len(unused_arguments)):
                if unused_arguments[j] in json_object[i]:
                    del json_object[i][unused_arguments[j]]
        
    

    #### Reload deviceID and meterID
        json_dump = json.dumps(json_object) #returns string
    ##### REPLACE ARGUMENT KEY NAMES
        old_key_names = ['device','station','meter','latitude','longitude']
        new_key_names = ['deviceId','stationId','meterId','lat','lng']
        
        key_names_end = len(old_key_names)
        for i in range(0,key_names_end):
            json_dump = json_dump.replace(old_key_names[i],new_key_names[i])
        
    #### SAVE JSON DATA    
        file.write(json_dump)
        file.close()
        
        json_object = json.loads(json_dump)
        
    #### WRITE GEOJSON
        if print_mode == True:
            print ('Create Geojson File')
        geojson = {
            "type": "FeatureCollection",
            "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [d["lng"], d["lat"]],
                    },
                "properties": d,
             } for d in json_object]
        }
    
    #### SAVE GEOJSON DATA
        geojson_file = data_path +"\\"+geojson_filename
        output = open(geojson_file, 'w')
        json.dump(geojson, output)
        output.close()
        
    
    #### WRITE DATABASE
        if print_mode == True:
            print ('Write to Database')
        
        command = 'ogr2ogr -progress -f "PostgreSQL" PG:"host='+host+' user='+user+' dbname='+database+' password='+password+'" "'+geojson_file+'" -nln ' +schemaname+'.'+table_messfahrt_name
        
        if server_deployment == True:
            os.chdir(QGIS_path)
        else:
            os.chdir(debug_QGIS_path)

    #### UPLOAD DATABASE
        if print_mode == True:
            print ('Upload Database')
        
        if commit_mode == True:
            if search_device_id != 0 and json_object != []:
                os.system(command)
                print('Data has been comitted')
    
                
        check_table_list = get_TableListOfSchema(cursor, schemaname)
        end_check_table_list = len(check_table_list)            
    #### Get INFO if Table exist already
        for i in range(0, end_check_table_list):
            if table_messfahrt_name == check_table_list[i]:
                table_messfahrt_name_exist = True
                break
            else:
                table_messfahrt_name_exist = False
            
    #### ALTER DATABASE ROLE
        if table_messfahrt_name_exist == True:
            set_TableOwner(cursor, conn, schemaname, table_messfahrt_name, role_name)
        
    #### WRITE LOGFILE
        if print_mode == True:
            print ('Write Logfile')
        log_status = 'normal'
        if short_overview == True:
            if len(measurementDate) == 0:
                print('Schema: ' + schemaname + ', Device: ' + device_id + ', Datasets: ' + str(datasets) + ', CorrectData: ' + str(correct_datasets)+ ' Messtage: 0')
            else:
                print('Schema: ' + schemaname + ', Device: ' + device_id + ', Datasets: ' + str(datasets) + ', CorrectData: ' + str(correct_datasets)+ ', letzteMessung am: ' + measurementDate[0] + ', Messtage: ' + str(len(measurementDate)))
        write_Logfile(log_path, logfile_name, start, timestamp_log, schemaname,device_id, datasets, correct_datasets, log_status)

cursor.close()
conn.close()    
    
if print_mode == True:
    print("Vorgang Erfolgreich")
    # input("press ENTER to quit")
    # sys.exit("FINISHED")
        

############################################################
