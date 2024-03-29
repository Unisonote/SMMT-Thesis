# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 21:43:40 2023

@author: 15253
"""
import pandas as pd
import dabest
import numpy as np

hums=[84.71,71.51333,71.001,69.3225,67.36538,70.257,72.30867,70.68688,73.19765]
short = [7.727272727272727071e-01,3.571428571428571508e-01,2.272727272727272652e-01,0.000000000000000000e+00,3.225806451612903136e-02,4.347826086956521618e-02,5.555555555555555247e-02,1.052631578947368363e-01,1.666666666666666574e-01]
time_short = [11.11111111111111, 21.666666666666668, 27.27272727272727, 11.76470588235294]
df = pd.DataFrame(columns=['61%-70%','71%-80%','81%-90%'])
hum_40 = []
hum_50 = []
hum_60=[]
hum_70=[]
hum_80=[]
hum_90=[]
hum_100=[]

for x in range(len(hums)):
    if(int(hums[x]) < 40):
        hum_40.append(short[x]*100)
        #df=df.append({'<=40':(DAA_short_ratio[x] *100)},ignore_index=True)
    elif(int(hums[x]) >= 40 and int(hums[x]) < 50):
        hum_50.append(short[x]*100)
        #df=df.append({'41-50':DAA_short_ratio[x] *100},ignore_index=True)
    elif(int(hums[x]) >= 50 and int(hums[x]) < 60):
        hum_60.append(short[x]*100)
        #df=df.append({'51-60':DAA_short_ratio[x] *100},ignore_index=True)
    elif(int(hums[x]) >= 60 and int(hums[x]) < 70):
        hum_70.append(short[x]*100)
        #df=df.append({'61-70':DAA_short_ratio[x] *100},ignore_index=True)
    elif(int(hums[x]) >= 70 and int(hums[x]) < 80):
        hum_80.append(short[x]*100)
        #df=df.append({'71-80':DAA_short_ratio[x] *100},ignore_index=True)
    elif(int(hums[x]) >= 80 and int(hums[x]) < 90):
        hum_90.append(short[x]*100)
        #df=df.append({'81-90':DAA_short_ratio[x] *100},ignore_index=True)
    elif(int(hums[x]) >= 90):        
        hum_100.append(short[x]*100)
        
df['61%-70%'] = pd.Series(hum_70)
df['71%-80%'] = pd.Series(hum_80)
df['81%-90%'] = pd.Series(hum_90)

df=df.append({'71%-80%':4.3478},ignore_index=True)
df=df.append({'71%-80%':5.5556},ignore_index=True)
df=df.append({'71%-80%':10.526315789473683},ignore_index=True)
df=df.append({'71%-80%':16.666666666666664},ignore_index=True)

shared = dabest.load(df,idx=('61%-70%','71%-80%'))
shared.mean_diff.plot(swarm_label='Ratio of Short Sport/Total(%)')
print(shared.mean_diff)


noon = [0, 0.3333333333333333, 0, 0, 0, 0, 0, 0, 0]
afternoon = [0.5, 0.5, 0.3333333333333333, 1.0, 0.3333333333333333, 1.0, 0.5, 1.0, 0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.3333333333333333, 0, 0, 0, 0.3333333333333333, 0, 0, 0.3333333333333333, 0, 0, 0, 0, 0, 0, 0, 0, 0]
evening = [0, 0, 0.3333333333333333, 1.0, 1.0, 1.0, 1.0, 0.5, 0, 1.0, 0.5, 0, 1.0, 0, 0, 0.3333333333333333, 0, 0, 1.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1.0, 0.5, 0, 0, 0, 0.3333333333333333, 0]
night = [0, 1.0, 1.0, 0.3333333333333333, 0.5, 0, 0, 0, 0, 0, 0, 0, 1.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1.0, 0, 0]

for x in range(len(noon)):
    noon[x] = noon[x] * 100    
for x in range(len(afternoon)):
    afternoon[x] = afternoon[x] * 100
for x in range(len(evening)):
    evening[x] = evening[x] * 100
for x in range(len(night)):
    night[x] = night[x] * 100


df_time = pd.DataFrame(columns=['10AM - 2PM','2PM - 6PM','6PM - 10PM','10PM - 6AM'])

df_time['2PM - 6PM'] = pd.Series(afternoon)
df_time['10AM - 2PM'] = pd.Series(noon)
df_time['6PM - 10PM'] = pd.Series(evening)
df_time['10PM - 6AM'] = pd.Series(night)

shared = dabest.load(df_time,idx=('10AM - 2PM','10PM - 6AM','2PM - 6PM','6PM - 10PM'))
shared.mean_diff.plot(swarm_label='Ratio of Short Sport/Total(%)')
print(shared.mean_diff)
