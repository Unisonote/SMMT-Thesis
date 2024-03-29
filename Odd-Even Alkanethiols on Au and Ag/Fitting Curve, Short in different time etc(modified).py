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

sc='sc'
fc='fc'
c=chr(92)
carbo_folder_path= r'F:\Thuo Research Group\RE Martin data\Odd-even alkanethiols on Ag'
#carbonLen = [9,11,13,15]
dogs=np.linspace(7,17,11)
timePeriod = np.linspace(0,4,5)
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

dateChangeFormat = []


def gaussian(x, A, B):
   return A*np.exp(-1*B*x**2)                                                                                                                                          

'''
Get duration for the selected spot
'''
def getDate(Series):
    
    date = []
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
J0 = np.linspace(0,7,8)
counter2tot = [0] * 5
J0tot = [0] * 5
for values in dogs:
    carbo_folder_path= r'F:\Thuo Research Group\RE Martin data\Odd-even alkanethiols on Ag'
    values=str(int(values))
    carbo_folder_path=carbo_folder_path + c + sc + values + fc
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


    
                
            if Full.empty:
                break
            #if len(time) == 0:
                #break
        
        #result=Full
        #Volts=result['Voltage (V)']
        Abso = Full['Absolute Value of J']
        J0_temp = []
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
    pattern = r"sc(\d+)fc\\(\d+)" # Change if dataset format changes - current (sc15fc/spot 1)

    grouped_files = {}

    for file_path in file_paths:
        match = re.search(pattern, file_path)
        if match:
            scfc = match.group(1)
            spot = match.group(2)
            key = f"sc{scfc}fc" # Change as well if dataset format changes - if just number then can change whole apparatus
            if key not in grouped_files:
                grouped_files[key] = {}
            if spot not in grouped_files[key]:
                grouped_files[key][spot] = []
            grouped_files[key][spot].append(file_path)

    return grouped_files


if not(len(morning) == 0):
    morning=group_files_by_scfc_and_spot(morning)
    spots_with_values_greater_than_3_0 = 0
    total_spots=0
    for scfc_line, spot_data in morning.items():

        for spot_number, file_paths in spot_data.items():
            total_spots+=1
            concatenated_data = DataConcat(file_paths)
            

            if any(np.log10(concatenated_data['Absolute Value of J']) > 3):
                spots_with_values_greater_than_3_0 += 1

    #print(f"Total Spots with Values > 3: {spots_with_values_greater_than_3_1}")
    if total_spots > 0:
        spots_with_values_greater_than_30 = spots_with_values_greater_than_3_0 / total_spots
        #print(total_spots)
        counter2tot[0] = spots_with_values_greater_than_30
    countertot = 0
else:
    counter2tot[0] = 0

if not(len(noon) == 0):
    noon=group_files_by_scfc_and_spot(noon)
    spots_with_values_greater_than_3_1 = 0
    total_spots=0
    for scfc_line, spot_data in noon.items():

        for spot_number, file_paths in spot_data.items():
            total_spots+=1
            concatenated_data = DataConcat(file_paths)
            
            

            if any(np.log10(concatenated_data['Absolute Value of J']) > 0):
                spots_with_values_greater_than_3_1 += 1

    #print(f"Total Spots with Values > 3: {spots_with_values_greater_than_3_1}")
    if total_spots > 0:
        spots_with_values_greater_than_31 = spots_with_values_greater_than_3_1 / total_spots
        #print(total_spots)
        counter2tot[1] = spots_with_values_greater_than_31
    countertot = 0
else:
    counter2tot[1] = 0

if not(len(afternoon) == 0):
    afternoon=group_files_by_scfc_and_spot(afternoon)
    spots_with_values_greater_than_3_2 = 0
    total_spots=0
    #print(afternoon)
    for scfc_line, spot_data in afternoon.items():
        for spot_number, file_paths in spot_data.items():
            total_spots+=1
            concatenated_data = DataConcat(file_paths)
            
            if any(np.log10(concatenated_data['Absolute Value of J']) > 0):
                spots_with_values_greater_than_3_2 += 1

    #print(f"Total Spots with Values > 3: {spots_with_values_greater_than_3_2}")
    if total_spots > 0:
        spots_with_values_greater_than_32 = spots_with_values_greater_than_3_2 / total_spots
        #print(total_spots)
        counter2tot[2] = spots_with_values_greater_than_32
    countertot = 0
else:
    counter2tot[2] = 0
    
if not(len(evening) == 0):
    evening=group_files_by_scfc_and_spot(evening)
    spots_with_values_greater_than_3_3 = 0
    total_spots=0
    #print(afternoon)
    for scfc_line, spot_data in evening.items():
        for spot_number, file_paths in spot_data.items():
            total_spots+=1
            concatenated_data = DataConcat(file_paths)
            
            if any(np.log10(concatenated_data['Absolute Value of J']) > 0):
                spots_with_values_greater_than_3_3 += 1

    #print(f"Total Spots with Values > 3: {spots_with_values_greater_than_3_2}")
    if total_spots > 0:
        spots_with_values_greater_than_33 = spots_with_values_greater_than_3_3 / total_spots
        #print(total_spots)
        counter2tot[3] = spots_with_values_greater_than_33
    countertot = 0
else:
    counter2tot[3] = 0    
    
if not(len(night) == 0):
    night=group_files_by_scfc_and_spot(night)
    spots_with_values_greater_than_3_4 = 0
    total_spots=0
    for scfc_line, spot_data in night.items():

        for spot_number, file_paths in spot_data.items():
            total_spots+=1
            concatenated_data = DataConcat(file_paths)

            if any(np.log10(concatenated_data['Absolute Value of J']) > 0):
                spots_with_values_greater_than_3_4 += 1

    #print(f"Total Spots with Values > 3: {spots_with_values_greater_than_3_3}")
    if total_spots > 0:
        spots_with_values_greater_than_34 = spots_with_values_greater_than_3_4 /total_spots
        #print(total_spots)
        counter2tot[4] = spots_with_values_greater_than_34
    countertot = 0
else:
    
    counter2tot[4] = 0



for i in range(len(scounts)):
    scounts[i] = shorting[i] - counter2[i]
    

carbonNum = ['C7','C8','C9','C11','C13','C14','C15','C16','C17','C18','C19']
hums=[26.18, 67.31, 59.82857, 42.57583,1,1,1,1,1,1,1]


plt.scatter(dogs,counter2,c='black')
plt.xticks(np.arange(7, 17 + 1, 1),['C7','C8','C9','C11','C13','C14','C15','C16','C17','C18','C19'])
plt.yticks(np.arange(0,max(counter2) + 1, 1))
plt.grid(True,alpha=0.25)
#plt.title('Carbon Number Vs Number of Shorted Junctions')
#plt.xlabel('Carbon Length')
plt.title('Carbon Length Vs Number of Shorted Junctions')
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
fig, ax1 = plt.subplots()

ax1.set_title('Carbon Length Vs Ratio of Shorted Junctions', fontweight='bold', fontsize=18)
ax1.set_xlabel('Carbon Length', fontweight='bold', labelpad=15, fontsize=12)
ax1.set_ylabel('Ratio of # of Shorts/Total', color='red')
degree = 2
# Plot the data points and the fitted curve for counter2tot
ax1.scatter(carbonNum, ratios, color='red')
ax1.tick_params(axis='y', labelcolor='red')

ax2 = ax1.twinx()
ax2.scatter(carbonNum, hums, color='blue')
ax2.set_ylabel('Humidity', color='blue')
ax2.tick_params(axis='y', labelcolor='blue')

plt.tight_layout()
plt.show()


plt.figure()
plt.scatter(dogs,devs,c='black')
plt.xticks(np.arange(7, 17 + 1, 1),['C7','C8','C9','C11','C13','C14','C15','C16','C17','C18','C19'])
plt.yticks(np.arange(0,max(devs)+1,1))
plt.grid(True,alpha=0.25)
plt.title('Carbon Length vs Number of Junctions with STD>{} at each Voltage'.format(round(std,3)))
plt.xlabel('Carbon Length')
plt.ylabel('# of Junctions with STD>{}'.format(round(std,3)))
plt.show()


densitystd=devs/scounts

fig, ax1 = plt.subplots()

ax1.set_title('Density of Junctions with STD>{} at each Voltage'.format(round(std,3)), fontweight='bold', fontsize=18)
ax1.set_xlabel('Carbon Length', fontweight='bold', labelpad=15, fontsize=12)
ax1.set_ylabel('Denstiy of Junctions with STD>{}'.format(round(std,3)), color='red')
degree = 2
# Plot the data points and the fitted curve for counter2tot
ax1.scatter(carbonNum, densitystd, color='red')
ax1.tick_params(axis='y', labelcolor='red')

ax2 = ax1.twinx()
ax2.scatter(carbonNum, hums, color='blue')
ax2.set_ylabel('Humidity', color='blue')
ax2.tick_params(axis='y', labelcolor='blue')

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

plt.figure()
plt.scatter(timePeriod,counter2tot,c='black')
label = ['Morning','Noon','Afternoon','Evening','Night']
plt.xticks(np.arange(0,5,1),label)
plt.yticks(np.arange(0,max(counter2tot)+0.05,0.05))
plt.grid(True,alpha=0.15)
plt.title('Number of Shorted Junctions in Different Time Periods',fontweight='bold',fontsize=18)
plt.xlabel('Time Period',fontweight='bold',labelpad=15,fontsize=12)
plt.ylabel('Ratio of # of Shorts/Total',fontweight='bold',fontsize=12)

plt.text(-0.30,-0.01,'6 AM - 10 AM',fontsize=7)
plt.text(0.70,-0.01,'10 AM - 2 PM',fontsize=7)
plt.text(1.70,-0.01,'2 PM - 6 PM',fontsize=7)
plt.text(2.70,-0.01,'6 PM - 10 PM',fontsize=7)
plt.text(3.70,-0.01,'10 PM - 6 AM',fontsize=7)

plt.text(0.5,0.09,'Ratio: '+str(round(spots_with_values_greater_than_31,3))+ "| Shorts:"+str(spots_with_values_greater_than_3_1),fontsize=8)
plt.text(1.5,0.02,'Ratio: '+str(round(spots_with_values_greater_than_32,3))+ "| Shorts:"+str(spots_with_values_greater_than_3_2),fontsize=8)
plt.text(2.5,0.04,'Ratio: '+str(round(spots_with_values_greater_than_33,3))+ "| Shorts:" + str(spots_with_values_greater_than_3_3),fontsize=8)
plt.text(3.05,0.1,'Ratio: '+str(round(spots_with_values_greater_than_34,3))+ "| Shorts:" + str(spots_with_values_greater_than_3_4),fontsize=8)
plt.show()

#avg=sum(stdavg)/len(stdavg)
#print(avg)

hums=[1/74.23598, 1/61.83482, 1/54.08589, 1/58.57513,1/72.96708]




fig, ax1 = plt.subplots()

ax1.set_title('Number of Shorted Junctions in Different Time Periods', fontweight='bold', fontsize=18)
ax1.set_xlabel('Time Period', fontweight='bold', labelpad=15, fontsize=12)
ax1.set_ylabel('Ratio of # of Shorts/Total', color='red')
degree = 4
xs = np.linspace(0, 4, 5)

'''
popt, pcov = curve_fit(gaussian, xs, counter2tot)
μ_fit, σ_fit = popt
y_fit = gaussian(xs, μ_fit, σ_fit)
'''



coefficients_counter2tot = np.polyfit(xs, counter2tot, degree)
y_fit_counter2tot = np.polyval(coefficients_counter2tot, xs)

X_Y_Spline = make_interp_spline(xs, y_fit_counter2tot)
 
# Returns evenly spaced numbers
# over a specified interval.
X_ = np.linspace(xs.min(), xs.max(), 500)
Y_ = X_Y_Spline(X_)
# Plot the data points and the fitted curve for counter2tot
ax1.scatter(label, counter2tot, color='red')
ax1.plot(X_, Y_, color='lightcoral')

# Calculate R-squared for counter2tot
r_squared_counter2tot = r2_score(counter2tot, y_fit_counter2tot)

# Annotate the plot with R-squared value (counter2tot)
r_squared_str_counter2tot = f'R-squared: {r_squared_counter2tot:.2f}'
ax1.annotate(r_squared_str_counter2tot, xy=(0.04, 0.8), xycoords='axes fraction', fontsize=10, color='red')

ax1.tick_params(axis='y', labelcolor='red')

coefficients_hums = np.polyfit(xs, hums, degree)
y_fit_hums = np.polyval(coefficients_hums, xs)

X_Y_Spline = make_interp_spline(xs, y_fit_hums)
 
# Returns evenly spaced numbers
# over a specified interval.
X_ = np.linspace(xs.min(), xs.max(), 500)
Y_ = X_Y_Spline(X_)


ax2 = ax1.twinx()
ax2.plot(X_, Y_, label='Fitted Curve (Humidity)', color='lightblue')
ax2.scatter(label, hums, color='blue', label='Humidity Data Points')

# Calculate R-squared for humidity
r_squared_hums = r2_score(hums, y_fit_hums)

# Annotate the plot with R-squared value (humidity)
r_squared_str_hums = f'R-squared: {r_squared_hums:.2f}'
ax2.annotate(r_squared_str_hums, xy=(0.02, 0.7), xycoords='axes fraction', fontsize=10, color='blue')

ax2.set_ylabel('1/Humidity', color='blue')
ax2.tick_params(axis='y', labelcolor='blue')

# Set the legend
#ax1.legend(loc='upper left', bbox_to_anchor=(0.7, 1.05))

plt.tight_layout()
plt.show()


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