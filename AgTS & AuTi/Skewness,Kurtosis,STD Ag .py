# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 16:07:42 2024

@author: 15253
"""

import matplotlib.gridspec as gridspec
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import re
from natsort import natsorted
from scipy.optimize import curve_fit
from scipy.interpolate import make_interp_spline
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import mean_squared_error, r2_score
import math
import matplotlib.ticker as mtick
from scipy.stats import skew
from scipy.stats import kurtosis
import csv



sc='sc'
fc='fc'
c=chr(92)
carbo_folder_path= r'Q:\Shared drives\MSE-Thuo Group\Group Server ISU\Zizhi\Data\Data Analysis\New dataset AgTS\Combined'
#carbonLen = [9,11,13,15]
dogs=np.linspace(10,17,8)

def findRelatedData(filename1, filename2): #Finding data file with _data.txt as spot and date filenames are as follows: spot 1 scan 1-20 vs spot 1 scan 1-20_data.txt
    
    fileTXT = []
    
    for file in filename2:
        if(file[-1] == ')'):
            temp_str = file[-4:]
            fileM = file[:-4] + '_data' + temp_str + '.txt'
        else:
            fileM = file + '_data.txt'
        if fileM in filename1:
            fileTXT.append(fileM)
           
    return fileTXT

def DataConcat(Series):
    i=0
    Full=pd.DataFrame()
    dfs=pd.DataFrame()
    df=[]
    for values in Series:
        df=pd.read_csv(values,sep='\t',on_bad_lines='skip')
        if i==1:
            x=dfs.columns
            b=df.columns
            df=df.rename(columns={b[k]:x[k] for k in range(len(b))})
            Full=pd.concat([dfs,df],ignore_index=True)
        elif i>=2:
            c=df.columns
            df=df.rename(columns={c[j]:x[j] for j in range(len(c))})
            Full=pd.concat([Full,df],ignore_index=True)
        i=i+1
        dfs=df
    if i==1:
        Full=df
    new_names=['Voltage (V)','Absolute Value of J','Current Density (J)','Current','Time']
    columns=Full.columns.tolist()
    for i in range(len(new_names)):
        columns[i]=new_names[i]
    Full.columns=columns
    if len(Full.columns)>=7:
        Full=Full.drop(Full.columns[[5,6]],axis=1)
    #else:
        #Full=Full.drop(Full.columns[5], axis=1)
    Full=Full.iloc[:,:5]
    return Full

def search_files_with_same_number(folder_path, number):
    matching_files = []

    for file in os.listdir(folder_path):
        if file.endswith(".txt"):
            file_path = os.path.abspath(os.path.join(folder_path, file))
            file_name = os.path.splitext(file)[0]
            numbers = re.findall(r"\d+", file_name)
            if numbers and int(numbers[0]) == number:
                matching_files.append(file_path)
                
    matching_files = sorted(matching_files, key = len)

    return matching_files

def get_text_file_paths(folder_path):
    file_paths = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                file_paths.append(file_path)

    file_paths_series = pd.Series(file_paths)
    return file_paths_series

def search_setting_with_same_number(folder_path, number):
    matching_files = []

    for file in os.listdir(folder_path):
        if not file.endswith(".txt"):
            file_path = os.path.abspath(os.path.join(folder_path, file))
            file_name = os.path.splitext(file)[0]
            numbers = re.findall(r"\d+", file_name)
            if numbers and int(numbers[0]) == number:
                matching_files.append(file_path)
                
    matching_files = sorted(matching_files, key = len)
    return matching_files


def extract_numbers_from_filename(filename):
    numbers = re.findall(r'\d+', filename)
    return [int(num) for num in numbers]

large_diff='green'
default_color='black'
Sub='Fc-Cn-SH'
countertot=0
counter=0
i=0
shortcounter=0
devcount=0
devs=np.linspace(0,7,8)
counter2=np.linspace(0,7,8)
stdavg=np.linspace(0,7,8)
scounts=np.linspace(0,7,8)
shorting=np.linspace(0,7,8)
#Very basic idea
#positive
p5_total = []
p45_total = []
p4_total = []
p35_total = []
p3_total = []
p25_total = []
p2_total = []
p15_total = []
p1_total = []
p05_total = []
#negative
p5_total_neg = []
p45_total_neg = []
p4_total_neg = []
p35_total_neg = []
p3_total_neg = []
p25_total_neg = []
p2_total_neg = []
p15_total_neg = []
p1_total_neg = []
p05_total_neg = []

carbonFull_p1 = [] * 6
carbonFull_p5 = [] * 6
carbonFull_p1_neg = [] * 6
carbonFull_p5_neg = [] * 6
#J0 = np.linspace(0,7,8)
counter2tot = [0] * 4
carbonNumber = 0
#J0tot = [0] * 5
for values in dogs:
    carbo_folder_path= r'Q:\Shared drives\MSE-Thuo Group\Group Server ISU\Zizhi\Data\Data Analysis\New dataset AgTS\Combined'
    values=str(int(values))
    carbo_folder_path=carbo_folder_path + c + 'C' + values
    files_paths=get_text_file_paths(carbo_folder_path)
    nums=[]
    carbon_temp_p1 = []
    carbon_temp_p5 = []
    carbon_temp_p1_neg = []
    carbon_temp_p5_neg = []
    for pathss in files_paths:
        a=extract_numbers_from_filename(pathss)
        if(len(a) != 1):
            nums.append(a[1])
        #nums.append(a[1])
    sorted_numbers=natsorted(nums)
    unique_numbers=list(set(sorted_numbers))
    fresh=[]
    stdcount=0
    for n in range(len(unique_numbers)):
        for m in [unique_numbers[n]]:
            Full = pd.DataFrame()
            TotalDnT = pd.DataFrame()
            result=pd.DataFrame()
            number=int(m)
            matching_files = search_files_with_same_number(carbo_folder_path,number)
            matching_setting = search_setting_with_same_number(carbo_folder_path, number)
            
            fileTXT = findRelatedData(matching_files, matching_setting)
            
            
                
            if not len(matching_files) == 0:
                Full = DataConcat(matching_files)

            if not len(fileTXT) == 0:
                TotalDnT = DataConcat(fileTXT)


    
                
            if Full.empty:
                break
            #if len(time) == 0:
                #break
        
        #result=Full
        #Volts=result['Voltage (V)']
        Abso = Full['Absolute Value of J']
        #J0_temp = []
        '''
        for x in (range(len(Abso))):
            if not(Abso[x] > 1):
                result =  Abso[x] - math.exp(-abs(carbonLen[i]))
                J0_temp.append(result)               
        J0[i] = round(sum(J0_temp) / len(J0_temp),8)
        '''   
            
        #if(len(TotalDnT) > 0):
            #Abso1 = TotalDnT['Absolute Value of J']
        Abso = np.log10(Abso)
        #Abso1 = np.log10(Abso1)
        if any(value > 0 for value in Abso):
            counter += 1
        #shortcounter+=1
        #if any(value > 3 for value in Abso1):
            #countertot += 1
        nl1std=[0] * 10
        nl2std=[0] * 10
        k=0
        newneg=[-0.50,-0.45,-0.40,-0.35,-0.30,-0.25,-0.20,-0.15,-0.10,-0.05]
        newpos=[0.50,0.45,0.40,0.35,0.30,0.25,0.20,0.15,0.10,0.05]
        tot_average=[]
        if not any(value > 0 for value in Abso):
            
            for numpos, numneg in zip(newpos,newneg):
                
                filtered_neg = Full[Full['Voltage (V)'] == numneg]
                
                filtered_pos = Full[Full['Voltage (V)']== numpos]
                new_df = pd.DataFrame()
                new_df_2=pd.DataFrame()
                new_df_2=np.log10(filtered_neg['Absolute Value of J']) #Negative
                new_df=np.log10(filtered_pos['Absolute Value of J']) #Positive
                new_list1=new_df.tolist()
                new_list2=new_df_2.tolist()
                nl1std[k]=np.std(new_list1)
                nl2std[k]=np.std(new_list2)
                if(numpos == 0.5):
                    p5_total.append(new_list1)
                    if( int(values) >= 10 and int(values) <= 15):
                        carbon_temp_p5.append(np.log10(filtered_pos['Absolute Value of J']).tolist())
                elif(numpos == 0.45):
                    p45_total.append(new_list1)
                elif(numpos == 0.4):
                    p4_total.append(new_list1)      
                elif(numpos == 0.35):
                    p35_total.append(new_list1)    
                elif(numpos == 0.3):
                    p3_total.append(new_list1)    
                elif(numpos == 0.25):
                    p25_total.append(new_list1)
                elif(numpos == 0.2):
                    p2_total.append(new_list1)    
                elif(numpos == 0.15):
                    p15_total.append(new_list1)   
                elif(numpos == 0.1):
                    p1_total.append(new_list1)
                    if( int(values) >= 10 and int(values) <= 15):
                        carbon_temp_p1.append(np.log10(filtered_pos['Absolute Value of J']).tolist())
                elif(numpos == 0.05):
                    p05_total.append(new_list1)
                    
                    
                    
                if(numneg == -0.5):
                    p5_total_neg.append(new_list2)
                    if( int(values) >= 10 and int(values) <= 15):
                        carbon_temp_p5_neg.append(np.log10(filtered_neg['Absolute Value of J']).tolist())
                elif(numneg == -0.45):
                    p45_total_neg.append(new_list2)
                elif(numneg == -0.4):
                    p4_total_neg.append(new_list2)      
                elif(numneg == -0.35):
                    p35_total_neg.append(new_list2)    
                elif(numneg == -0.3):
                    p3_total_neg.append(new_list2)    
                elif(numneg == -0.25):
                    p25_total_neg.append(new_list2)
                elif(numneg == -0.2):
                    p2_total_neg.append(new_list2)    
                elif(numneg == -0.15):
                    p15_total_neg.append(new_list2)   
                elif(numneg == -0.1):
                    p1_total_neg.append(new_list2)
                    if( int(values) >= 10 and int(values) <= 15):
                        carbon_temp_p1_neg.append(np.log10(filtered_neg['Absolute Value of J']).tolist())
                elif(numneg == -0.05):
                    p05_total_neg.append(new_list2)


                    
                #else:
                    

                k+=1
                #print(nl1std,nl2std)
            std=0.3
            stdcount+=1
            if any(value > std for value in nl1std) or any(value > std for value in nl2std):
                devcount += 1
            combined_list = nl1std + nl2std
            total_average = sum(combined_list) / len(combined_list)
            fresh.append(total_average)
    scounts[i]=stdcount
    #if(len(fresh) > 0):
    fresh=sum(fresh)/len(fresh)       
    #else:
        #fresh = 1
    stdavg[i]=fresh
    devs[i]=devcount
    counter2[i]=counter
    #shorting[i]=shortcounter
    counter=0
    devcount=0
    shortcounter=0
    i=i+1
    if( int(values) >= 10 and int(values) <= 15):
        carbon_temp_1d_p1 = [n for carbon_temp_1d_p1 in carbon_temp_p1 for n in carbon_temp_1d_p1]
        carbon_temp_1d_p5 = [n for carbon_temp_1d_p5 in carbon_temp_p5 for n in carbon_temp_1d_p5]
        carbon_temp_1d_p1_neg = [n for carbon_temp_1d_p1_neg in carbon_temp_p1_neg for n in carbon_temp_1d_p1_neg]
        carbon_temp_1d_p5_neg = [n for carbon_temp_1d_p5_neg in carbon_temp_p5_neg for n in carbon_temp_1d_p5_neg]
        carbonFull_p1.append(carbon_temp_1d_p1)
        carbonFull_p5.append(carbon_temp_1d_p5)
        carbonFull_p1_neg.append(carbon_temp_1d_p1_neg)
        carbonFull_p5_neg.append(carbon_temp_1d_p5_neg)

#SHIT MOUNTAIN ALERT!!!!!!!!!!!!!!!
#NEED A BETTER WAY TO Simplify the calculation process :(
#positive voltage 0-0.5
skew_pos = [0] * 10
kur_pos = [0] * 10
std_pos = [0] * 10
p5_total_1d = [n for p5_total_1d in p5_total for n in p5_total_1d]
p45_total_1d = [n for p45_total_1d in p45_total for n in p45_total_1d]
p4_total_1d = [n for p4_total_1d in p4_total for n in p4_total_1d]
p35_total_1d = [n for p35_total_1d in p35_total for n in p35_total_1d]
p3_total_1d = [n for p3_total_1d in p3_total for n in p3_total_1d]
p25_total_1d = [n for p25_total_1d in p25_total for n in p25_total_1d]
p2_total_1d = [n for p2_total_1d in p2_total for n in p2_total_1d]
p15_total_1d = [n for p15_total_1d in p15_total for n in p15_total_1d]
p1_total_1d = [n for p1_total_1d in p1_total for n in p1_total_1d]
p05_total_1d = [n for p05_total_1d in p05_total for n in p05_total_1d]

skew_pos[9] = skew(p5_total_1d, axis=0, bias=True)
skew_pos[8] = skew(p45_total_1d, axis=0, bias=True)
skew_pos[7] = skew(p4_total_1d, axis=0, bias=True)
skew_pos[6] = skew(p35_total_1d, axis=0, bias=True)
skew_pos[5] = skew(p3_total_1d, axis=0, bias=True)
skew_pos[4] = skew(p25_total_1d, axis=0, bias=True)
skew_pos[3] = skew(p2_total_1d, axis=0, bias=True)
skew_pos[2] = skew(p15_total_1d, axis=0, bias=True)
skew_pos[1] = skew(p1_total_1d, axis=0, bias=True)
skew_pos[0] = skew(p05_total_1d, axis=0, bias=True)

kur_pos[9] = kurtosis(p5_total_1d, axis=0, bias=True)
kur_pos[8] = kurtosis(p45_total_1d, axis=0, bias=True)
kur_pos[7] = kurtosis(p4_total_1d, axis=0, bias=True)
kur_pos[6] = kurtosis(p35_total_1d, axis=0, bias=True)
kur_pos[5] = kurtosis(p3_total_1d, axis=0, bias=True)
kur_pos[4] = kurtosis(p25_total_1d, axis=0, bias=True)
kur_pos[3] = kurtosis(p2_total_1d, axis=0, bias=True)
kur_pos[2] = kurtosis(p15_total_1d, axis=0, bias=True)
kur_pos[1] = kurtosis(p1_total_1d, axis=0, bias=True)
kur_pos[0] = kurtosis(p05_total_1d, axis=0, bias=True)

std_pos[9] = np.std(p5_total_1d, axis=0)
std_pos[8] = np.std(p45_total_1d, axis=0)
std_pos[7] = np.std(p4_total_1d, axis=0)
std_pos[6] = np.std(p35_total_1d, axis=0)
std_pos[5] = np.std(p3_total_1d, axis=0)
std_pos[4] = np.std(p25_total_1d, axis=0)
std_pos[3] = np.std(p2_total_1d, axis=0)
std_pos[2] = np.std(p15_total_1d, axis=0)
std_pos[1] = np.std(p1_total_1d, axis=0)
std_pos[0] = np.std(p05_total_1d, axis=0)

#negative voltage 0-0.5
skew_neg = [0] * 10
kur_neg = [0] * 10
std_neg = [0] * 10
p5_total_neg_1d = [n for p5_total_neg_1d in p5_total_neg for n in p5_total_neg_1d]
p45_total_neg_1d = [n for p45_total_neg_1d in p45_total_neg for n in p45_total_neg_1d]
p4_total_neg_1d = [n for p4_total_neg_1d in p4_total_neg for n in p4_total_neg_1d]
p35_total_neg_1d = [n for p35_total_neg_1d in p35_total_neg for n in p35_total_neg_1d]
p3_total_neg_1d = [n for p3_total_neg_1d in p3_total_neg for n in p3_total_neg_1d]
p25_total_neg_1d = [n for p25_total_neg_1d in p25_total_neg for n in p25_total_neg_1d]
p2_total_neg_1d = [n for p2_total_neg_1d in p2_total_neg for n in p2_total_neg_1d]
p15_total_neg_1d = [n for p15_total_neg_1d in p15_total_neg for n in p15_total_neg_1d]
p1_total_neg_1d = [n for p1_total_neg_1d in p1_total_neg for n in p1_total_neg_1d]
p05_total_neg_1d = [n for p05_total_neg_1d in p05_total_neg for n in p05_total_neg_1d]

skew_neg[9] = skew(p5_total_neg_1d, axis=0, bias=True)
skew_neg[8] = skew(p45_total_neg_1d, axis=0, bias=True)
skew_neg[7] = skew(p4_total_neg_1d, axis=0, bias=True)
skew_neg[6] = skew(p35_total_neg_1d, axis=0, bias=True)
skew_neg[5] = skew(p3_total_neg_1d, axis=0, bias=True)
skew_neg[4] = skew(p25_total_neg_1d, axis=0, bias=True)
skew_neg[3] = skew(p2_total_neg_1d, axis=0, bias=True)
skew_neg[2] = skew(p15_total_neg_1d, axis=0, bias=True)
skew_neg[1] = skew(p1_total_neg_1d, axis=0, bias=True)
skew_neg[0] = skew(p05_total_neg_1d, axis=0, bias=True)

kur_neg[9] = kurtosis(p5_total_neg_1d, axis=0, bias=True)
kur_neg[8] = kurtosis(p45_total_neg_1d, axis=0, bias=True)
kur_neg[7] = kurtosis(p4_total_neg_1d, axis=0, bias=True)
kur_neg[6] = kurtosis(p35_total_neg_1d, axis=0, bias=True)
kur_neg[5] = kurtosis(p3_total_neg_1d, axis=0, bias=True)
kur_neg[4] = kurtosis(p25_total_neg_1d, axis=0, bias=True)
kur_neg[3] = kurtosis(p2_total_neg_1d, axis=0, bias=True)
kur_neg[2] = kurtosis(p15_total_neg_1d, axis=0, bias=True)
kur_neg[1] = kurtosis(p1_total_neg_1d, axis=0, bias=True)
kur_neg[0] = kurtosis(p05_total_neg_1d, axis=0, bias=True)

std_neg[9] = np.std(p5_total_neg_1d, axis=0)
std_neg[8] = np.std(p45_total_neg_1d, axis=0)
std_neg[7] = np.std(p4_total_neg_1d, axis=0)
std_neg[6] = np.std(p35_total_neg_1d, axis=0)
std_neg[5] = np.std(p3_total_neg_1d, axis=0)
std_neg[4] = np.std(p25_total_neg_1d, axis=0)
std_neg[3] = np.std(p2_total_neg_1d, axis=0)
std_neg[2] = np.std(p15_total_neg_1d, axis=0)
std_neg[1] = np.std(p1_total_neg_1d, axis=0)
std_neg[0] = np.std(p05_total_neg_1d, axis=0)

#Normalized pos and neg data

skew_pos_normalize = [0] * 10
for x in range(len(skew_pos_normalize)):
    skew_pos_normalize[x] = skew_pos[x] - skew_pos[0]    
kur_pos_normalize = [0] * 10
for x in range(len(kur_pos_normalize)):
    kur_pos_normalize[x] = kur_pos[x] - kur_pos[0] 
std_pos_normalize = [0] * 10
for x in range(len(std_pos_normalize)):
    std_pos_normalize[x] = std_pos[x] - std_pos[0] 
skew_neg_normalize = [0] * 10
for x in range(len(skew_neg_normalize)):
    skew_neg_normalize[x] = skew_neg[x] - skew_neg[0]  
kur_neg_normalize = [0] * 10
for x in range(len(kur_neg_normalize)):
    kur_neg_normalize[x] = kur_neg[x] - kur_neg[0]
std_neg_normalize = [0] * 10
for x in range(len(std_neg_normalize)):
    std_neg_normalize[x] = std_neg[x] - std_neg[0]

#carbon length

skew_carbon_p1 = [0] * 6
kur_carbon_p1 = [0] * 6
std_carbon_p1 = [0] * 6

skew_carbon_p5 = [0] * 6
kur_carbon_p5 = [0] * 6
std_carbon_p5 = [0] * 6

skew_carbon_p1_neg = [0] * 6
kur_carbon_p1_neg = [0] * 6
std_carbon_p1_neg = [0] * 6

skew_carbon_p5_neg = [0] * 6
kur_carbon_p5_neg = [0] * 6
std_carbon_p5_neg = [0] * 6
for x in range(len(carbonFull_p1)):
    skew_carbon_p1[x] = skew(carbonFull_p1[x], axis=0, bias=True)
    kur_carbon_p1[x] = kurtosis(carbonFull_p1[x], axis=0, bias=True)
    std_carbon_p1[x] = np.std(carbonFull_p1[x], axis=0)

    skew_carbon_p5[x] = skew(carbonFull_p5[x], axis=0, bias=True)
    kur_carbon_p5[x] = kurtosis(carbonFull_p5[x], axis=0, bias=True)
    std_carbon_p5[x] = np.std(carbonFull_p5[x], axis=0)
    
    skew_carbon_p1_neg[x] = skew(carbonFull_p1_neg[x], axis=0, bias=True)
    kur_carbon_p1_neg[x] = kurtosis(carbonFull_p1_neg[x], axis=0, bias=True)
    std_carbon_p1_neg[x] = np.std(carbonFull_p1_neg[x], axis=0)
    
    skew_carbon_p5_neg[x] = skew(carbonFull_p5_neg[x], axis=0, bias=True)
    kur_carbon_p5_neg[x] = kurtosis(carbonFull_p5_neg[x], axis=0, bias=True)
    std_carbon_p5_neg[x] = np.std(carbonFull_p5_neg[x], axis=0)

#Normalized carbon length
skew_carbon_p1_normalize = [0] * 6
kur_carbon_p1_normalize = [0] * 6
std_carbon_p1_normalize = [0] * 6

skew_carbon_p5_normalize = [0] * 6
kur_carbon_p5_normalize = [0] * 6
std_carbon_p5_normalize = [0] * 6

skew_carbon_p1_neg_normalize = [0] * 6
kur_carbon_p1_neg_normalize = [0] * 6
std_carbon_p1_neg_normalize = [0] * 6

skew_carbon_p5_neg_normalize = [0] * 6
kur_carbon_p5_neg_normalize = [0] * 6
std_carbon_p5_neg_normalize = [0] * 6

for x in range(len(skew_carbon_p1_normalize)):
    skew_carbon_p1_normalize[x] = skew_carbon_p1[x] - skew_carbon_p1[0]
    kur_carbon_p1_normalize[x] = kur_carbon_p1[x] - kur_carbon_p1[0]
    std_carbon_p1_normalize[x] = std_carbon_p1[x] - std_carbon_p1[0]

    skew_carbon_p5_normalize[x] = skew_carbon_p5[x] - skew_carbon_p5[0]
    kur_carbon_p5_normalize[x] = kur_carbon_p5[x] - kur_carbon_p5[0]
    std_carbon_p5_normalize[x] = std_carbon_p5[x] - std_carbon_p5[0]
    
    skew_carbon_p1_neg_normalize[x] = skew_carbon_p1_neg[x] - skew_carbon_p1_neg[0]
    kur_carbon_p1_neg_normalize[x] = kur_carbon_p1_neg[x] - kur_carbon_p1_neg[0]
    std_carbon_p1_neg_normalize[x] = std_carbon_p1_neg[x] - std_carbon_p1_neg[0]
    
    skew_carbon_p5_neg_normalize[x] = skew_carbon_p5_neg[x] - skew_carbon_p5_neg[0]
    kur_carbon_p5_neg_normalize[x] = kur_carbon_p5_neg[x] - kur_carbon_p5_neg[0]
    std_carbon_p5_neg_normalize[x] = std_carbon_p5_neg[x] - std_carbon_p5_neg[0]

def group_files_by_scfc_and_spot(file_paths):
    
    #for sc#fc r"sc(\d+)fc\\(\d+)"
    pattern = r"C(\d+)\\(\d+)" # Change if dataset format changes - current (sc15fc/spot 1)

    grouped_files = {}

    for file_path in file_paths:
        match = re.search(pattern, file_path)        
        if match:
            scfc = match.group(1)
            spot = match.group(2)
            key = f"C{scfc}" # Change as well if dataset format changes - if just number then can change whole apparatus
            if key not in grouped_files:
                grouped_files[key] = {}
            if spot not in grouped_files[key]:
                grouped_files[key][spot] = []
            grouped_files[key][spot].append(file_path)

    return grouped_files

#Export to Excel
'''
result_01 = pd.DataFrame(carbonFull_p1)
result_05 = pd.DataFrame(carbonFull_p5)
result_01_neg = pd.DataFrame(carbonFull_p1_neg)
result_05_neg = pd.DataFrame(carbonFull_p5_neg)

with pd.ExcelWriter(r'Q:\Shared drives\MSE-Thuo Group\Group Server ISU\Zizhi\Data\Data Analysis\Captured Data\Ag_2.xlsx', engine='xlsxwriter') as writer:
    result_01.to_excel(writer,sheet_name='0.1')
    result_05.to_excel(writer,sheet_name='0.5')
    result_01_neg.to_excel(writer,sheet_name='-0.1')
    result_05_neg.to_excel(writer,sheet_name='-0.5')
   
    
result_01_std = pd.DataFrame(std_carbon_p1)
result_05_std = pd.DataFrame(std_carbon_p5)
result_01_neg_std = pd.DataFrame(std_carbon_p1_neg)
result_05_neg_std = pd.DataFrame(std_carbon_p5_neg)
  
with pd.ExcelWriter(r'Q:\Shared drives\MSE-Thuo Group\Group Server ISU\Zizhi\Data\Data Analysis\Captured Data\Ag__std_2.xlsx', engine='xlsxwriter') as writer:
    result_01_std.to_excel(writer,sheet_name='0.1')
    result_05_std.to_excel(writer,sheet_name='0.5')
    result_01_neg_std.to_excel(writer,sheet_name='-0.1')
    result_05_neg_std.to_excel(writer,sheet_name='-0.5')
'''


voltage_label = ['0.05','0.10','0.15','0.20','0.25','0.30','0.35','0.40','0.45','0.50']

'''
Skewness Positive
'''
fig, ax1 = plt.subplots(figsize=(20,12),dpi = 300)

ax1.set_xlabel('V', fontsize=40)
ax1.set_ylabel(u'$ΔS_{average}$', color='red',fontsize=40)

ax1.scatter(voltage_label, skew_pos_normalize, color='red',s=500)
ax1.tick_params(axis='x',labelsize=40)
ax1.tick_params(axis='y', labelcolor='red',labelsize=40)

plt.tight_layout()
plt.show()


'''
Kurtosis Positive
'''
fig, ax1 = plt.subplots(figsize=(20,12),dpi = 300)

ax1.set_xlabel('V', fontsize=40)
ax1.set_ylabel(u'$ΔK_{average}$', color='red',fontsize=40)

ax1.scatter(voltage_label, kur_pos_normalize, color='red',s=500)
ax1.tick_params(axis='x',labelsize=40)
ax1.tick_params(axis='y', labelcolor='red',labelsize=40)

plt.tight_layout()
plt.show()

'''
Std Positive
'''
fig, ax1 = plt.subplots(figsize=(20,12),dpi = 300)

ax1.set_xlabel('V', fontsize=40)
ax1.set_ylabel(u'$Δ\sigma_{average}$', color='red',fontsize=40)

ax1.scatter(voltage_label, std_pos_normalize, color='red',s=500)
ax1.tick_params(axis='x',labelsize=40)
ax1.tick_params(axis='y', labelcolor='red',labelsize=40)

plt.tight_layout()
plt.show()


voltage_label_neg = ['-0.05','-0.10','-0.15','-0.20','-0.25','-0.30','-0.35','-0.40','-0.45','-0.50']

'''
Skewness Negative
'''
fig, ax1 = plt.subplots(figsize=(20,12),dpi = 300)

ax1.set_xlabel('V', fontsize=40)
ax1.set_ylabel(u'$ΔS_{average}$', color='red',fontsize=40)

ax1.scatter(voltage_label_neg, skew_neg_normalize, color='red',s=500)
ax1.tick_params(axis='x',labelsize=40)
ax1.tick_params(axis='y', labelcolor='red',labelsize=40)

plt.tight_layout()
plt.show()


'''
Kurtosis Negative
'''
fig, ax1 = plt.subplots(figsize=(20,12),dpi = 300)

ax1.set_xlabel('V', fontsize=40)
ax1.set_ylabel(u'$ΔK_{average}$', color='red',fontsize=40)

ax1.scatter(voltage_label_neg, kur_neg_normalize, color='red',s=500)
ax1.tick_params(axis='x',labelsize=40)
ax1.tick_params(axis='y', labelcolor='red',labelsize=40)

plt.tight_layout()
plt.show()

'''
Std Negative
'''
fig, ax1 = plt.subplots(figsize=(20,12),dpi = 300)

ax1.set_xlabel('V', fontsize=40)
ax1.set_ylabel(u'$Δ\sigma_{average}$', color='red',fontsize=40)

ax1.scatter(voltage_label_neg, std_neg_normalize, color='red',s=500)
ax1.tick_params(axis='x',labelsize=40)
ax1.tick_params(axis='y', labelcolor='red',labelsize=40)

plt.tight_layout()
plt.show()


carbon_length = ['C10','C11','C12','C13','C14','C15']

'''
Skewness Carbon Length
'''
fig, ax1 = plt.subplots(figsize=(20,12),dpi = 300)

ax1.set_xlabel('Carbon Length', fontsize=40)
ax1.set_ylabel(u'$ΔS_{average}$', color='red',fontsize=40)

ax1.scatter(carbon_length, skew_carbon_p1_normalize, marker='o',color='red',s=500)
ax1.scatter(carbon_length, skew_carbon_p5_normalize, marker='s',color='blue',s=500)
ax1.scatter(carbon_length, skew_carbon_p1_neg_normalize, marker='^',color='green',s=500)
ax1.scatter(carbon_length, skew_carbon_p5_neg_normalize, marker='*',color='black',s=500)
ax1.legend(["0.1V", "0.5V",'-0.1V','-0.5V'],loc='best',fontsize=40)
ax1.tick_params(axis='x',labelsize=40)
ax1.tick_params(axis='y', labelcolor='red',labelsize=40)

plt.tight_layout()
plt.show()


'''
Kurtosis Carbon Length
'''
fig, ax1 = plt.subplots(figsize=(20,12),dpi = 300)

ax1.set_xlabel('Carbon Length', fontsize=40)
ax1.set_ylabel(u'$ΔK_{average}$', color='red',fontsize=40)

ax1.scatter(carbon_length, kur_carbon_p1_normalize, marker='o',color='red',s=500)
ax1.scatter(carbon_length, kur_carbon_p5_normalize, marker='s',color='blue',s=500)
ax1.scatter(carbon_length, kur_carbon_p1_neg_normalize, marker='^',color='green',s=500)
ax1.scatter(carbon_length, kur_carbon_p5_neg_normalize, marker='*',color='black',s=500)
ax1.legend(["0.1V", "0.5V",'-0.1V','-0.5V'],loc='best',fontsize=40)
ax1.tick_params(axis='x',labelsize=40)
ax1.tick_params(axis='y', labelcolor='red',labelsize=40)

plt.tight_layout()
plt.show()

'''
Std Carbon Length
'''
fig, ax1 = plt.subplots(figsize=(20,12),dpi = 300)

ax1.set_xlabel('Carbon Length', fontsize=40)
ax1.set_ylabel(u'$Δ\sigma_{average}$', color='red',fontsize=40)

ax1.scatter(carbon_length, std_carbon_p1_normalize, marker='o',color='red',s=500)
ax1.scatter(carbon_length, std_carbon_p5_normalize, marker='s',color='blue',s=500)
ax1.scatter(carbon_length, std_carbon_p1_neg_normalize, marker='^',color='green',s=500)
ax1.scatter(carbon_length, std_carbon_p5_neg_normalize, marker='*',color='black',s=500)
ax1.legend(["0.1V", "0.5V",'-0.1V','-0.5V'],loc='best',fontsize=40)
ax1.tick_params(axis='x',labelsize=40)
ax1.tick_params(axis='y', labelcolor='red',labelsize=40)

plt.tight_layout()
plt.show()



'''
'''
#3D plots
'''

'''
#Postivite

'''
pos_volt = ['0.05','0.1','0.15','0.2','0.25','0.3','0.35','0.4','0.45','0.5']

carbonNum = ['C9','C10','C11','C12','C13','C14','C15']
#skew_pos_changed = skew_pos[3:9]

'''
#Skewness
'''
list_temp = []
for x in range(len(skew_carbon)):
    z = []
    for y in range(len(skew_pos)):
        z.append(skew_pos[y] * skew_carbon[x])
    list_temp.append(z)
data3d = np.array(list_temp)
fig, ax = plt.subplots(figsize=(40,25),dpi = 400, subplot_kw={'projection': '3d'})
for i in range(data3d.shape[0]):
    ax.plot3D(np.repeat(i, data3d.shape[1]),np.arange(data3d.shape[1]),
              data3d[i, :])
    
ax.set_xticklabels(carbonNum) #Set label will ignore first element in list, do not know why
#ax.set_xlabel('\n\nCarbon Number',fontsize = 40)
ax.set_yticklabels(pos_volt,rotation = 45) #Set label will ignore first element in list, do not know why

ax.tick_params(axis='z', pad=30)
#ax.set_ylabel('\n\n\n\nVoltage',fontsize = 40)
#ax.set_zlabel('\nSkewness',fontsize = 40)
#ax.set_zticks([0,5,10])
ax.tick_params(axis='x', labelcolor='blue',labelsize = 40)
ax.tick_params(axis='y', labelcolor='red',labelsize = 40)
ax.tick_params(axis='z', labelcolor='black',labelsize = 40)
ax.view_init(azim=45, elev=20)
ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
# make the grid lines transparent
ax.xaxis._axinfo["grid"]['color'] =  (1,1,1,0)
ax.yaxis._axinfo["grid"]['color'] =  (1,1,1,0)
ax.zaxis._axinfo["grid"]['color'] =  (1,1,1,0)
#plt.tight_layout()
plt.show()

'''
#Kurtosis
'''
list_temp = []
for x in range(len(kur_carbon)):
    z = []
    for y in range(len(kur_pos)):
        z.append(kur_pos[y] * kur_carbon[x])
    list_temp.append(z)
data3d = np.array(list_temp)
fig, ax = plt.subplots(figsize=(40,25),dpi = 400, subplot_kw={'projection': '3d'})
for i in range(data3d.shape[0]):
    ax.plot3D(np.repeat(i, data3d.shape[1]),np.arange(data3d.shape[1]),
              data3d[i, :])
    
ax.set_xticklabels(carbonNum) #Set label will ignore first element in list, do not know why
ax.set_yticklabels(pos_volt,rotation = 45) #Set label will ignore first element in list, do not know why
ax.tick_params(axis='z', pad=30)

ax.tick_params(axis='x', labelcolor='blue',labelsize = 40)
ax.tick_params(axis='y', labelcolor='red',labelsize = 40)
ax.tick_params(axis='z', labelcolor='black',labelsize = 40)
ax.view_init(azim=45, elev=20)
ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
# make the grid lines transparent
ax.xaxis._axinfo["grid"]['color'] =  (1,1,1,0)
ax.yaxis._axinfo["grid"]['color'] =  (1,1,1,0)
ax.zaxis._axinfo["grid"]['color'] =  (1,1,1,0)
plt.show()

'''
#STD
'''
list_temp = []
for x in range(len(std_carbon)):
    z = []
    for y in range(len(std_pos)):
        z.append(std_pos[y] * std_carbon[x])
    list_temp.append(z)
data3d = np.array(list_temp)
fig, ax = plt.subplots(figsize=(40,25),dpi = 400, subplot_kw={'projection': '3d'})
for i in range(data3d.shape[0]):
    ax.plot3D(np.repeat(i, data3d.shape[1]),np.arange(data3d.shape[1]),
              data3d[i, :])
    
ax.set_xticklabels(carbonNum) #Set label will ignore first element in list, do not know why
ax.set_yticklabels(pos_volt,rotation = 45) #Set label will ignore first element in list, do not know why
ax.tick_params(axis='z', pad=30)

ax.tick_params(axis='x', labelcolor='blue',labelsize = 40)
ax.tick_params(axis='y', labelcolor='red',labelsize = 40)
ax.tick_params(axis='z', labelcolor='black',labelsize = 40)
ax.view_init(azim=45, elev=20)
ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
# make the grid lines transparent
ax.xaxis._axinfo["grid"]['color'] =  (1,1,1,0)
ax.yaxis._axinfo["grid"]['color'] =  (1,1,1,0)
ax.zaxis._axinfo["grid"]['color'] =  (1,1,1,0)
plt.show()

'''
#Negative
'''
neg_volt = ['-0.05','-0.1','-0.15','-0.2','-0.25','-0.3','-0.35','-0.4','-0.45','-0.5']


'''
#Skewness
'''
list_temp = []
for x in range(len(skew_carbon)):
    z = []
    for y in range(len(skew_neg)):
        z.append(skew_neg[y] * skew_carbon[x])
    list_temp.append(z)
data3d = np.array(list_temp)
fig, ax = plt.subplots(figsize=(40,25),dpi = 400, subplot_kw={'projection': '3d'})
for i in range(data3d.shape[0]):
    ax.plot3D(np.repeat(i, data3d.shape[1]),np.arange(data3d.shape[1]),
              data3d[i, :])
    
ax.set_xticklabels(carbonNum) #Set label will ignore first element in list, do not know why
#ax.set_xlabel('\n\nCarbon Number',fontsize = 40)
ax.set_yticklabels(neg_volt,rotation = 45) #Set label will ignore first element in list, do not know why

ax.tick_params(axis='z', pad=40)
#ax.set_ylabel('\n\n\n\nVoltage',fontsize = 40)
#ax.set_zlabel('\nSkewness',fontsize = 40)
#ax.set_zticks([0,5,10])
ax.tick_params(axis='x', labelcolor='blue',labelsize = 40)
ax.tick_params(axis='y', labelcolor='red',labelsize = 40)
ax.tick_params(axis='z', labelcolor='black',labelsize = 40)
ax.view_init(azim=45, elev=20)
ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
# make the grid lines transparent
ax.xaxis._axinfo["grid"]['color'] =  (1,1,1,0)
ax.yaxis._axinfo["grid"]['color'] =  (1,1,1,0)
ax.zaxis._axinfo["grid"]['color'] =  (1,1,1,0)
#plt.tight_layout()
plt.show()

'''
#Kurtosis
'''
list_temp = []
for x in range(len(kur_carbon)):
    z = []
    for y in range(len(kur_neg)):
        z.append(kur_neg[y] * kur_carbon[x])
    list_temp.append(z)
data3d = np.array(list_temp)
fig, ax = plt.subplots(figsize=(40,25),dpi = 400, subplot_kw={'projection': '3d'})
for i in range(data3d.shape[0]):
    ax.plot3D(np.repeat(i, data3d.shape[1]),np.arange(data3d.shape[1]),
              data3d[i, :])
    
ax.set_xticklabels(carbonNum) #Set label will ignore first element in list, do not know why
ax.set_yticklabels(neg_volt,rotation = 45) #Set label will ignore first element in list, do not know why
ax.tick_params(axis='z', pad=30)

ax.tick_params(axis='x', labelcolor='blue',labelsize = 40)
ax.tick_params(axis='y', labelcolor='red',labelsize = 40)
ax.tick_params(axis='z', labelcolor='black',labelsize = 40)
ax.view_init(azim=45, elev=20)
ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
# make the grid lines transparent
ax.xaxis._axinfo["grid"]['color'] =  (1,1,1,0)
ax.yaxis._axinfo["grid"]['color'] =  (1,1,1,0)
ax.zaxis._axinfo["grid"]['color'] =  (1,1,1,0)
plt.show()

'''
#STD
'''
list_temp = []
for x in range(len(std_carbon)):
    z = []
    for y in range(len(std_neg)):
        z.append(std_neg[y] * std_carbon[x])
    list_temp.append(z)
data3d = np.array(list_temp)
fig, ax = plt.subplots(figsize=(40,25),dpi = 400, subplot_kw={'projection': '3d'})
for i in range(data3d.shape[0]):
    ax.plot3D(np.repeat(i, data3d.shape[1]),np.arange(data3d.shape[1]),
              data3d[i, :])
    
ax.set_xticklabels(carbonNum) #Set label will ignore first element in list, do not know why
ax.set_yticklabels(neg_volt,rotation = 45) #Set label will ignore first element in list, do not know why
ax.tick_params(axis='z', pad=30)

ax.tick_params(axis='x', labelcolor='blue',labelsize = 40)
ax.tick_params(axis='y', labelcolor='red',labelsize = 40)
ax.tick_params(axis='z', labelcolor='black',labelsize = 40)
ax.view_init(azim=45, elev=20)
ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
# make the grid lines transparent
ax.xaxis._axinfo["grid"]['color'] =  (1,1,1,0)
ax.yaxis._axinfo["grid"]['color'] =  (1,1,1,0)
ax.zaxis._axinfo["grid"]['color'] =  (1,1,1,0)
plt.show()
'''