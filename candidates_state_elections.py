# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 13:15:06 2021

@author: Gautam
"""
import numpy as np
import pandas as pd
import json as js
import os
os.chdir("C:\\Users\Gautam\Desktop\IndiaSpend\Research\State Elections 2021 - Mar-Apr/West_Bengal")


with open("getDataWestBengal2021BasicDetails.json") as file: 
    data = js.load(file)

test = pd.DataFrame.from_dict(data)

constituency_list= pd.read_csv('wb2021_const_list_ph1.csv') 

import urllib.request

yes = [] 

for const in constituency_list["Constituency"]:
    if len(const.split(' '))!=1: 
        temp_str = const.split(' ')[0]+'%20'+const.split(' ')[1]
    else:
        temp_str = const
    new1 = "http://api.myneta.info/API_2021/ver_4.1/getDataWestBengal2021BasicDetails.php?message="+temp_str+"&apikey=253619C1F75775497259634A6F46B"
    with urllib.request.urlopen(new1) as new_work:
        data1= js.loads(new_work.read())
    
    yes+=data1
    
wb_phase1 = pd.DataFrame.from_dict(yes)




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

temp_list = wb_phase1.cases.apply(change_cases_value)
temp_list = temp_list.astype(int)

wb_phase1.cases = temp_list 

#Changing Age ad IPC Count columns to integers from strings
wb_phase1.age = wb_phase1.age.astype(int)
wb_phase1.serious_ipc_counts = wb_phase1.serious_ipc_counts.astype(int)

def change_assets_value(curr_val):
    curr_val=str(curr_val)
    if 'Lac' in curr_val: 
        val1 = float(curr_val[:-3])*(10**5)
    elif 'Crore' in curr_val: 
        val1 = float(curr_val[:-5])*(10**7)
    else: 
        val1 = float(curr_val)
    
    return val1

temp2 = wb_phase1.total_assets.apply(change_assets_value)
temp2 = temp2.astype(int)

#Change total_assets column
wb_phase1.total_assets = temp2

#Do the same with 'movable_assets' and 'immovable_assets' 

temp3 = wb_phase1.movable_assets.apply(change_assets_value)
temp3 = temp3.astype(int)

wb_phase1.movable_assets = temp3

temp4 = wb_phase1.immovable_assets.apply(change_assets_value)
temp4 = temp4.astype(int)

wb_phase1.immovable_assets = temp4

# We need to do the same with 'liabilities', 'self_income', and 'total_income'
del temp4, temp3, temp2, temp_list

temp5 = wb_phase1.self_income.apply(change_assets_value)
temp5 = temp5.astype(int)
wb_phase1.self_income = temp5

temp6 = wb_phase1.total_income.apply(change_assets_value)
temp6 = temp6.astype(int)
wb_phase1.total_income = temp6


del temp5, temp6 
temp7 = wb_phase1.liabilities.apply(change_assets_value)
temp7 = temp7.astype(int)
wb_phase1.liabilities = temp7


#Export Dataset
wb_phase1.to_csv('wb_phase1_collated_data.csv')


##############<<<<<<<<< Phase 2 >>>>>>>>#########


constituency_list_ph2 = pd.read_csv('Assembly-Elections-West-Bengal-2021-constituencies-list-Phase-2.csv') 

import urllib.request

yes2 = [] 

for const in constituency_list_ph2["Constituency"]:
    if len(const.split(' '))!=1: 
        temp_str = const.split(' ')[0]+'%20'+const.split(' ')[1]
    else:
        temp_str = const
    new1 = "http://api.myneta.info/API_2021/ver_4.1/getDataWestBengal2021BasicDetails.php?message="+temp_str+"&apikey=253619C1F75775497259634A6F46B"
    with urllib.request.urlopen(new1) as new_work:
        data1= js.loads(new_work.read())
    
    yes2+=data1
    
wb_phase2 = pd.DataFrame.from_dict(yes2)




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

temp_list2 = wb_phase2.cases.apply(change_cases_value)
temp_list2 = temp_list2.astype(int)

wb_phase2.cases = temp_list2 

#Changing Age ad IPC Count columns to integers from strings
wb_phase2.age = wb_phase2.age.astype(int)
wb_phase2.serious_ipc_counts = wb_phase2.serious_ipc_counts.astype(int)

def change_assets_value(curr_val):
    curr_val=str(curr_val)
    if 'Lac' in curr_val: 
        val1 = float(curr_val[:-3])*(10**5)
    elif 'Crore' in curr_val: 
        val1 = float(curr_val[:-5])*(10**7)
    else: 
        val1 = float(curr_val)
    
    return val1

temp2 = wb_phase2.total_assets.apply(change_assets_value)
temp2 = temp2.astype(int)

#Change total_assets column
wb_phase2.total_assets = temp2

#Do the same with 'movable_assets' and 'immovable_assets' 

temp3 = wb_phase2.movable_assets.apply(change_assets_value)
temp3 = temp3.astype(int)

wb_phase2.movable_assets = temp3

temp4 = wb_phase2.immovable_assets.apply(change_assets_value)
temp4 = temp4.astype(int)

wb_phase2.immovable_assets = temp4

# We need to do the same with 'liabilities', 'self_income', and 'total_income'
del temp4, temp3, temp2

temp5 = wb_phase2.self_income.apply(change_assets_value)
temp5 = temp5.astype(int)
wb_phase2.self_income = temp5

temp6 = wb_phase2.total_income.apply(change_assets_value)
temp6 = temp6.astype(int)
wb_phase2.total_income = temp6


del temp5, temp6 
temp7 = wb_phase2.liabilities.apply(change_assets_value)
temp7 = temp7.astype(int)
wb_phase2.liabilities = temp7


#Export Dataset
wb_phase2.to_csv('wb_phase2_collated_data.csv')

#>>>>>>>>>>>>> Phase 3 <<<<<<<<<<<<<<<<<<<<<




constituency_list_ph3 = pd.read_csv('Assembly-Elections-West-Bengal-2021-constituencies-list-Phase-3.csv') 

yes2 = [] 

for const in constituency_list_ph3["Constituency"]:
    if len(const.split(' '))!=1: 
        if len(const.split(' '))>2: 
               temp_str = const.split(' ')[0]+'%20'+const.split(' ')[1]+'%20'+const.split(' ')[2]
        else:
            temp_str = const.split(' ')[0]+'%20'+const.split(' ')[1]
    else:
        temp_str = const
    new1 = "http://api.myneta.info/API_2021/ver_4.1/getDataWestBengal2021BasicDetails.php?message="+temp_str+"&apikey=253619C1F75775497259634A6F46B"
    with urllib.request.urlopen(new1) as new_work:
        data1= js.loads(new_work.read())
    
    yes2+=data1
    
wb_phase3 = pd.DataFrame.from_dict(yes2)




#Changing 'Yes (x) to Int. X and 'No' to 0 in the column of: Cases' 



temp_list3 = wb_phase3.cases.apply(change_cases_value)
temp_list3 = temp_list3.astype(int)

wb_phase3.cases = temp_list3 

#Changing Age ad IPC Count columns to integers from strings
wb_phase3.age = wb_phase3.age.astype(int)
wb_phase3.serious_ipc_counts = wb_phase3.serious_ipc_counts.astype(int)


temp3 = wb_phase3.total_assets.apply(change_assets_value)
temp3 = temp3.astype(int)

#Change total_assets column
wb_phase3.total_assets = temp3

del temp3 ##uff so confusing this is. 

#Do the same with 'movable_assets' and 'immovable_assets' 

temp3 = wb_phase3.movable_assets.apply(change_assets_value)
temp3 = temp3.astype(int)

wb_phase3.movable_assets = temp3

temp4 = wb_phase3.immovable_assets.apply(change_assets_value)
temp4 = temp4.astype(int)

wb_phase3.immovable_assets = temp4

# We need to do the same with 'liabilities', 'self_income', and 'total_income'
del temp4, temp3, temp_list3

temp5 = wb_phase3.self_income.apply(change_assets_value)
temp5 = temp5.astype(int)
wb_phase3.self_income = temp5

temp6 = wb_phase3.total_income.apply(change_assets_value)
temp6 = temp6.astype(int)
wb_phase3.total_income = temp6


del temp5, temp6 
temp7 = wb_phase3.liabilities.apply(change_assets_value)
temp7 = temp7.astype(int)
wb_phase3.liabilities = temp7
del temp7,temp_str

#Export Dataset
wb_phase3.to_csv('wb_phase3_collated_data.csv')


######>>>>>>>>>>>>> Phase 4 <<<<<<<<<<<<<##########
constituency_list_ph4 = pd.read_csv('Assembly Elections West Bengal 2021 constituencies list- Phase-4.csv') 

yes2 = [] 

for const in constituency_list_ph4["Constituency"]:
    if len(const.split(' '))!=1: 
        if len(const.split(' '))>2: 
               temp_str = const.split(' ')[0]+'%20'+const.split(' ')[1]+'%20'+const.split(' ')[2]
        else:
            temp_str = const.split(' ')[0]+'%20'+const.split(' ')[1]
    else:
        temp_str = const
    new1 = "http://api.myneta.info/API_2021/ver_4.1/getDataWestBengal2021BasicDetails.php?message="+temp_str+"&apikey=253619C1F75775497259634A6F46B"
    with urllib.request.urlopen(new1) as new_work:
        data1= js.loads(new_work.read())
    
    yes2+=data1
    
wb_phase4 = pd.DataFrame.from_dict(yes2)

#Changing 'Yes (x) to Int. X and 'No' to 0 in the column of: Cases' 



temp_list3 = wb_phase4.cases.apply(change_cases_value)
temp_list3 = temp_list3.astype(int)

wb_phase4.cases = temp_list3 

#Changing Age ad IPC Count columns to integers from strings
wb_phase4.age = wb_phase4.age.astype(int)
wb_phase4.serious_ipc_counts = wb_phase4.serious_ipc_counts.astype(int)


temp3 = wb_phase4.total_assets.apply(change_assets_value)
temp3 = temp3.astype(int)

#Change total_assets column
wb_phase4.total_assets = temp3

del temp3 ##uff so confusing this is. 

#Do the same with 'movable_assets' and 'immovable_assets' 

temp3 = wb_phase4.movable_assets.apply(change_assets_value)
temp3 = temp3.astype(int)

wb_phase4.movable_assets = temp3

temp4 = wb_phase4.immovable_assets.apply(change_assets_value)
temp4 = temp4.astype(int)

wb_phase4.immovable_assets = temp4

# We need to do the same with 'liabilities', 'self_income', and 'total_income'
del temp4, temp3, temp_list3

temp5 = wb_phase4.self_income.apply(change_assets_value)
temp5 = temp5.astype(int)
wb_phase4.self_income = temp5

temp6 = wb_phase4.total_income.apply(change_assets_value)
temp6 = temp6.astype(int)
wb_phase4.total_income = temp6


del temp5, temp6 
temp7 = wb_phase4.liabilities.apply(change_assets_value)
temp7 = temp7.astype(int)
wb_phase4.liabilities = temp7
del temp7,temp_str

#Export Dataset
wb_phase4.to_csv('wb_phase4_collated_data.csv')

######>>>>>>>>>>>>> Phase 5 <<<<<<<<<<<<<##########
constituency_list_ph5 = pd.read_csv('Assembly Elections West Bengal 2021 constituencies list- Phase-5.csv') 

yes2 = [] 

for const in constituency_list_ph5["Constituency"]:
    if len(const.split(' '))!=1: 
        if len(const.split(' '))>3: 
               temp_str = const.split(' ')[0]+'%20'+const.split(' ')[1]+'%20'+const.split(' ')[2]+'%20'+const.split(' ')[3]
        elif len(const.split(' '))>2: 
               temp_str = const.split(' ')[0]+'%20'+const.split(' ')[1]+'%20'+const.split(' ')[2]
        else:
            temp_str = const.split(' ')[0]+'%20'+const.split(' ')[1]
    else:
        temp_str = const
    new1 = "http://api.myneta.info/API_2021/ver_4.1/getDataWestBengal2021BasicDetails.php?message="+temp_str+"&apikey=253619C1F75775497259634A6F46B"
    with urllib.request.urlopen(new1) as new_work:
        data1= js.loads(new_work.read())
    
    yes2+=data1
    
wb_phase5 = pd.DataFrame.from_dict(yes2)

#Changing 'Yes (x) to Int. X and 'No' to 0 in the column of: Cases' 



temp_list3 = wb_phase5.cases.apply(change_cases_value)
temp_list3 = temp_list3.astype(int)

wb_phase5.cases = temp_list3 

#Changing Age ad IPC Count columns to integers from strings
wb_phase5.age = wb_phase5.age.astype(int)
wb_phase5.serious_ipc_counts = wb_phase5.serious_ipc_counts.astype(int)


temp3 = wb_phase5.total_assets.apply(change_assets_value)
temp3 = temp3.astype(int)

#Change total_assets column
wb_phase5.total_assets = temp3

del temp3 ##uff so confusing this is. 

#Do the same with 'movable_assets' and 'immovable_assets' 

temp3 = wb_phase5.movable_assets.apply(change_assets_value)
temp3 = temp3.astype(int)

wb_phase5.movable_assets = temp3

temp4 = wb_phase5.immovable_assets.apply(change_assets_value)
temp4 = temp4.astype(int)

wb_phase5.immovable_assets = temp4

# We need to do the same with 'liabilities', 'self_income', and 'total_income'
del temp4, temp3, temp_list3

temp5 = wb_phase5.self_income.apply(change_assets_value)
temp5 = temp5.astype(int)
wb_phase5.self_income = temp5

temp6 = wb_phase5.total_income.apply(change_assets_value)
temp6 = temp6.astype(int)
wb_phase5.total_income = temp6


del temp5, temp6 
temp7 = wb_phase5.liabilities.apply(change_assets_value)
temp7 = temp7.astype(int)
wb_phase5.liabilities = temp7
del temp7,temp_str

#Export Dataset
wb_phase5.to_csv('wb_phase5_collated_data.csv')
del const, data1, new1, new_work, yes2, temp_str

######>>>>>>>>>>>>> Phase 6 <<<<<<<<<<<<<##########
constituency_list_ph6 = pd.read_csv('Assembly Elections West Bengal 2021 constituencies list- Phase-6.csv') 

yes2 = [] 

for const in constituency_list_ph6["Constituency"]:
    if len(const.split(' '))!=1: 
        if len(const.split(' '))>3: 
               temp_str = const.split(' ')[0]+'%20'+const.split(' ')[1]+'%20'+const.split(' ')[2]+'%20'+const.split(' ')[3]
        elif len(const.split(' '))>2: 
               temp_str = const.split(' ')[0]+'%20'+const.split(' ')[1]+'%20'+const.split(' ')[2]
        else:
            temp_str = const.split(' ')[0]+'%20'+const.split(' ')[1]
    else:
        temp_str = const
    new1 = "http://api.myneta.info/API_2021/ver_4.1/getDataWestBengal2021BasicDetails.php?message="+temp_str+"&apikey=253619C1F75775497259634A6F46B"
    with urllib.request.urlopen(new1) as new_work:
        data1= js.loads(new_work.read())
    
    yes2+=data1
    
wb_phase6 = pd.DataFrame.from_dict(yes2)

#Changing 'Yes (x) to Int. X and 'No' to 0 in the column of: Cases' 



temp_list3 = wb_phase6.cases.apply(change_cases_value)
temp_list3 = temp_list3.astype(int)

wb_phase6.cases = temp_list3 

#Changing Age ad IPC Count columns to integers from strings
wb_phase6.age = wb_phase6.age.astype(int)
wb_phase6.serious_ipc_counts = wb_phase6.serious_ipc_counts.astype(int)


temp3 = wb_phase6.total_assets.apply(change_assets_value)
temp3 = temp3.astype(int)

#Change total_assets column
wb_phase6.total_assets = temp3

del temp3 ##uff so confusing this is. 

#Do the same with 'movable_assets' and 'immovable_assets' 

temp3 = wb_phase6.movable_assets.apply(change_assets_value)
temp3 = temp3.astype(int)

wb_phase6.movable_assets = temp3

temp4 = wb_phase6.immovable_assets.apply(change_assets_value)
temp4 = temp4.astype(int)

wb_phase6.immovable_assets = temp4

# We need to do the same with 'liabilities', 'self_income', and 'total_income'
del temp4, temp3, temp_list3

temp5 = wb_phase6.self_income.apply(change_assets_value)
temp5 = temp5.astype(int)
wb_phase6.self_income = temp5

temp6 = wb_phase6.total_income.apply(change_assets_value)
temp6 = temp6.astype(int)
wb_phase6.total_income = temp6


del temp5, temp6 
temp7 = wb_phase6.liabilities.apply(change_assets_value)
temp7 = temp7.astype(int)
wb_phase6.liabilities = temp7
del temp7,temp_str

#Export Dataset
wb_phase6.to_csv('wb_phase6_collated_data.csv')
del const, data1, new1, new_work, yes2, temp_str


######>>>>>>>>>>>>> Phase 7 <<<<<<<<<<<<<##########
constituency_list_ph7 = pd.read_csv('Assembly Elections West Bengal 2021 constituencies list- Phase-7.csv') 

yes2 = [] 

for const in constituency_list_ph7["Constituency"]:
    if len(const.split(' '))!=1: 
        if len(const.split(' '))>3: 
               temp_str = const.split(' ')[0]+'%20'+const.split(' ')[1]+'%20'+const.split(' ')[2]+'%20'+const.split(' ')[3]
        elif len(const.split(' '))>2: 
               temp_str = const.split(' ')[0]+'%20'+const.split(' ')[1]+'%20'+const.split(' ')[2]
        else:
            temp_str = const.split(' ')[0]+'%20'+const.split(' ')[1]
    else:
        temp_str = const
    new1 = "http://api.myneta.info/API_2021/ver_4.1/getDataWestBengal2021BasicDetails.php?message="+temp_str+"&apikey=253619C1F75775497259634A6F46B"
    with urllib.request.urlopen(new1) as new_work:
        data1= js.loads(new_work.read())
    
    yes2+=data1
    
wb_phase7 = pd.DataFrame.from_dict(yes2)

#Changing 'Yes (x) to Int. X and 'No' to 0 in the column of: Cases' 



temp_list3 = wb_phase7.cases.apply(change_cases_value)
temp_list3 = temp_list3.astype(int)

wb_phase7.cases = temp_list3 

#Changing Age ad IPC Count columns to integers from strings
wb_phase7.age = wb_phase7.age.astype(int)
wb_phase7.serious_ipc_counts = wb_phase7.serious_ipc_counts.astype(int)


temp3 = wb_phase7.total_assets.apply(change_assets_value)
temp3 = temp3.astype(int)

#Change total_assets column
wb_phase7.total_assets = temp3

del temp3 ##uff so confusing this is. 

#Do the same with 'movable_assets' and 'immovable_assets' 

temp3 = wb_phase7.movable_assets.apply(change_assets_value)
temp3 = temp3.astype(int)

wb_phase7.movable_assets = temp3

temp4 = wb_phase7.immovable_assets.apply(change_assets_value)
temp4 = temp4.astype(int)

wb_phase7.immovable_assets = temp4

# We need to do the same with 'liabilities', 'self_income', and 'total_income'
del temp4, temp3, temp_list3

temp5 = wb_phase7.self_income.apply(change_assets_value)
temp5 = temp5.astype(int)
wb_phase7.self_income = temp5

temp6 = wb_phase7.total_income.apply(change_assets_value)
temp6 = temp6.astype(int)
wb_phase7.total_income = temp6


del temp5, temp6 
temp7 = wb_phase7.liabilities.apply(change_assets_value)
temp7 = temp7.astype(int)
wb_phase7.liabilities = temp7
del temp7,temp_str

#Export Dataset
wb_phase7.to_csv('wb_phase7_collated_data.csv')
del const, data1, new1, new_work, yes2, temp_str

######>>>>>>>>>>>>> Phase 8 <<<<<<<<<<<<<##########
constituency_list_ph8 = pd.read_csv('Assembly Elections West Bengal 2021 constituencies list- Phase-8.csv') 

yes2 = [] 

for const in constituency_list_ph8["Constituency"]:
    if len(const.split(' '))!=1: 
        if len(const.split(' '))>3: 
               temp_str = const.split(' ')[0]+'%20'+const.split(' ')[1]+'%20'+const.split(' ')[2]+'%20'+const.split(' ')[3]
        elif len(const.split(' '))>2: 
               temp_str = const.split(' ')[0]+'%20'+const.split(' ')[1]+'%20'+const.split(' ')[2]
        else:
            temp_str = const.split(' ')[0]+'%20'+const.split(' ')[1]
    else:
        temp_str = const
    new1 = "http://api.myneta.info/API_2021/ver_4.1/getDataWestBengal2021BasicDetails.php?message="+temp_str+"&apikey=253619C1F75775497259634A6F46B"
    with urllib.request.urlopen(new1) as new_work:
        data1= js.loads(new_work.read())
    
    yes2+=data1
    
wb_phase8 = pd.DataFrame.from_dict(yes2)

#Changing 'Yes (x) to Int. X and 'No' to 0 in the column of: Cases' 



temp_list3 = wb_phase8.cases.apply(change_cases_value)
temp_list3 = temp_list3.astype(int)

wb_phase8.cases = temp_list3 

#Changing Age ad IPC Count columns to integers from strings
wb_phase8.age = wb_phase8.age.astype(int)
wb_phase8.serious_ipc_counts = wb_phase8.serious_ipc_counts.astype(int)


temp3 = wb_phase8.total_assets.apply(change_assets_value)
temp3 = temp3.astype(int)

#Change total_assets column
wb_phase8.total_assets = temp3

del temp3 ##uff so confusing this is. 

#Do the same with 'movable_assets' and 'immovable_assets' 

temp3 = wb_phase8.movable_assets.apply(change_assets_value)
temp3 = temp3.astype(int)

wb_phase8.movable_assets = temp3

temp4 = wb_phase8.immovable_assets.apply(change_assets_value)
temp4 = temp4.astype(int)

wb_phase8.immovable_assets = temp4

# We need to do the same with 'liabilities', 'self_income', and 'total_income'
del temp4, temp3, temp_list3

temp5 = wb_phase8.self_income.apply(change_assets_value)
temp5 = temp5.astype(int)
wb_phase8.self_income = temp5

temp6 = wb_phase8.total_income.apply(change_assets_value)
temp6 = temp6.astype(int)
wb_phase8.total_income = temp6


del temp5, temp6 
temp7 = wb_phase8.liabilities.apply(change_assets_value)
temp7 = temp7.astype(int)
wb_phase8.liabilities = temp7
del temp7,temp_str

#Export Dataset
wb_phase8.to_csv('wb_phase8_collated_data.csv')
del const, data1, new1, new_work, yes2, temp_str

