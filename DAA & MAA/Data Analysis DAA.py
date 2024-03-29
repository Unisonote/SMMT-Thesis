# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 20:17:26 2023

@author: 15253
"""


# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 00:32:08 2023

@author: zzz
"""

# -*- coding: utf-8 -*-
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

sc='sc'
fc='fc'
c=chr(92)
carbo_folder_path= r'E:\SMMT Group\DAA'
#carbonLen = [9,11,13,15]
dogs=np.linspace(0,10,11)
timePeriod = np.linspace(0,3,4)
spots_with_values_greater_than_30 = 0
spots_with_values_greater_than_31 = 0
spots_with_values_greater_than_32 = 0
spots_with_values_greater_than_33 = 0
spots_with_values_greater_than_34 = 0
spots_with_values_greater_than_3_0 = 0
spots_with_values_greater_than_3_1 = 0
spots_with_values_greater_than_3_2 = 0
spots_with_values_greater_than_3_3 = 0
spots_with_values_greater_than_3_4 = 0


#These variable are used in method getDuraionTime


fileDnT = []  #filename that contains data and time 
morning = []  #6am - 10am
noon = []     #10am - 2pm
afternoon = []  #2pm - 6pm
evening = []   #6pm - 10pm
night=[] #10pm-6am
spring = [] #3/1-5/31
summer = [] #6/1-8/31
autumn = [] #9/1-11/30
winter = [] #12/1-2/28(29)

est_morning = []  #6am - 10am
est_noon = []     #10am - 2pm
est_afternoon = []  #2pm - 6pm
est_evening = []   #6pm - 10pm
est_night=[] #10pm-6am
est_spring = [] #3/1-5/31
est_summer = [] #6/1-8/31
est_autumn = [] #9/1-11/30
est_winter = [] #12/1-2/28(29)



def gaussian(x, A, B):
   return A*np.exp(-1*B*x**2)     

def parabolic(x, a, b, c):
    return a*x**2 + b*x + c         

def parabola(t, *p): 
    a, b, c, d = p
    y = np.zeros(t.shape)
    indices = np.abs(t) < b
    y[indices] = (a*(1-(((t[indices]-c)/b)**2)) + d)
    return y                                                                                                                            

'''
Get duration for the selected spot
'''
def getDate(Series):
    
    date = []
    dateChangeFormat = []
    unique_date = []
    
    '''
    Get experiment date and time from input data set
    '''
    for file in Series:
        f = open(file)
    
        for lines in f : 
            if(lines[0:3] == 'Mon' 
               or lines[0:3] == 'Tue' 
               or lines[0:3] == 'Wed' 
               or lines[0:3] == 'Thu' 
               or lines[0:3] == 'Fri' 
               or lines[0:3] == 'Sat' 
               or lines[0:3] == 'Sun') :
                if(len(date) == 0):
                    date.append(lines[0:len(lines)-1])
                    
                else:             
                    if(lines[0:len(lines)-1] != date[0]):
                        if(len(date) < 2):
                            date.append('NaN')
                        date[1] = lines[0:len(lines)-1]
                        
            try:
                lineindex = lines.index('-')
            except(ValueError):
                lineindex = 0
            if(lineindex):
                if(lines[0:lines.index('-')] == 'September'):
                   dateChangeFormat.append(' 20' + lines[-3:-1] + '-09-' +  lines[lines.index('-') + 1 : lines.index('-') + 3])
                elif(lines[0:lines.index('-')] == 'October'):
                   dateChangeFormat.append(' 20' + lines[-3:-1] + '-10-' +  lines[lines.index('-') + 1 : lines.index('-') + 3])
                elif(lines[0:lines.index('-')] == 'March'):
                   dateChangeFormat.append(' 20' + lines[-3:-1] + '-03-' +  lines[lines.index('-') + 1 : lines.index('-') + 3])
                elif(lines[0:lines.index('-')] == 'January'):
                   dateChangeFormat.append(' 20' + lines[-3:-1] + '-09-' +  lines[lines.index('-') + 1 : lines.index('-') + 3])
                elif(lines[0:lines.index('-')] == 'December'):
                   dateChangeFormat.append(' 20' + lines[-3:-1] + '-12-' +  lines[lines.index('-') + 1 : lines.index('-') + 3])
               
           
                
 
        '''
        Change the format of date
        '''
        for i in range(len(date)):
            commaPos = date[i].index(',') + 2
            if((date[i][commaPos:commaPos + 3]) == 'Jan'):
                dateChangeFormat.append('01-' + date[i][(commaPos + 8):])
            elif((date[i][commaPos:commaPos + 3]) == 'Feb'):
                dateChangeFormat.append('02-' + date[i][(commaPos + 9):])
            elif((date[i][commaPos:commaPos + 3]) == 'Mar'):
                dateChangeFormat.append('03-' + date[i][(commaPos + 6):])
            elif((date[i][commaPos:commaPos + 3]) == 'Apr'):
                dateChangeFormat.append('04-' + date[i][(commaPos + 6):])
            elif((date[i][commaPos:commaPos + 3]) == 'May'):
                dateChangeFormat.append('05-' + date[i][(commaPos + 4):])
            elif((date[i][commaPos:commaPos + 3]) == 'Jun'):
                dateChangeFormat.append('06-' + date[i][(commaPos + 5):])
            elif((date[i][commaPos:commaPos + 3]) == 'Jul'):
                dateChangeFormat.append('07-' + date[i][(commaPos + 5):])
            elif((date[i][commaPos:commaPos + 3]) == 'Aug'):
                dateChangeFormat.append('08-' + date[i][(commaPos + 7):])
            elif((date[i][commaPos:commaPos + 3]) == 'Sep'):
                dateChangeFormat.append('09-' + date[i][(commaPos + 10):])
            elif((date[i][commaPos:commaPos + 3]) == 'Oct'):
                dateChangeFormat.append('10-' + date[i][(commaPos + 8):])
            elif((date[i][commaPos:commaPos + 3]) == 'Nov'):
                dateChangeFormat.append('11-' + date[i][(commaPos + 9):])
            elif((date[i][commaPos:commaPos + 3]) == 'Dec'):
                dateChangeFormat.append('12-' + date[i][(commaPos + 9):])
        for i in range(len(dateChangeFormat)):
            dateChangeFormat[i].strip(" ")
            for j in range(len(dateChangeFormat[i])):
                if(dateChangeFormat[i][j] == ','):
                    dateChangeFormat[i] = (dateChangeFormat[i][(j + 1):] + '-' + dateChangeFormat[i][:j])
  
            if not dateChangeFormat[i][1:] in unique_date:
                
                unique_date.append(dateChangeFormat[i][1:])

       
    return unique_date
#Get duration for the selected spot

def getExperienceTime(Series):
    
    #Get experiment date and time from input data set
    
    time = []
    currentLength = 0
    
    for file in Series:
        f = open(file)
        count = 0
        for lines in f :
            
            if(lines[0].isnumeric()) :
                time.append(lines[0:-1])               
                count += 1

        if(count > 1):

            time[currentLength] = time[-1]

            for i in range(count):                
                if(len(time) > currentLength + 1):                   
                    del time[- 1]

                    
        currentLength += 1
        
    return time
        
def findRelatedData(filename1, filename2): #Finding data file with _data.txt as spot and date filenames are as follows: spot 1 scan 1-20 vs spot 1 scan 1-20_data.txt
    
    fileTXT = []
    
    for file in filename2:
        if(file[-1] == ')'):
            temp_str = file[-4:]
            fileM = file[:-4] + '_data' + temp_str + '.txt'
        else:
            fileM = file + '_data.txt'
        if fileM in filename1:
            fileDnT.append(file)
            fileTXT.append(fileM)
           
    return fileTXT
           

def findTimePeriod(file,time): # finding time in file related and binning them into premade bins (above)
        for index in range(len(time)):
            if(time[index][len(time[index]) - 2 : len(time[index])] == "AM"): # starting with AM times - 
                hour = int(time[index][0:time[index].index(':')])
                if hour < 10 and hour >= 6:
                    morning.append(file[index])
                elif hour == 12:
                    night.append(file[index])
                elif hour < 6:
                    night.append(file[index])
                else:
                    noon.append(file[index])
                
            else:
                hour = int(time[index][0:time[index].index(':')])
                if  hour < 2:
                    noon.append(file[index])
                elif  hour ==12:
                    noon.append(file[index])
                elif hour  >= 2 and hour  < 6:
                    afternoon.append(file[index])
                elif hour  >= 6 and hour  <10:
                    evening.append(file[index])
                else:
                    night.append(file[index])

def findSeasons(file,date):
    if(date[0][5:6] == '1'):
        if(date[0][6:7] == '1' or date[0][6:7] == '0'):
            for index in range(len(file)):
                autumn.append(file[index])
        elif(date[0][6:7] == '2'):
            for index in range(len(file)):
                winter.append(file[index])
    elif(date[0][6:7] == '1' or date[0][6:7] == '2'):
        for index in range(len(file)):
            winter.append(file[index])
    elif(date[0][6:7] == '3' or date[0][6:7] == '4' or date[0][6:7] == '5'):
        for index in range(len(file)):
            spring.append(file[index])
    elif(date[0][6:7] == '6' or date[0][6:7] == '7' or date[0][6:7] == '8'):
        for index in range(len(file)):
            summer.append(file[index])
    elif(date[0][6:7] == '9'):
        for index in range(len(file)):
            autumn.append(file[index])
    
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
devs=np.linspace(0,10,11)
counter2=np.linspace(0,10,11)
stdavg=np.linspace(0,10,11)
scounts=np.linspace(0,10,11)
shorting=np.linspace(0,10,11)
#J0 = np.linspace(0,7,8)
counter2tot = [0] * 4
seasonCounter = [0] * 4
#J0tot = [0] * 5
for values in dogs:
    carbo_folder_path= r'E:\SMMT Group\DAA'
    values=str(int(values))
    carbo_folder_path=carbo_folder_path + c + 'C' + values
    files_paths=get_text_file_paths(carbo_folder_path)
    nums=[]
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
            if not len(fileDnT) == 0: 
                time = getExperienceTime(fileDnT)
                date = getDate(fileDnT)

                fileDnT = []
            if not len(fileTXT) == 0:
                TotalDnT = DataConcat(fileTXT)
                findTimePeriod(fileTXT,time)
                findSeasons(fileTXT,date)
            

    
                
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
        shortcounter+=1
        #if any(value > 3 for value in Abso1):
            #countertot += 1
        nl1std=[0] * 20
        nl2std=[0] * 20
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
                new_df_2['Negative']=np.log10(filtered_neg['Absolute Value of J'])
                new_df['Positive']=np.log10(filtered_pos['Absolute Value of J'])
                new_list1=new_df['Positive'].tolist()
                new_list2=new_df_2['Negative'].tolist()
                nl1std[k]=np.std(new_list1)
                nl2std[k]=np.std(new_list2)
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
    fresh=sum(fresh)/len(fresh)
    stdavg[i]=fresh
    devs[i]=devcount
    counter2[i]=counter
    shorting[i]=shortcounter
    counter=0
    devcount=0
    shortcounter=0
    i=i+1
#print(noon)

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

total_spots_time = [0]*4
total_spots_seasons = [0]*4
std_time = [0] * 4
std_season = [0] * 4
'''
if not(len(morning) == 0):
    morning=group_files_by_scfc_and_spot(morning)
    spots_with_values_greater_than_3_0 = 0
    total_spots=0
    for scfc_line, spot_data in morning.items():
        for spot_number, file_paths in spot_data.items():
            repeat = 0
            for x in range(len(file_paths)):
                if(file_paths[x][-5] == ')'):                   
                    repeat = int(file_paths[x][-6])
            if(repeat == 0):
                total_spots+=1
            else:
                total_spots+=repeat
            concatenated_data = DataConcat(file_paths)
            

            if any(np.log10(concatenated_data['Absolute Value of J']) > 3):
                spots_with_values_greater_than_3_0 += 1

    #print(f"Total Spots with Values > 3: {spots_with_values_greater_than_3_1}")
    if total_spots > 0:
        spots_with_values_greater_than_30 = spots_with_values_greater_than_3_0 / total_spots * 100
        total_spots_time[0] = total_spots
        #print(total_spots)
        counter2tot[0] = spots_with_values_greater_than_30
    countertot = 0
else:
    counter2tot[0] = -100
'''
if not(len(noon) == 0):
    noon=group_files_by_scfc_and_spot(noon)
    spots_with_values_greater_than_3_1 = 0
    total_spots=0
    for scfc_line, spot_data in noon.items():
        #total_spots += len(spot_data)
        for spot_number, file_paths in spot_data.items():
            #total_spots += len(file_paths)

            repeat = 0
            for x in range(len(file_paths)):
                if(file_paths[x][-5] == ')') and (int(file_paths[x][-6]) > repeat):                   
                    repeat = int(file_paths[x][-6])
            if(repeat == 0):
                total_spots+=1
            else:
                total_spots+=repeat


            for x in range(len(file_paths)):
                concatenated_data = DataConcat(file_paths)
            
            
            if any(np.log10(concatenated_data['Absolute Value of J']) > 0):
                spots_with_values_greater_than_3_1 += 1
                est_noon.append(1/len(file_paths))
            else:
                est_noon.append(0)

    #print(f"Total Spots with Values > 3: {spots_with_values_greater_than_3_1}")
    if total_spots > 0:
        spots_with_values_greater_than_31 = spots_with_values_greater_than_3_1 / total_spots * 100
        total_spots_time[0] = total_spots
        #print(total_spots)
        counter2tot[0] = spots_with_values_greater_than_31
    #countertot = 0
    if total_spots > 10:
        std_noon = []
        for scfc_line, spot_data in noon.items():
            each_spots = len(spot_data)
            for spot_number, file_paths in spot_data.items():
                std_temp = 0
                #each_spots = len(file_paths)
                concatenated_data = DataConcat(file_paths)
                if any(np.log10(concatenated_data['Absolute Value of J']) > 0):
                    std_temp += 1
                
                std_noon.append(std_temp/each_spots*100)
        deviations = [(x - spots_with_values_greater_than_31) ** 2 for x in std_noon]
        variance = sum(deviations) / total_spots
        std_time[0] = math.sqrt(variance)
    else:
        std_time[0] = -1
                
else:
    counter2tot[0] = -100

if not(len(afternoon) == 0):
    afternoon=group_files_by_scfc_and_spot(afternoon)
    spots_with_values_greater_than_3_2 = 0
    total_spots=0
    #print(afternoon)
    for scfc_line, spot_data in afternoon.items():
        #total_spots += len(spot_data)
        n = 0
        for spot_number, file_paths in spot_data.items():
            #total_spots += len(file_paths)
            repeat = 0
            for x in range(len(file_paths)):
                if(file_paths[x][-5] == ')') and (int(file_paths[x][-6]) > repeat):                   
                    repeat = int(file_paths[x][-6])
            if(repeat == 0):
                total_spots+=1
            else:
                total_spots+=repeat
            
            concatenated_data = DataConcat(file_paths)
            
            if any(np.log10(concatenated_data['Absolute Value of J']) > 0):
                spots_with_values_greater_than_3_2 += 1
            
                est_afternoon.append(1/len(file_paths))
            else:
                est_afternoon.append(0)
    #print(f"Total Spots with Values > 3: {spots_with_values_greater_than_3_2}")
    if total_spots > 0:
        spots_with_values_greater_than_32 = spots_with_values_greater_than_3_2 / total_spots * 100
        #print(total_spots)
        total_spots_time[1] = total_spots
        counter2tot[1] = spots_with_values_greater_than_32
    #countertot = 0
    if total_spots > 10:
        std_afternoon = []
        for scfc_line, spot_data in afternoon.items():
            each_spots = len(spot_data)
            for spot_number, file_paths in spot_data.items():
                std_temp = 0
                #each_spots = len(file_paths)
                concatenated_data = DataConcat(file_paths)
                if any(np.log10(concatenated_data['Absolute Value of J']) > 0):
                    std_temp += 1
                std_afternoon.append(std_temp/each_spots*100)
        deviations = [(x - spots_with_values_greater_than_32) ** 2 for x in std_afternoon]
        variance = sum(deviations) / total_spots
        std_time[1] = math.sqrt(variance)
    else:
        std_time[1] = -1
else:
    counter2tot[1] = -100
    
if not(len(evening) == 0):
    evening=group_files_by_scfc_and_spot(evening)
    spots_with_values_greater_than_3_3 = 0
    total_spots=0
    #print(afternoon)
    for scfc_line, spot_data in evening.items():
        #total_spots += len(spot_data)
        for spot_number, file_paths in spot_data.items():
            #total_spots += len(file_paths)

            repeat = 0
            for x in range(len(file_paths)):
                if(file_paths[x][-5] == ')') and (int(file_paths[x][-6]) > repeat):                   
                    repeat = int(file_paths[x][-6])
            if(repeat == 0):
                total_spots+=1
            else:
                total_spots+=repeat

            concatenated_data = DataConcat(file_paths)
            
            if any(np.log10(concatenated_data['Absolute Value of J']) > 0):
                spots_with_values_greater_than_3_3 += 1
                est_evening.append(1/len(file_paths))
            else:
                est_evening.append(0)

    #print(f"Total Spots with Values > 3: {spots_with_values_greater_than_3_2}")
    if total_spots > 0:
        spots_with_values_greater_than_33 = spots_with_values_greater_than_3_3 / total_spots * 100
        #print(total_spots)
        total_spots_time[2] = total_spots
        counter2tot[2] = spots_with_values_greater_than_33
    #countertot = 0
    if total_spots > 10:
        std_evening = []
        for scfc_line, spot_data in evening.items():
            each_spots = len(spot_data)            
            for spot_number, file_paths in spot_data.items():
                std_temp = 0
                #each_spots = len(file_paths)
                concatenated_data = DataConcat(file_paths)
                if any(np.log10(concatenated_data['Absolute Value of J']) > 0):
                    std_temp += 1
                std_evening.append(std_temp/each_spots*100)
        deviations = [(x - spots_with_values_greater_than_33) ** 2 for x in std_evening]
        variance = sum(deviations) / total_spots
        std_time[2] = math.sqrt(variance)
    else:
        std_time[2] = -1
else:
    counter2tot[2] = -100    
 
if not(len(night) == 0):
    night=group_files_by_scfc_and_spot(night)
    spots_with_values_greater_than_3_4 = 0
    total_spots=0
    for scfc_line, spot_data in night.items():
        #total_spots += len(spot_data)
        for spot_number, file_paths in spot_data.items():
            #total_spots += len(file_paths)

            repeat = 0
            for x in range(len(file_paths)):
                if(file_paths[x][-5] == ')') and (int(file_paths[x][-6]) > repeat):                   
                    repeat = int(file_paths[x][-6])
            if(repeat == 0):
                total_spots+=1
            else:
                total_spots+=repeat

            concatenated_data = DataConcat(file_paths)

            if any(np.log10(concatenated_data['Absolute Value of J']) > 0):
                spots_with_values_greater_than_3_4 += 1
                est_night.append(1/len(file_paths))
            else:
                est_night.append(0)
                

    #print(f"Total Spots with Values > 3: {spots_with_values_greater_than_3_3}")
    if total_spots > 0:
        spots_with_values_greater_than_34 = spots_with_values_greater_than_3_4 /total_spots * 100
        #print(total_spots)
        total_spots_time[3] = total_spots
        counter2tot[3] = spots_with_values_greater_than_34
    #countertot = 0
    if total_spots > 10:
        std_night = []
        for scfc_line, spot_data in night.items():
            each_spots = len(spot_data)
            for spot_number, file_paths in spot_data.items():
                std_temp = 0
                #print(len(file_paths))
                #each_spots = len(file_paths)
                concatenated_data = DataConcat(file_paths)
                if any(np.log10(concatenated_data['Absolute Value of J']) > 0):
                    std_temp += 1
                std_night.append(std_temp/each_spots*100)
        deviations = [(x - spots_with_values_greater_than_34) ** 2 for x in std_night]
        variance = sum(deviations) / total_spots
        std_time[3] = math.sqrt(variance)
    else:
        std_time[3] = -1
else:
    
    counter2tot[3] = -100

if (counter2tot[0] == 0):
    counter2tot[0] = -100
    
    
hums=[74.4005,70.3875,76.75025,86.807375]
label = ['Noon','Afternoon','Evening','Night']
std_hum = [12.09512463,11.68054981,11.31933799,7.977036847]
std_time[1] = 2.98
fig, ax1 = plt.subplots(figsize=(20,12),dpi = 300)

#ax1.set_title('# of Shorted Junctions in Different Time Periods', fontweight='bold', fontsize=16)
ax1.set_xlabel('Time Period', fontsize=40)
ax1.set_ylabel('Shorts per Chip(%)', color='red',fontsize=40)
#degree = 2
xs = np.linspace(0, 3, 4)
ax1.scatter(label, counter2tot, color='red',s=800)
ax1.yaxis.set_major_formatter(mtick.PercentFormatter())
ax1.tick_params(axis='x',labelsize=40)
ax1.tick_params(axis='y', labelcolor='red',labelsize=40)

ax2 = ax1.twinx()
ax2.scatter(label, hums, color='blue', label='Humidity Data Points',s=800)
ax2.yaxis.set_major_formatter(mtick.PercentFormatter())
ax2.set_ylabel('Humidity(%)', color='blue',fontsize=40)
ax2.tick_params(axis='y', labelcolor='blue',labelsize=40)
ax1.text(0,47,'n =' + str(spots_with_values_greater_than_3_1),fontsize=40)
ax1.text(0.75,47,'n =' + str(spots_with_values_greater_than_3_2),fontsize=40)
ax1.text(1.75,47,'n =' + str(spots_with_values_greater_than_3_3),fontsize=40)
ax1.text(2.75,30,'n =' + str(spots_with_values_greater_than_3_4),fontsize=40)
ax1.set_ylim(-3,50)
for x in range(len(timePeriod)):
    if not(std_time[x] == -1):
        ax1.errorbar(label[x], counter2tot[x],yerr=std_time[x],fmt='none',capsize=20,ecolor='red')
    ax2.errorbar(label[x], hums[x],yerr=std_hum[x],fmt='none',capsize=20,ecolor='blue')
ax2.set_ylim(0,100)
plt.tight_layout()
plt.show()   

spots_with_values_greater_than_30 = 0
spots_with_values_greater_than_31 = 0
spots_with_values_greater_than_32 = 0
spots_with_values_greater_than_33 = 0
spots_with_values_greater_than_34 = 0
spots_with_values_greater_than_3_0 = 0
spots_with_values_greater_than_3_1 = 0
spots_with_values_greater_than_3_2 = 0
spots_with_values_greater_than_3_3 = 0
spots_with_values_greater_than_3_4 = 0    

if not(len(spring) == 0):
    spring=group_files_by_scfc_and_spot(spring)
    spots_with_values_greater_than_3_0 = 0
    total_spots=0  
    for scfc_line, spot_data in spring.items():
        #total_spots += len(spot_data)
        for spot_number, file_paths in spot_data.items():
            #total_spots += len(file_paths)

            repeat = 0
            for x in range(len(file_paths)):
                if(file_paths[x][-5] == ')') and (int(file_paths[x][-6]) > repeat):                   
                    repeat = int(file_paths[x][-6])
            if(repeat == 0):
                total_spots+=1
            else:
                total_spots+=repeat

            concatenated_data = DataConcat(file_paths)
            

            if any(np.log10(concatenated_data['Absolute Value of J']) > 0):
                spots_with_values_greater_than_3_0 += 1
                est_spring.append(1/len(file_paths))
            else:
                est_spring.append(0)

    #print(f"Total Spots with Values > 3: {spots_with_values_greater_than_3_1}")
    if total_spots > 0:
        spots_with_values_greater_than_30 = spots_with_values_greater_than_3_0 / total_spots * 100
        #print(total_spots)
        total_spots_seasons[0] = total_spots
        seasonCounter[0] = spots_with_values_greater_than_30
    #countertot = 0
    if total_spots > 10:
        std_spring = []
        for scfc_line, spot_data in spring.items():
            each_spots = len(spot_data)
            for spot_number, file_paths in spot_data.items():
                std_temp = 0
                #print(len(file_paths))
                #each_spots = len(file_paths)
                concatenated_data = DataConcat(file_paths)
                if any(np.log10(concatenated_data['Absolute Value of J']) > 0):
                    std_temp += 1
                std_spring.append(std_temp/each_spots*100)
        deviations = [(x - spots_with_values_greater_than_30) ** 2 for x in std_spring]
        variance = sum(deviations) / total_spots
        std_season[0] = math.sqrt(variance)
    else:
        std_season[0] = -1
else:
    seasonCounter[0] = -100

if not(len(summer) == 0):
    summer=group_files_by_scfc_and_spot(summer)
    spots_with_values_greater_than_3_1 = 0
    total_spots=0   
    for scfc_line, spot_data in summer.items():
        #total_spots += len(spot_data)
        for spot_number, file_paths in spot_data.items():
            #total_spots += len(file_paths)

            repeat = 0
            for x in range(len(file_paths)):
                if(file_paths[x][-5] == ')') and (int(file_paths[x][-6]) > repeat):                   
                    repeat = int(file_paths[x][-6])
            if(repeat == 0):
                total_spots+=1
            else:
                total_spots+=repeat

            concatenated_data = DataConcat(file_paths)
            
            

            if any(np.log10(concatenated_data['Absolute Value of J']) > 0):
                spots_with_values_greater_than_3_1 += 1
                est_summer.append(1/len(file_paths))
            else:
                est_summer.append(0)

    #print(f"Total Spots with Values > 3: {spots_with_values_greater_than_3_1}")
    if total_spots > 0:
        spots_with_values_greater_than_31 = spots_with_values_greater_than_3_1 / total_spots *100
        #print(total_spots)
        total_spots_seasons[1] = total_spots
        seasonCounter[1] = spots_with_values_greater_than_31
    #countertot = 0
    if total_spots > 10:
        std_summer = []
        for scfc_line, spot_data in summer.items():
            each_spots = len(spot_data)
            for spot_number, file_paths in spot_data.items():
                std_temp = 0
                #print(len(file_paths))
                #each_spots = len(file_paths)
                concatenated_data = DataConcat(file_paths)
                if any(np.log10(concatenated_data['Absolute Value of J']) > 0):
                    std_temp += 1
                std_summer.append(std_temp/each_spots*100)
        deviations = [(x - spots_with_values_greater_than_31) ** 2 for x in std_summer]
        variance = sum(deviations) / total_spots
        std_season[1] = math.sqrt(variance)
    else:
        std_season[1] = -1
else:
    seasonCounter[1] = -100

if not(len(autumn) == 0):
    autumn=group_files_by_scfc_and_spot(autumn)
    spots_with_values_greater_than_3_2 = 0
    total_spots=0   
    #print(afternoon)
    for scfc_line, spot_data in autumn.items():
        #total_spots += len(spot_data)
        for spot_number, file_paths in spot_data.items():
            #total_spots += len(file_paths)

            repeat = 0
            for x in range(len(file_paths)):
                if(file_paths[x][-5] == ')') and (int(file_paths[x][-6]) > repeat):                   
                    repeat = int(file_paths[x][-6])
            if(repeat == 0):
                total_spots+=1
            else:
                total_spots+=repeat

            concatenated_data = DataConcat(file_paths)
            
            if any(np.log10(concatenated_data['Absolute Value of J']) > 0):
                spots_with_values_greater_than_3_2 += 1
                est_autumn.append(1/len(file_paths))
            else:
                est_autumn.append(0)

    #print(f"Total Spots with Values > 3: {spots_with_values_greater_than_3_2}")
    if total_spots > 0:
        spots_with_values_greater_than_32 = spots_with_values_greater_than_3_2 / total_spots * 100
        #print(total_spots)
        total_spots_seasons[2] = total_spots
        seasonCounter[2] = spots_with_values_greater_than_32
    if total_spots > 10:
        std_autumn = []
        for scfc_line, spot_data in autumn.items():
            each_spots = len(spot_data)
            for spot_number, file_paths in spot_data.items():
                std_temp = 0
                #print(len(file_paths))
                #each_spots = len(file_paths)
                concatenated_data = DataConcat(file_paths)
                if any(np.log10(concatenated_data['Absolute Value of J']) > 0):
                    std_temp += 1
                std_autumn.append(std_temp/each_spots*100)
        deviations = [(x - spots_with_values_greater_than_32) ** 2 for x in std_autumn]
        variance = sum(deviations) / total_spots
        std_season[2] = math.sqrt(variance)
    else:
        std_season[2] = -1
else:
    seasonCounter[2] = -100
    
if not(len(winter) == 0):
    winter=group_files_by_scfc_and_spot(winter)
    spots_with_values_greater_than_3_3 = 0
    total_spots=0
    #print(afternoon)
    for scfc_line, spot_data in winter.items():
        #total_spots += len(spot_data)
        for spot_number, file_paths in spot_data.items():
            #total_spots += len(file_paths)

            repeat = 0
            for x in range(len(file_paths)):
                if(file_paths[x][-5] == ')') and (int(file_paths[x][-6]) > repeat):                   
                    repeat = int(file_paths[x][-6])
            if(repeat == 0):
                total_spots+=1
            else:
                total_spots+=repeat
            
            concatenated_data = DataConcat(file_paths)
            
            if any(np.log10(concatenated_data['Absolute Value of J']) > 0):
                spots_with_values_greater_than_3_3 += 1
                est_winter.append(1/len(file_paths))
            else:
                est_winter.append(0)

    #print(f"Total Spots with Values > 3: {spots_with_values_greater_than_3_2}")
    if total_spots > 0:
        spots_with_values_greater_than_33 = spots_with_values_greater_than_3_3 / total_spots * 100
        #print(total_spots)
        total_spots_seasons[3] = total_spots
        seasonCounter[3] = spots_with_values_greater_than_33
    if total_spots > 10:
        std_winter = []
        for scfc_line, spot_data in winter.items():
            each_spots = len(spot_data)
            for spot_number, file_paths in spot_data.items():
                std_temp = 0
                #print(len(file_paths))
                #each_spots = len(file_paths)
                concatenated_data = DataConcat(file_paths)
                if any(np.log10(concatenated_data['Absolute Value of J']) > 0):
                    std_temp += 1
                std_winter.append(std_temp/each_spots*100)
        deviations = [(x - spots_with_values_greater_than_33) ** 2 for x in std_winter]
        variance = sum(deviations) / total_spots
        std_season[3] = math.sqrt(variance)
    else:
        std_season[3] = -1
else:
    seasonCounter[3] = -100

for i in range(len(scounts)):
    scounts[i] = shorting[i] - counter2[i]
    

carbonNum = ['C11\nNPPD','C11\nPPD','C11\nDPA','C11\nDEA','C12\nDPA','C12\nPRR\nRT','C12\nPRR\nICE','C12\nPYR','C12\nDEA','C12\nPPD','C12\nPRR']
#carbospeci = ['NPPD','PPD','DPA','DEA','DPA','PRR RT','PRR ICE','PYR','DEA','PPD','PRR']
hums=[72.739,63.104,55.019,59.949,80.374,86.538,89.025,70.62,74.01375,95.674,90.885]


plt.scatter(dogs,counter2,c='black',s=80)
plt.xticks(np.arange(0, 10 + 1, 1),carbonNum,fontsize = 15)
plt.yticks(np.arange(0,max(counter2) + 1, 1),fontsize = 15)
plt.grid(True,alpha=0.25)
#plt.title('Carbon Number Vs Number of Shorted Junctions')
#plt.xlabel('Carbon Length')
#plt.title('Carbon Length Vs # of Shorted Junctions',fontweight='bold',fontsize=16)
plt.xlabel('Carbon Length')
plt.ylabel('# of Shorted Junctions')
plt.show()


'''
plt.scatter(dogs,J0,c='black')
plt.xticks(np.arange(9, 12 + 1, 1),['C9','C11','C13','C15'])
plt.yticks(np.arange(0,max(J0), 1))
plt.grid(True,alpha=0.25)
#plt.title('Carbon Number Vs Number of Shorted Junctions')
#plt.xlabel('Carbon Length')
plt.title('J0 Vs Number of Shorted Junctions')
plt.xlabel('Carbon Length')
plt.ylabel('J0')
plt.text(9,0.0005,str(J0[0]),fontsize=8)
plt.text(10,0.0001,str(J0[1]),fontsize=8)
plt.text(11,0.0005,str(J0[2]),fontsize=8)
plt.text(12,0.0001,str(J0[3]),fontsize=8)
plt.show()

'''


ratios=counter2/shorting
'''
plt.scatter(dogs,ratios,c='black')
plt.xticks(np.arange(9, 12 + 1, 1),['C9','C11','C13','C15'])
plt.yticks(np.arange(0,1.1, 0.1))
plt.grid(True,alpha=0.25)
#plt.title('Carbon Number Vs Density of Shorted Junctions')
plt.title('User Measurement Vs Density of Shorted Junctions')
plt.xlabel('Carbon Length')
plt.ylabel('Density of Shorts')
plt.show()
'''
fig, ax1 = plt.subplots(figsize=(20,12),dpi = 300)

#ax1.set_title('Carbon Length Vs % of Shorted Junctions', fontweight='bold', fontsize=40)
ax1.set_xlabel('Carbon Length', fontweight='bold', labelpad=15, fontsize=40)
ax1.set_ylabel('Ratio of # of Shorts/Total', color='red', fontsize=40)
# Plot the data points and the fitted curve for counter2tot
for index in range(len(ratios)):
    if(int(carbonNum[index][1:3]) % 2) == 0:
        ax1.scatter(carbonNum[index], ratios[index], color='white',s=500, marker="o", edgecolors="red")
    else:
        ax1.scatter(carbonNum[index], ratios[index], color='red',s=500, marker="o")
#ax1.scatter(carbonNum, ratios, color='red',s=80)
ax1.tick_params(axis='x', labelsize = 40)
ax1.tick_params(axis='y', labelcolor='red',labelsize = 40)

ax2 = ax1.twinx()
ax2.scatter(carbonNum, hums, color='blue',s=500,marker = 'o')
ax2.set_ylabel('Humidity', color='blue', fontsize=40)

ax2.yaxis.set_ticks(np.arange(30,98,10))
ax2.set_ylim(24,98)
ax2.tick_params(axis='y', labelcolor='blue',labelsize = 40)

plt.tight_layout()
plt.show()


plt.figure()
plt.scatter(dogs,devs,c='black',s=80)
plt.xticks(np.arange(0, 10 + 1, 1),carbonNum,fontsize = 15)
plt.yticks(np.arange(0,max(devs)+1,3),fontsize = 15)
plt.grid(True,alpha=0.25)
plt.title('Carbon Length vs # of Junctions with STD>{}'.format(round(std,3)),fontweight='bold',fontsize=16)
plt.xlabel('Carbon Length')
plt.ylabel('# of Junctions with STD>{}'.format(round(std,3)))
plt.show()


densitystd=devs/scounts

fig, ax1 = plt.subplots(figsize=(20,12),dpi = 300)

#ax1.set_title('% of Junctions with STD>{} at each Voltage'.format(round(std,3)), fontweight='bold', fontsize=40)
ax1.set_xlabel('Carbon Length', fontweight='bold', labelpad=15, fontsize=40)
ax1.set_ylabel('Denstiy of Junctions with STD>{}'.format(round(std,3)), color='red',fontsize=39)
# Plot the data points and the fitted curve for counter2tot
for index in range(len(densitystd)):
    if(int(carbonNum[index][1:3]) % 2) == 0:
        ax1.scatter(carbonNum[index], densitystd[index], color='white',s=500, marker="o", edgecolors="red")
    else:
        ax1.scatter(carbonNum[index], densitystd[index], color='red',s=500, marker="o")
#ax1.scatter(carbonNum, densitystd, color='red',s=80)
ax1.tick_params(axis='x', labelsize = 40)
ax1.tick_params(axis='y', labelcolor='red',labelsize = 40)

ax2 = ax1.twinx()
ax2.scatter(carbonNum, hums, color='blue',s=500,marker='o')
ax2.set_ylabel('Humidity', color='blue', fontsize=40)
ax2.set_ylim(24,98)
ax2.tick_params(axis='y', labelcolor='blue',labelsize = 40)

plt.tight_layout()
plt.show()

'''
plt.figure()
plt.scatter(dogs,densitystd,c='black')
plt.xticks(np.arange(9, 12 + 1, 1),['C9','C11','C13','C15'])
plt.yticks(np.arange(0,1.1,0.1))
plt.grid(True,alpha=0.25)
plt.title('Density of Junctions with STD>{} at each Voltage'.format(round(std,3)))
plt.xlabel('Carbon Length')
plt.ylabel('Denstiy of Junctions with STD>{}'.format(round(std,3)))
plt.show()
'''
'''

plt.figure()
plt.scatter(dogs,stdavg,c='black')
plt.xticks(np.arange(9,16+1,1))
plt.yticks(np.arange(0,1.1,0.1))
plt.grid(True,alpha=0.25)
plt.title('Carbon Number vs Avg Std ')
plt.xlabel('Carbon Length')
plt.ylabel('Avg Std')
plt.show()
'''
plt.figure(figsize=(20,12))
plt.scatter(timePeriod,seasonCounter,c='black',s=800)
label = ['Spring','Summer','Autumn','Winter']
plt.xticks(np.arange(0,4,1),label,fontsize = 40)
plt.yticks(np.arange(0,51,10),fontsize = 40)
plt.grid(True,alpha=0.15)
#plt.title('Number of Shorted Junctions in Different Seasons',fontweight='bold',fontsize=18)
plt.xlabel('Seasons', fontsize=40)
plt.ylabel('Shorts per Chip(%)',fontsize=40)
plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter())
plt.ylim(-1,51)
#plt.text(-0.25,-7,'3/1-5/31',fontsize=40)
#plt.text(0.75,-7,'6/1-8/31',fontsize=40)
#plt.text(0.1,10,'No Measurement Taken in Spring and Winter',fontsize=40,color='red')
#plt.text(1.75,-7,'9/1-11/30',fontsize=40)
#plt.text(2.70,-7,'12/1-2/28(29)',fontsize=40)
plt.text(1.8,40,'n =' + str(spots_with_values_greater_than_3_2),fontsize=40)
plt.text(0.8,40,'n =' + str(spots_with_values_greater_than_3_1),fontsize=40)
for x in range(len(timePeriod)):
    if not(std_season[x] == -1):
        plt.errorbar(timePeriod[x],seasonCounter[x],yerr=std_season[x],fmt='none',capsize=20,ecolor='black')

'''
plt.figure()
plt.scatter(timePeriod,counter2tot,c='black',s=80)
#label = ['10PM - 10AM','10AM - 2PM','2PM - 6PM','6PM - 10PM']
label = ['10AM - 2PM','2PM - 6PM','6PM - 10PM','10PM - 6AM']
plt.xticks(np.arange(0,4,1),label,fontsize = 14)
plt.yticks(np.arange(0,max(counter2tot)+0.05,0.05),fontsize = 14)
plt.grid(True,alpha=0.15)
#plt.title('Number of Shorted Junctions in Different Time Periods',fontweight='bold',fontsize=18)
plt.xlabel('Time Period',fontweight='bold',labelpad=15,fontsize=12)
plt.ylabel('Ratio of # of Shorts/Total',fontweight='bold',fontsize=12)
'''
'''
plt.text(-0.30,-0.02,'6 AM - 10 AM',fontsize=10)
plt.text(0.70,-0.02,'10 AM - 2 PM',fontsize=10)
plt.text(1.70,-0.02,'2 PM - 6 PM',fontsize=10)
plt.text(2.70,-0.02,'6 PM - 10 PM',fontsize=10)
plt.text(3.70,-0.02,'10 PM - 6 AM',fontsize=10)
'''

#plt.text(0.5,0.09,'Ratio: '+str(round(spots_with_values_greater_than_31,3))+ "| Shorts:"+str(spots_with_values_greater_than_3_1),fontsize=13)
#plt.text(1.5,0.04,'Ratio: '+str(round(spots_with_values_greater_than_32,3))+ "| Shorts:"+str(spots_with_values_greater_than_3_2),fontsize=13)
#plt.text(2.5,0.04,'Ratio: '+str(round(spots_with_values_greater_than_33,3))+ "| Shorts:" + str(spots_with_values_greater_than_3_3),fontsize=13)
#plt.text(3.05,0.1,'Ratio: '+str(round(spots_with_values_greater_than_34,3))+ "| Shorts:" + str(spots_with_values_greater_than_3_4),fontsize=13)
#plt.show()

#avg=sum(stdavg)/len(stdavg)
#print(avg)
'''
#hums=[77.85354, 70.20533333, 68.4425, 72.86854167]  #10pm-10am
#hums = [84.58916667,67.69166667,71.1725,81.86083333]
hums=[74.4005,70.3875,76.75025,86.807375]   #10pm-6am


fig, ax1 = plt.subplots(figsize=(20,12),dpi = 300)

#ax1.set_title('# of Shorted Junctions in Different Time Periods', fontweight='bold', fontsize=16)
ax1.set_xlabel('Time Period', fontsize=40)
ax1.set_ylabel(' # of Shorts/Total(%)', color='red',fontsize=40)
#degree = 2
xs = np.linspace(0, 3, 4)

#popt, pcov = curve_fit(gaus, xs, counter2tot)
#plt.plot(xs,gaus(xs,*popt),'ro:',label='fit')
#plt.show()

#coefficients_counter2tot = np.polyfit(xs, counter2tot, degree)
#y_fit_counter2tot = np.polyval(coefficients_counter2tot, xs)

#X_Y_Spline = make_interp_spline(xs, y_fit_counter2tot)
 
# Returns evenly spaced numbers
# over a specified interval.
#X_ = np.linspace(xs.min(), xs.max(), 500)
#Y_ = X_Y_Spline(X_)

# Plot the data points and the fitted curve for counter2tot
ax1.scatter(label, counter2tot, color='red',s=500)
ax1.yaxis.set_major_formatter(mtick.PercentFormatter())
ax1.tick_params(axis='x',labelsize=40)
#ax1.plot(X_, Y_, color='lightcoral')

# Calculate R-squared for counter2tot
#r_squared_counter2tot = r2_score(counter2tot, y_fit_counter2tot)

# Annotate the plot with R-squared value (counter2tot)
#r_squared_str_counter2tot = f'R-squared: {r_squared_counter2tot:.2f}'
#equation = 'Equation: ' + str(round(coefficients_counter2tot[0],3)) + 'x^2+' + str(round(coefficients_counter2tot[1],3)) + 'x+' + str(round(coefficients_counter2tot[2],3))
#ax1.annotate(r_squared_str_counter2tot, xy=(0.04, 0.9), xycoords='axes fraction', fontsize=10, color='red')
#ax1.annotate(equation, xy=(0.04, 0.8), xycoords='axes fraction', fontsize=10, color='red')
ax1.tick_params(axis='y', labelcolor='red',labelsize=40)


#coefficients_hums = np.polyfit(xs, hums, degree)
#y_fit_hums = np.polyval(coefficients_hums, xs)

#X_Y_Spline = make_interp_spline(xs, y_fit_hums)
 
# Returns evenly spaced numbers
# over a specified interval.
#X_ = np.linspace(xs.min(), xs.max(), 500)
#Y_ = X_Y_Spline(X_)


ax2 = ax1.twinx()
#ax2.plot(X_, Y_, label='Fitted Curve (Humidity)', color='lightblue')
ax2.scatter(label, hums, color='blue', label='Humidity Data Points',s=500)
ax2.yaxis.set_major_formatter(mtick.PercentFormatter())
# Calculate R-squared for humidity
#r_squared_hums = r2_score(hums, y_fit_hums)

# Annotate the plot with R-squared value (humidity)
#r_squared_str_hums = f'R-squared: {r_squared_hums:.2f}'
#ax2.annotate(r_squared_str_hums, xy=(0.02, 0.7), xycoords='axes fraction', fontsize=10, color='blue')

ax2.set_ylabel('Humidity(%)', color='blue',fontsize=40)
ax2.tick_params(axis='y', labelcolor='blue',labelsize=40)
ax1.text(-0.1,19,'n =' + str(total_spots_time[0]),fontsize=40)
ax1.text(0.8,4,'n =' + str(total_spots_time[1]),fontsize=40)
ax1.text(1.8,6,'n =' + str(total_spots_time[2]),fontsize=40)
ax1.text(2.8,2,'n =' + str(total_spots_time[3]),fontsize=40)
ax1.set_ylim(-3,50)
for x in range(len(timePeriod)):
    if not(std_time[x] == -1):
        ax1.errorbar(label[x], counter2tot[x],yerr=std_time[x],fmt='none',capsize=20,ecolor='red')
ax2.set_ylim(48,90)
# Set the legend
#ax1.legend(loc='upper left', bbox_to_anchor=(0.7, 1.05))

plt.tight_layout()
plt.show()
'''

'''

This stuff is another attempt at fitting curve an putting r squared on the plot.
However, while the curve is smooth, I couldn't get the r squared values to show or look proper.
Run if you want to see how it looks - could try to fix it.

x_data = np.linspace(0, 4, 5)
counter2tot = [0, 0.11111111111111111111, 0.21666666666666667, 0.21818181818181817, 0.0784313725490196]

# Fitted curve for the first set of data
degree = 2
coefficients_1 = np.polyfit(x_data, counter2tot, degree)
x_fit = np.linspace(min(x_data), max(x_data), 100)
y_fit_1 = np.polyval(coefficients_1, x_fit)

# Sample humidity data
hums = [1/74.23598, 1/61.83482, 1/54.08589, 1/58.57513,1/72.96708]

# Fitted curve for humidity data
coefficients_2 = np.polyfit(x_data, hums, degree)
y_fit_2 = np.polyval(coefficients_2, x_fit)

# Calculate the percentage difference between the two curves at each x-value
percentage_difference = np.abs((y_fit_1 - y_fit_2) / ((y_fit_1 + y_fit_2) / 2)) * 100

# Create a plot
fig, ax1 = plt.subplots()

# Plot the original data points and the fitted curves for counter2tot
ax1.scatter(x_data, counter2tot, color='red', label='Counter2tot Data')
ax1.plot(x_fit, y_fit_1, label='Fitted Curve (Counter2tot)', color='red')

# Set labels and tick colors for the first y-axis (counter2tot)
ax1.set_xlabel('Time Period', fontweight='bold', labelpad=15, fontsize=12)
ax1.set_ylabel('Ratio of # of Shorts/Total', color='red')
ax1.tick_params(axis='y', labelcolor='red')

# Plot the fitted curve for humidity on the second y-axis
ax2 = ax1.twinx()
ax2.plot(x_fit, y_fit_2, label='Fitted Curve (Humidity)', color='blue')

# Set label and tick color for the second y-axis (humidity)
ax2.set_ylabel('Humidity (%)', color='blue')
ax2.tick_params(axis='y', labelcolor='blue')

# Calculate the y-axis range for counter2tot
counter2tot_min = np.min(counter2tot)
counter2tot_max = np.max(counter2tot)
counter2tot_range = counter2tot_max - counter2tot_min

# Calculate the scaled percentage difference based on y_fit_1 range
scaled_percentage_difference = percentage_difference * counter2tot_range / 100

# Show the percentage difference as text on the plot
for i, x_val in enumerate(x_data):
    # Adjust the text placement for percentage difference
    text_y = counter2tot[i] + scaled_percentage_difference[i]
    if text_y <= counter2tot_max:  # Avoid exceeding the upper limit of counter2tot
        ax1.annotate(f'{percentage_difference[i]:.2f}%', (x_val, text_y), textcoords="offset points", xytext=(0, 3),
                     ha='center', color='blue')

plt.tight_layout()
plt.show()
'''