
import numpy as np
import pandas as pd
import json as js
import os
import urllib.request

def change_cases_value(current_value):  #Data Cleaning Function 1 - to be called later
    
    if 'Yes' in current_value:
        if len(current_value.split(' ')[1]) == 4:
               val= current_value.split(' ')[1][1:3]
        else:
            val = current_value.split(' ')[1][1:2]
    elif 'No' in current_value: 
        val = '0'

    return val

def change_assets_value(curr_val): #Data cleaning function 2 - to be called later
    curr_val=str(curr_val)
    if 'Lac' in curr_val: 
        val1 = float(curr_val[:-3])*(10**5)
    elif 'Crore' in curr_val: 
        val1 = float(curr_val[:-5])*(10**7)
    else: 
        val1 = float(curr_val)
    
    return val1

def extract_and_process(csv_name, url, url_api_key): 
    constituency_list = pd.read_csv(csv_name) 
    
    yes2 = [] 

    for const in constituency_list["Constituency"]:
        if len(const.split(' '))!=1: 
            if len(const.split(' '))>3: 
                   temp_str = const.split(' ')[0]+'%20'+const.split(' ')[1]+'%20'+const.split(' ')[2]+'%20'+const.split(' ')[3]
            elif len(const.split(' '))>2: 
                   temp_str = const.split(' ')[0]+'%20'+const.split(' ')[1]+'%20'+const.split(' ')[2]
            else:
                temp_str = const.split(' ')[0]+'%20'+const.split(' ')[1]
        else:
            temp_str = const
            
        new1 = url+temp_str+url_api_key
        with urllib.request.urlopen(new1) as new_work:
            data1= js.loads(new_work.read())
        
        yes2+=data1
        
    wb_phase = pd.DataFrame.from_dict(yes2)
    
    temp_list3 = wb_phase.cases.apply(change_cases_value)
    temp_list3 = temp_list3.astype(int)
    
    wb_phase.cases = temp_list3 
    
    #Changing Age ad IPC Count columns to integers from strings
    wb_phase.age = wb_phase.age.astype(int)
    wb_phase.serious_ipc_counts = wb_phase.serious_ipc_counts.astype(int)
    
    
    temp3 = wb_phase.total_assets.apply(change_assets_value)
    temp3 = temp3.astype(int)
    
    #Change total_assets column
    wb_phase.total_assets = temp3
    
    
    #Do the same with 'movable_assets' and 'immovable_assets' 
    
    temp3 = wb_phase.movable_assets.apply(change_assets_value)
    temp3 = temp3.astype(int)
    
    wb_phase.movable_assets = temp3
    
    temp4 = wb_phase.immovable_assets.apply(change_assets_value)
    temp4 = temp4.astype(int)
    
    wb_phase.immovable_assets = temp4
    
    # We need to do the same with 'liabilities', 'self_income', and 'total_income'
        
    temp5 = wb_phase.self_income.apply(change_assets_value)
    temp5 = temp5.astype(int)
    wb_phase.self_income = temp5
    
    temp6 = wb_phase.total_income.apply(change_assets_value)
    temp6 = temp6.astype(int)
    wb_phase.total_income = temp6
    
    
    temp7 = wb_phase.liabilities.apply(change_assets_value)
    temp7 = temp7.astype(int)
    wb_phase.liabilities = temp7
    
    
    return wb_phase

#Test with West Bengal Phase 3 file

wb_phase3= extract_and_process(csv_name = "Assembly-Elections-West-Bengal-2021-constituencies-list-Phase-3.csv",
                    url="http://api.myneta.info/API_2021/ver_4.1/getDataWestBengal2021BasicDetails.php?message=",
                    url_api_key="&apikey=253619C1F75775497259634A6F46B")

## Test successful

## Test with Tamil Nadu (change csv_name and URL as per instructions)
## Don't forget to add: .csv  ;) 
### Got to change working directory first - jesus, mary, and Joseph
os.chdir("C:\\Users\Gautam\Desktop\IndiaSpend\Research\State Elections 2021 - Mar-Apr/Tamil_Nadu")

tamil_nadu_collated_data = extract_and_process(csv_name = 'Assembly Elections Tamil Nadu 2021 constituencies list.csv',
                                               url="http://api.myneta.info/API_2020/ver_4.1/getDataTamilNadu2021BasicDetails.php?message=",
                                               url_api_key="&apikey=253619C1F75775497259634A6F46B")

#Diagnosis - working fine on West Bengal but bugging for Tamil Nadu. Need to fix bugs. 