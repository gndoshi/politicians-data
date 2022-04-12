# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 11:18:30 2021

@author: Gautam
"""
###>>>>>> Assam <<<<<<<#####

######>>>>>> Phase 1 <<<<<<<<<<######

import numpy as np
import pandas as pd
import json as js
import os
os.chdir("C:\\Users\Gautam\Desktop\IndiaSpend\Research\State Elections 2021 - Mar-Apr/Assam")

Assam_constituency_list= pd.read_csv('Assembly Elections Assam 2021 constituencies list- Phase-1.csv') 

import urllib.request

#URl for Assam is diffirent 
yes2 = [] 

for const in Assam_constituency_list["Constituency"]:
    if len(const.split(' '))!=1: 
        if len(const.split(' '))>2:
            temp_str = const.split(' ')[0]+'%20'+const.split(' ')[1]+'%20'+const.split(' ')[2]
        else:
            temp_str = const.split(' ')[0]+'%20'+const.split(' ')[1]
    else:
        temp_str = const
    new1 = "http://api.myneta.info/API_2021/ver_4.1/getDataAssam2021BasicDetails.php?message="+temp_str+"&apikey=253619C1F75775497259634A6F46B"
    with urllib.request.urlopen(new1) as new_work:
        data1= js.loads(new_work.read())
    
    yes2+=data1
    
assam_ph1 = pd.DataFrame.from_dict(yes2)




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

temp_list = assam_ph1.cases.apply(change_cases_value)
temp_list = temp_list.astype(int)

assam_ph1.cases = temp_list 

#Changing Age ad IPC Count columns to integers from strings
assam_ph1.age = assam_ph1.age.astype(int)
assam_ph1.serious_ipc_counts = assam_ph1.serious_ipc_counts.astype(int)

def change_assets_value(curr_val):
    curr_val=str(curr_val)
    if 'Lac' in curr_val: 
        val1 = float(curr_val[:-3])*(10**5)
    elif 'Crore' in curr_val: 
        val1 = float(curr_val[:-5])*(10**7)
    else: 
        val1 = float(curr_val)
    
    return val1

temp2 = assam_ph1.total_assets.apply(change_assets_value)
temp2 = temp2.astype(int)

#Change total_assets column
assam_ph1.total_assets = temp2

#Do the same with 'movable_assets' and 'immovable_assets' 

temp3 = assam_ph1.movable_assets.apply(change_assets_value)
temp3 = temp3.astype(int)

assam_ph1.movable_assets = temp3

temp4 = assam_ph1.immovable_assets.apply(change_assets_value)
temp4 = temp4.astype(int)

assam_ph1.immovable_assets = temp4

# We need to do the same with 'liabilities', 'self_income', and 'total_income'
del temp4, temp3, temp2, temp_list

temp5 = assam_ph1.self_income.apply(change_assets_value)
temp5 = temp5.astype(int)
assam_ph1.self_income = temp5

temp6 = assam_ph1.total_income.apply(change_assets_value)
temp6 = temp6.astype(int)
assam_ph1.total_income = temp6


del temp5, temp6 
temp7 = assam_ph1.liabilities.apply(change_assets_value)
temp7 = temp7.astype(int)
assam_ph1.liabilities = temp7

del temp7
#Export Dataset
assam_ph1.to_csv('Assam2021-Phase1_collated_data.csv')


######>>>>>>>>>>Phase 2<<<<<<<<########3
del temp_str, yes2, const, data1, new1, new_work
Assam_constituency_list_ph2= pd.read_csv('Assembly Elections Assam 2021 constituencies list- Phase-2.csv') 



#URl for Assam is diffirent 
yes2 = [] 

for const in Assam_constituency_list_ph2["Constituency"]:
    if len(const.split(' '))!=1: 
        if len(const.split(' '))>2:
            temp_str = const.split(' ')[0]+'%20'+const.split(' ')[1]+'%20'+const.split(' ')[2]
        else:
            temp_str = const.split(' ')[0]+'%20'+const.split(' ')[1]
    else:
        temp_str = const
    new1 = "http://api.myneta.info/API_2021/ver_4.1/getDataAssam2021BasicDetails.php?message="+temp_str+"&apikey=253619C1F75775497259634A6F46B"
    with urllib.request.urlopen(new1) as new_work:
        data1= js.loads(new_work.read())
    
    yes2+=data1
    
assam_ph2 = pd.DataFrame.from_dict(yes2)

#Changing 'Yes (x) to Int. X and 'No' to 0 in the column of: Cases' 


temp_list = assam_ph2.cases.apply(change_cases_value)
temp_list = temp_list.astype(int)

assam_ph2.cases = temp_list 

#Changing Age ad IPC Count columns to integers from strings
assam_ph2.age = assam_ph2.age.astype(int)
assam_ph2.serious_ipc_counts = assam_ph2.serious_ipc_counts.astype(int)


temp2 = assam_ph2.total_assets.apply(change_assets_value)
temp2 = temp2.astype(int)

#Change total_assets column
assam_ph2.total_assets = temp2

#Do the same with 'movable_assets' and 'immovable_assets' 

temp3 = assam_ph2.movable_assets.apply(change_assets_value)
temp3 = temp3.astype(int)

assam_ph2.movable_assets = temp3

temp4 = assam_ph2.immovable_assets.apply(change_assets_value)
temp4 = temp4.astype(int)

assam_ph2.immovable_assets = temp4

# We need to do the same with 'liabilities', 'self_income', and 'total_income'
del temp4, temp3, temp2, temp_list

temp5 = assam_ph2.self_income.apply(change_assets_value)
temp5 = temp5.astype(int)
assam_ph2.self_income = temp5

temp6 = assam_ph2.total_income.apply(change_assets_value)
temp6 = temp6.astype(int)
assam_ph2.total_income = temp6


del temp5, temp6 
temp7 = assam_ph2.liabilities.apply(change_assets_value)
temp7 = temp7.astype(int)
assam_ph2.liabilities = temp7

del temp7
#Export Dataset
assam_ph2.to_csv('Assam2021-Phase2_collated_data.csv')



####>>>>>>>>> Phase 3 <<<<<<<<<<<#########
Assam_constituency_list_ph3= pd.read_csv('Assembly Elections Assam 2021 constituencies list- Phase-3.csv') 
yes2 = [] 

for const in Assam_constituency_list_ph3["Constituency"]:
    if len(const.split(' '))!=1: 
        if len(const.split(' '))>2:
            temp_str = const.split(' ')[0]+'%20'+const.split(' ')[1]+'%20'+const.split(' ')[2]
        else:
            temp_str = const.split(' ')[0]+'%20'+const.split(' ')[1]
    else:
        temp_str = const
    new1 = "http://api.myneta.info/API_2021/ver_4.1/getDataAssam2021BasicDetails.php?message="+temp_str+"&apikey=253619C1F75775497259634A6F46B"
    with urllib.request.urlopen(new1) as new_work:
        data1= js.loads(new_work.read())
    
    yes2+=data1
    
assam_ph3 = pd.DataFrame.from_dict(yes2)

#Changing 'Yes (x) to Int. X and 'No' to 0 in the column of: Cases' 

temp_list3 = assam_ph3.cases.apply(change_cases_value)
temp_list3 = temp_list3.astype(int)

assam_ph3.cases = temp_list3 

#Changing Age ad IPC Count columns to integers from strings
assam_ph3.age = assam_ph3.age.astype(int)
assam_ph3.serious_ipc_counts = assam_ph3.serious_ipc_counts.astype(int)


temp3 = assam_ph3.total_assets.apply(change_assets_value)
temp3 = temp3.astype(int)

#Change total_assets column
assam_ph3.total_assets = temp3

del temp3 ##uff so confusing this is. 

#Do the same with 'movable_assets' and 'immovable_assets' 

temp3 = assam_ph3.movable_assets.apply(change_assets_value)
temp3 = temp3.astype(int)

assam_ph3.movable_assets = temp3

temp4 = assam_ph3.immovable_assets.apply(change_assets_value)
temp4 = temp4.astype(int)

assam_ph3.immovable_assets = temp4

# We need to do the same with 'liabilities', 'self_income', and 'total_income'
del temp4, temp3, temp_list3

temp5 = assam_ph3.self_income.apply(change_assets_value)
temp5 = temp5.astype(int)
assam_ph3.self_income = temp5

temp6 = assam_ph3.total_income.apply(change_assets_value)
temp6 = temp6.astype(int)
assam_ph3.total_income = temp6


del temp5, temp6 
temp7 = assam_ph3.liabilities.apply(change_assets_value)
temp7 = temp7.astype(int)
assam_ph3.liabilities = temp7
del temp7,temp_str

#Export Dataset
assam_ph3.to_csv('assam_ph3_collated_data.csv')
del const, data1, new1, new_work, yes2