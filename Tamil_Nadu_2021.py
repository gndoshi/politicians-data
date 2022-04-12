# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 11:01:41 2021

@author: Gautam
"""
###>>>>>> Tamil Nadu <<<<<<<####
import numpy as np
import pandas as pd
import json as js
import os
os.chdir("C:\\Users\Gautam\Desktop\IndiaSpend\Research\State Elections 2021 - Mar-Apr/Tamil_Nadu")

TN_constituency_list= pd.read_csv('Assembly Elections Tamil Nadu 2021 constituencies list.csv') 

import urllib.request

#URl for Tamil Nadu is diffirent 
yes2 = [] 

for const in TN_constituency_list["Constituency"]:
    if len(const.split(' '))!=1: 
        if len(const.split(' '))>2:
            temp_str = const.split(' ')[0]+'%20'+const.split(' ')[1]+'%20'+const.split(' ')[2]
        else:
            temp_str = const.split(' ')[0]+'%20'+const.split(' ')[1]
    else:
        temp_str = const
    new1 = "http://api.myneta.info/API_2021/ver_4.1/getDataTamilNadu2021BasicDetails.php?message="+temp_str+"&apikey=253619C1F75775497259634A6F46B"
    with urllib.request.urlopen(new1) as new_work:
        data1= js.loads(new_work.read())
    
    yes2+=data1
    
Tamil_Nadu_1 = pd.DataFrame.from_dict(yes2)




#Changing 'Yes (x) to Int. X and 'No' to 0 in the column of: Cases' 

def change_cases_value(current_value):
    
    if 'Yes' in current_value:
        if len(current_value.split(' ')[1]) == 4:
               val= current_value.split(' ')[1][1:3]
        else:
            val = current_value.split(' ')[1][1:2]
    elif 'No' in current_value: 
        val = '0'

    return val

temp_list = Tamil_Nadu_1.cases.apply(change_cases_value)
temp_list = temp_list.astype(int)

Tamil_Nadu_1.cases = temp_list 

#Changing Age ad IPC Count columns to integers from strings
Tamil_Nadu_1.age = Tamil_Nadu_1.age.astype(int)
Tamil_Nadu_1.serious_ipc_counts = Tamil_Nadu_1.serious_ipc_counts.astype(int)

def change_assets_value(curr_val):
    curr_val=str(curr_val)
    if 'Lac' in curr_val: 
        val1 = float(curr_val[:-3])*(10**5)
    elif 'Crore' in curr_val: 
        val1 = float(curr_val[:-5])*(10**7)
    else: 
        val1 = float(curr_val)
    
    return val1

temp2 = Tamil_Nadu_1.total_assets.apply(change_assets_value)
temp2 = temp2.astype(int)

#Change total_assets column
Tamil_Nadu_1.total_assets = temp2

#Do the same with 'movable_assets' and 'immovable_assets' 

temp3 = Tamil_Nadu_1.movable_assets.apply(change_assets_value)
temp3 = temp3.astype(int)

Tamil_Nadu_1.movable_assets = temp3

temp4 = Tamil_Nadu_1.immovable_assets.apply(change_assets_value)
temp4 = temp4.astype(int)

Tamil_Nadu_1.immovable_assets = temp4

# We need to do the same with 'liabilities', 'self_income', and 'total_income'
del temp4, temp3, temp2, temp_list

temp5 = Tamil_Nadu_1.self_income.apply(change_assets_value)
temp5 = temp5.astype(int)
Tamil_Nadu_1.self_income = temp5

temp6 = Tamil_Nadu_1.total_income.apply(change_assets_value)
temp6 = temp6.astype(int)
Tamil_Nadu_1.total_income = temp6


del temp5, temp6 
temp7 = Tamil_Nadu_1.liabilities.apply(change_assets_value)
temp7 = temp7.astype(int)
Tamil_Nadu_1.liabilities = temp7

del temp7
#Export Dataset
Tamil_Nadu_1.to_csv('TamilNadu2021_collated_data.csv')