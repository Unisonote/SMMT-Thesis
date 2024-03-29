# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 00:27:13 2023

@author: zzz
"""
import pandas as pd
import dabest
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 17})

Ag_short_ratio = [6.896551724137930939e-02,3.181818181818181768e-01,0,0,0,0,0,0,0,0,4.000000000000000083e-02]
Ag_hums=[26.18,23.77, 67.31, 59.82857, 42.57583,79.71375,48.25286,84.9475,95.57,76.43667,61.216]
Au_short_ratio = [1.764705882352941291e-01,9.523809523809523281e-02,6.666666666666666574e-02,0,0,1.000000000000000056e-01,5.000000000000000278e-02,4.761904761904761640e-02]
Au_hums=[60.68,94.76,61.0925,87.74,30.925,86.26167,54.3375,77.777]
AuTi_short_ratio= [5.000000000000000000e-01,1.818181818181818232e-01,1.499999999999999944e-01,1.666666666666666574e-01,0,7.142857142857142461e-02,2.000000000000000042e-02,9.090909090909091161e-02,1.000000000000000056e-01]
AuTi_hums = [33.71,35.22,27.55,47.92,79.6,57.36,72.36,45.14,78.29]
AgTS_short_ratio = [4.000000000000000083e-02,0,0,0,0,7.142857142857142461e-02,0,6.250000000000000000e-02]
AgTS_hums=[93.79,52.64,59.57,67.8,65.05,60.34,78.44,56.34]

df = pd.DataFrame(columns=['Humidity<=40%','41%-50%','51%-60%','61%-70%','71%-80%','81%-90%','>90%'])
hum_40 = []
hum_50 = []
hum_60=[]
hum_70=[]
hum_80=[]
hum_90=[]
hum_100=[]

for x in range(len(Ag_hums)):
    if(int(Ag_hums[x]) < 40):
        hum_40.append(Ag_short_ratio[x] *100)
    elif(int(Ag_hums[x]) >= 40 and int(Ag_hums[x]) < 50):
        hum_50.append(Ag_short_ratio[x] *100)
    elif(int(Ag_hums[x]) >= 50 and int(Ag_hums[x]) < 60):
        hum_60.append(Ag_short_ratio[x] *100)
    elif(int(Ag_hums[x]) >= 60 and int(Ag_hums[x]) < 70):
        hum_70.append(Ag_short_ratio[x] *100)
    elif(int(Ag_hums[x]) >= 70 and int(Ag_hums[x]) < 80):
        hum_80.append(Ag_short_ratio[x] *100)
    elif(int(Ag_hums[x]) >= 80 and int(Ag_hums[x]) < 90):
        hum_90.append(Ag_short_ratio[x] *100)
    elif(int(Ag_hums[x]) >= 90):
        hum_100.append(Ag_short_ratio[x] *100)

for x in range(len(Au_hums)):
    if(int(Au_hums[x]) < 40):
        hum_40.append(Au_short_ratio[x] *100)
    elif(int(Au_hums[x]) >= 40 and int(Au_hums[x]) < 50):
        hum_50.append(Au_short_ratio[x] *100)
    elif(int(Au_hums[x]) >= 50 and int(Au_hums[x]) < 60):
        hum_60.append(Au_short_ratio[x] *100)
    elif(int(Au_hums[x]) >= 60 and int(Au_hums[x]) < 70):
        hum_70.append(Au_short_ratio[x] *100)
    elif(int(Au_hums[x]) >= 70 and int(Au_hums[x]) < 80):
        hum_80.append(Au_short_ratio[x] *100)
    elif(int(Au_hums[x]) >= 80 and int(Au_hums[x]) < 90):
        hum_90.append(Au_short_ratio[x] *100)
    elif(int(Au_hums[x]) >= 90):
        hum_100.append(Au_short_ratio[x] *100)

for x in range(len(AgTS_hums)):
    if(int(AgTS_hums[x]) < 40):
        hum_40.append(AgTS_short_ratio[x] *100)
    elif(int(AgTS_hums[x]) >= 40 and int(AgTS_hums[x]) < 50):
        hum_50.append(AgTS_short_ratio[x] *100)
    elif(int(AgTS_hums[x]) >= 50 and int(AgTS_hums[x]) < 60):
        hum_60.append(AgTS_short_ratio[x] *100)
    elif(int(AgTS_hums[x]) >= 60 and int(AgTS_hums[x]) < 70):
        hum_70.append(AgTS_short_ratio[x] *100)
    elif(int(AgTS_hums[x]) >= 70 and int(AgTS_hums[x]) < 80):
        hum_80.append(AgTS_short_ratio[x] *100)
    elif(int(AgTS_hums[x]) >= 80 and int(AgTS_hums[x]) < 90):
        hum_90.append(AgTS_short_ratio[x] *100)
    elif(int(AgTS_hums[x]) >= 90):
        hum_100.append(AgTS_short_ratio[x] *100)       
        
for x in range(len(AuTi_hums)):
    if(int(AuTi_hums[x]) < 40):
        hum_40.append(AuTi_short_ratio[x] *100)
    elif(int(AuTi_hums[x]) >= 40 and int(AuTi_hums[x]) < 50):
        hum_50.append(AuTi_short_ratio[x] *100)
    elif(int(AuTi_hums[x]) >= 50 and int(AuTi_hums[x]) < 60):
        hum_60.append(AuTi_short_ratio[x] *100)
    elif(int(AuTi_hums[x]) >= 60 and int(AuTi_hums[x]) < 70):
        hum_70.append(AuTi_short_ratio[x] *100)
    elif(int(AuTi_hums[x]) >= 70 and int(AuTi_hums[x]) < 80):
        hum_80.append(AuTi_short_ratio[x] *100)
    elif(int(AuTi_hums[x]) >= 80 and int(AuTi_hums[x]) < 90):
        hum_90.append(AuTi_short_ratio[x] *100)
    elif(int(AuTi_hums[x]) >= 90):
        hum_100.append(AuTi_short_ratio[x] *100)
        
df['Humidity<=40%'] = pd.Series(hum_40)
df['51%-60%'] = pd.Series(hum_60)
df['61%-70%'] = pd.Series(hum_70)
df['71%-80%'] = pd.Series(hum_80)
df=df.append({'71%-80%':10},ignore_index=True)

shared = dabest.load(df,idx=('Humidity<=40%','51%-60%','61%-70%','71%-80%'))
shared.mean_diff.plot(dpi=150,swarm_label='Short Ratio(%)',contrast_label='MD')

df_time = pd.DataFrame(columns=['Noon','Afternoon','Evening','Night'])
Ag_noon = [0, 0]
Ag_afternoon = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.5, 0, 0, 0, 0]
Ag_evening = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.5, 0, 0, 0, 0, 0.5, 0, 1.0, 1.0, 1.0, 0.5, 0.3333333333333333, 0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Ag_night = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Au_noon = [0, 0, 0.2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.5, 0, 0, 0, 0, 0, 0, 1.0, 0, 0, 0, 0, 0, 0, 0, 0, 0.2, 0, 0, 0, 0, 0]
Au_afternoon = [0, 0, 0, 0, 0.25, 0, 0, 0, 0.16666666666666666, 0, 0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Au_evening = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
AgTS_noon = [0, 0, 0, 0, 0, 0, 0, 1.0]
AgTS_afternoon = [0, 0, 0, 0, 0, 0.3333333333333333, 0, 0, 0, 0, 0, 0, 0]
AgTS_evening = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
AgTS_night = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
AuTi_noon = [0.25, 0, 0, 0]
AuTi_afternoon = [0, 0, 0, 0, 0, 0, 1.0, 0, 0, 0, 0, 0, 0, 0.07142857142857142, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
AuTi_evening = [0.1111111111111111, 0.2, 0.3333333333333333, 0.1111111111111111, 0, 0.25, 0, 0.09090909090909091, 0.2, 0, 0, 0, 0, 0, 0, 0, 0, 0.5, 0, 0.3333333333333333, 0, 0.14285714285714285, 0, 0, 0.1111111111111111, 0, 0, 1.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.05555555555555555, 0, 0, 0, 0, 0.1111111111111111, 0, 0, 0, 0, 0]
AuTi_night = [0, 0, 0, 0.5, 0.3333333333333333, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.16666666666666666, 0, 0, 0, 0, 0, 0, 0.5, 0, 0, 1.0]


for x in range(len(Ag_noon)):
    Ag_noon[x] = Ag_noon[x] * 100    
for x in range(len(Ag_afternoon)):
    Ag_afternoon[x] = Ag_afternoon[x] * 100
for x in range(len(Ag_evening)):
    Ag_evening[x] = Ag_evening[x] * 100
for x in range(len(Ag_night)):
    Ag_night[x] = Ag_night[x] * 100
    
    
for x in range(len(Au_noon)):
    Au_noon[x] = Au_noon[x] * 100    
for x in range(len(Au_afternoon)):
    Au_afternoon[x] = Au_afternoon[x] * 100
for x in range(len(Au_evening)):
    Au_evening[x] = Au_evening[x] * 100
    
for x in range(len(AgTS_noon)):
    AgTS_noon[x] = AgTS_noon[x] * 100    
for x in range(len(AgTS_afternoon)):
    AgTS_afternoon[x] = AgTS_afternoon[x] * 100
for x in range(len(AgTS_evening)):
    AgTS_evening[x] = AgTS_evening[x] * 100
for x in range(len(AgTS_night)):
    AgTS_night[x] = AgTS_night[x] * 100

for x in range(len(AuTi_noon)):
    AuTi_noon[x] = AuTi_noon[x] * 100    
for x in range(len(AuTi_afternoon)):
    AuTi_afternoon[x] = AuTi_afternoon[x] * 100
for x in range(len(AuTi_evening)):
    AuTi_evening[x] = AuTi_evening[x] * 100
for x in range(len(AuTi_night)):
    AuTi_night[x] = AuTi_night[x] * 100

noon_total = Ag_noon + Au_noon + AgTS_noon +  AuTi_noon
afternoon_total = Ag_afternoon + Au_afternoon + AgTS_afternoon + AuTi_afternoon
evening_total = Ag_evening + Au_evening + AgTS_evening + AuTi_evening
night_total = Ag_night + AgTS_night + AuTi_night

df_time['Afternoon'] = pd.Series(afternoon_total)
df_time['Noon'] = pd.Series(noon_total)
df_time['Evening'] = pd.Series(evening_total)
df_time['Night'] = pd.Series(night_total)

shared = dabest.load(df_time,idx=('Noon','Night','Evening','Afternoon'))
shared.mean_diff.plot(dpi=150,swarm_label='Short Ratio(%)',contrast_label='MD')

AuTi_spring = [0.08333333333333333, 0.14285714285714285, 0.16666666666666666, 0.5, 0.3333333333333333, 0.1111111111111111, 0, 0.25, 0, 0.09090909090909091, 0.2, 0, 0, 0, 0, 0, 0, 0, 0, 0.16666666666666666, 0.2, 0.3333333333333333, 0, 0.14285714285714285, 0, 0, 0.1111111111111111, 0, 0, 1.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.07142857142857142, 0, 0, 0, 0, 0, 0.07142857142857142, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.14285714285714285, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.05555555555555555, 0, 0, 0, 0, 0.1111111111111111, 0, 0, 0, 0, 0]
AuTi_summer = [0.14285714285714285, 0, 0, 0.25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Au_autumn = [0, 0, 0.2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.5, 0, 0, 0, 0, 0, 0, 1.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.2, 0, 0, 0, 0, 0, 0, 0.25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Au_winter = [0, 0, 0, 0, 0.25, 0, 0, 0, 0.16666666666666666, 0, 0.1, 0, 0, 0, 0, 0, 0, 0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Ag_spring = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.5, 0, 0, 0, 0, 0.5, 0, 0, 0, 0, 0, 0, 1.0, 0, 1.0, 1.0, 1.0, 0.5, 0.3333333333333333, 0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Ag_summer = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.5, 0, 0, 0, 0]
AgTS_autumn = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
AgTS_winter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.3333333333333333, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.25]


for x in range(len(Ag_spring)):
    Ag_spring[x] = Ag_spring[x] * 100    
for x in range(len(Ag_summer)):
    Ag_summer[x] = Ag_summer[x] * 100
for x in range(len(AgTS_autumn)):
    AgTS_autumn[x] = AgTS_autumn[x] * 100
for x in range(len(AgTS_winter)):
    AgTS_winter[x] = AgTS_winter[x] * 100

for x in range(len(AuTi_spring)):
    AuTi_spring[x] = AuTi_spring[x] * 100    
for x in range(len(AuTi_summer)):
    AuTi_summer[x] = AuTi_summer[x] * 100
for x in range(len(Au_autumn)):
    Au_autumn[x] = Au_autumn[x] * 100
for x in range(len(Au_winter)):
    Au_winter[x] = Au_winter[x] * 100


spring_total = AuTi_spring + Ag_spring
summer_total = AuTi_summer + Ag_summer
autumn_total = Au_autumn + AgTS_autumn
winter_total = Au_winter + AgTS_winter

df_time = pd.DataFrame(columns=['Spring','Summer','Autumn','Winter'])
df_time['Spring'] = pd.Series(spring_total)
df_time['Summer'] = pd.Series(summer_total)
df_time['Autumn'] = pd.Series(autumn_total)
df_time['Winter'] = pd.Series(winter_total)

shared = dabest.load(df_time,idx=('Summer','Autumn','Winter','Spring'))
shared.mean_diff.plot(dpi=150,swarm_label='Short Ratio(%)',contrast_label='MD')
