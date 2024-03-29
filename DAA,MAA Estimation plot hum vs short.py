# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 15:14:35 2023

@author: 15253
"""

import pandas as pd
import dabest
import numpy as np

'''
DAA_hums = [72.739,63.104,55.019,59.949,80.374,86.538,89.025,70.62,74.01375,95.674,90.885]
MAA_hums = [83.205,73.859,67.69]
DAA_short_ratio = [0,0,0,0,0,66.67,0,6.67,0,0,20]
MAA_short_ratio = [8.3,0,0]

df = pd.DataFrame(columns=['51%-60%','61%-70%','71%-80%','81%-90%','>90%'])
hum_40 = []
hum_50 = []
hum_60=[]
hum_70=[]
hum_80=[]
hum_90=[]
hum_100=[]

for x in range(len(DAA_hums)):
    if(int(DAA_hums[x]) < 40):
        hum_40.append(DAA_short_ratio[x])
        #df=df.append({'<=40':(DAA_short_ratio[x] *100)},ignore_index=True)
    elif(int(DAA_hums[x]) >= 40 and int(DAA_hums[x]) < 50):
        hum_50.append(DAA_short_ratio[x])
        #df=df.append({'41-50':DAA_short_ratio[x] *100},ignore_index=True)
    elif(int(DAA_hums[x]) >= 50 and int(DAA_hums[x]) < 60):
        hum_60.append(DAA_short_ratio[x])
        #df=df.append({'51-60':DAA_short_ratio[x] *100},ignore_index=True)
    elif(int(DAA_hums[x]) >= 60 and int(DAA_hums[x]) < 70):
        hum_70.append(DAA_short_ratio[x])
        #df=df.append({'61-70':DAA_short_ratio[x] *100},ignore_index=True)
    elif(int(DAA_hums[x]) >= 70 and int(DAA_hums[x]) < 80):
        hum_80.append(DAA_short_ratio[x])
        #df=df.append({'71-80':DAA_short_ratio[x] *100},ignore_index=True)
    elif(int(DAA_hums[x]) >= 80 and int(DAA_hums[x]) < 90):
        hum_90.append(DAA_short_ratio[x])
        #df=df.append({'81-90':DAA_short_ratio[x] *100},ignore_index=True)
    elif(int(DAA_hums[x]) >= 90):        
        hum_100.append(DAA_short_ratio[x])

        #df=df.append({'>90':DAA_short_ratio[x] *100},ignore_index=True)
        
for x in range(len(MAA_hums)):
    if(int(MAA_hums[x]) < 40):
        hum_40.append(MAA_short_ratio[x])
        #df=df.append({'<=40':(MAA_short_ratio[x] *100)},ignore_index=True)
    elif(int(MAA_hums[x]) >= 40 and int(MAA_hums[x]) < 50):
        hum_50.append(MAA_short_ratio[x])
        #df=df.append({'41-50':MAA_short_ratio[x] *100},ignore_index=True)
    elif(int(MAA_hums[x]) >= 50 and int(MAA_hums[x]) < 60):
        hum_60.append(MAA_short_ratio[x])
        #df=df.append({'51-60':MAA_short_ratio[x] *100},ignore_index=True)
    elif(int(MAA_hums[x]) >= 60 and int(MAA_hums[x]) < 70):
        hum_70.append(MAA_short_ratio[x])
        #df=df.append({'61-70':MAA_short_ratio[x] *100},ignore_index=True)
    elif(int(MAA_hums[x]) >= 70 and int(MAA_hums[x]) < 80):
        hum_80.append(MAA_short_ratio[x])
        #df=df.append({'71-80':MAA_short_ratio[x] *100},ignore_index=True)
    elif(int(MAA_hums[x]) >= 80 and int(MAA_hums[x]) < 90):
        hum_90.append(MAA_short_ratio[x])
        #df=df.append({'81-90':MAA_short_ratio[x] *100},ignore_index=True)
    elif(int(MAA_hums[x]) >= 90):
        hum_100.append(MAA_short_ratio[x])
        #df=df.append({'>90':MAA_short_ratio[x] *100},ignore_index=True)
        
        
df['51%-60%'] = pd.Series(hum_60)
df['61%-70%'] = pd.Series(hum_70)
df['71%-80%'] = pd.Series(hum_80)
df['81%-90%'] = pd.Series(hum_90)
df['>90%'] = pd.Series(hum_100)
df=df.append({'71%-80%':0,'81%-90%':0},ignore_index=True)
df=df.append({'71%-80%':0,'81%-90%':8.3},ignore_index=True)


shared = dabest.load(df,idx=('51%-60%','61%-70%','71%-80%','81%-90%','>90%'))
shared.mean_diff.plot(swarm_label='Ratio of Short Sport/Total(%)')
'''

df_time = pd.DataFrame(columns=['10AM - 2PM','2PM - 6PM','6PM - 10PM','10PM - 6AM'])


#MAA_morning = [0, 0, 0, 0, 0]
#MAA_noon = [0, 0, 0, 0, 0, 0]
#MAA_evening = [0, 0, 0, 0]
#MAA_night = [0, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#MAA_summer = [0, 0, 0, 0, 0, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#MAA_autumn = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
'''
#For time period only, Close Ring MARTIN
'''
DAA_noon = [50, 50, 0, 100, 0, 0, 0, 0, 0]
DAA_afternoon = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 0, 100]
DAA_evening = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
DAA_night = [0, 0, 0, 0, 0, 0, 0, 0]
'''
#For Season, All DAA Martin data are used
'''
DAA_summer = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, 50, 0, 50, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, 50, 0, 0, 0, 0, 0, 0, 0]
DAA_autumn = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

DAA_noon_shawn_close = [0, 50, 0, 0, 33.33, 100, 0, 0]
DAA_afternoon_shawn_close = [25, 0, 0, 33.33333333333333, 0, 0, 33.33333333333333, 100, 0, 0, 12.5, 0, 14.285714285714285, 11.11111111111111, 11.11111111111111, 12.5, 16.666666666666666, 16.666666666666666, 20, 16.666666666666666, 16.666666666666666, 20, 25, 25, 50, 33.33333333333333, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 0, 10, 0, 0, 0, 0, 16.666666666666666, 0, 14.285714285714285, 14.285714285714285, 0, 0, 0, 0, 0]
DAA_evening_shawn_close = [0, 0, 100, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 33.33333333333333, 0, 0, 0, 33.33333333333333, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 20, 50, 100, 0, 0, 0, 0, 16.666666666666666, 16.666666666666666, 33.33333333333333, 33.33333333333333, 0, 0]
DAA_night_shawn_close = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1.0, 1.0]

DAA_winter_shawn_close = [0, 0, 33.33333333333333, 33.33333333333333, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 0, 0, 33.33333333333333, 0, 0, 33.33333333333333, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 33.33333333333333, 0, 0, 25, 20, 50, 7.142857142857142, 0, 0, 0, 9.090909090909091, 8.333333333333333, 9.090909090909091, 8.333333333333333, 9.090909090909091, 11.11111111111111, 0, 0]
DAA_spring_shawn_close = [6.666666666666667, 7.692307692307693, 10, 7.692307692307693, 7.142857142857142, 9.090909090909091, 8.333333333333333, 8.333333333333333, 11.11111111111111, 10, 11.11111111111111, 16.666666666666666, 20, 20, 33.33333333333333, 33.33333333333333, 100, 0, 0, 0, 0, 0, 100, 0, 0]

DAA_afternoon_shawn_open = [0, 33.33333333333333, 0, 0, 0, 0, 0, 0, 25, 0, 0, 0, 0, 25, 0, 0, 0, 0]
DAA_evening_shawn_open = [0, 0, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 33.33333333333333, 0, 0, 33.33333333333333, 0, 33.33333333333333, 0, 0]
DAA_night_shawn_open = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

DAA_winter_shawn_open = [0, 33.33333333333333, 0, 0, 0, 0, 33.33333333333333, 0, 0, 0, 0, 25, 0, 0, 0, 0, 25, 0, 0, 0, 0, 0, 0, 0, 33.33333333333333, 0, 0, 33.33333333333333, 0, 33.33333333333333, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

'''
For time period, only close ring
'''

noon_total = DAA_noon_shawn_close + DAA_noon
afternoon_total = DAA_afternoon + DAA_afternoon_shawn_close
evening_total = DAA_evening_shawn_close + DAA_evening
night_total = DAA_night + DAA_night_shawn_close

df_time['2PM - 6PM'] = pd.Series(afternoon_total)
df_time['10AM - 2PM'] = pd.Series(noon_total)
df_time['6PM - 10PM'] = pd.Series(evening_total)
df_time['10PM - 6AM'] = pd.Series(night_total)

shared = dabest.load(df_time,idx=('10PM - 6AM','6PM - 10PM','2PM - 6PM','10AM - 2PM'))
shared.mean_diff.plot(swarm_label='Ratio of Short Sport/Total(%)')
print(shared.mean_diff)
'''
For season, all DAA data
'''
spring_total = DAA_spring_shawn_close
summer_total = DAA_summer
autumn_total = DAA_autumn
winter_total = DAA_winter_shawn_open + DAA_winter_shawn_close

df_time = pd.DataFrame(columns=['Spring','Summer','Autumn','Winter'])
df_time['Summer'] = pd.Series(summer_total)
df_time['Spring'] = pd.Series(spring_total)
df_time['Autumn'] = pd.Series(autumn_total)
df_time['Winter'] = pd.Series(winter_total)

shared = dabest.load(df_time,idx=('Autumn','Summer','Winter','Spring'))
shared.mean_diff.plot(swarm_label='Ratio of Short Sport/Total(%)')
print(shared.mean_diff)
