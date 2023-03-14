# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 08:03:40 2022

@author: thomas.michel
"""
from datetime import datetime, timedelta
from lookuptable_onecharInteger import lookuptable_onecharInteger

def calculate_date(id_list,date_list):
    lastentry = len(id_list)
    old_date = date_list[lastentry-1]
    today = datetime.now()
    
    #Calculate DateMin
    year_old = str(old_date.year)
    
    month_old = str(old_date.month)
    month_old = lookuptable_onecharInteger(month_old)
    
    day_old = str(old_date.day)
    day_old = lookuptable_onecharInteger(day_old)
    
    hour_old = str(old_date.hour)
    hour_old = lookuptable_onecharInteger(hour_old)
    
    minute_old = str(old_date.minute)
    minute_old = lookuptable_onecharInteger(minute_old)
    
    datemin = year_old+'-'+month_old+'-'+day_old+'T'+hour_old+':'+minute_old
    
    #Calculate DateMax,Timestamp
    year_today = str(today.year)
    
    month_today = str(today.month)
    month_today = lookuptable_onecharInteger(month_today)
    
    day_today =  str(today.day)
    day_today = lookuptable_onecharInteger(day_today)
    
    hour_today = '00'
    minute_today = '00'
    second_today = '00'    
    
    datemax = year_today+'-'+month_today+'-'+day_today+'T'+hour_today+':'+minute_today
    
    timestamp = year_today+'-'+month_today+'-'+day_today+' '+hour_today+':'+minute_today+':'+second_today
    
    return datemin,datemax,timestamp
    
    


if __name__ == "calculate_date(id_list,date_list)":
    calculate_date()