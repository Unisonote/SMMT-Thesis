# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 23:02:23 2023

@author: 15253
"""
import matplotlib.gridspec as gridspec
from matplotlib.lines import Line2D
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

timePeriod = np.linspace(0,3,4)
AuTi = [11.976047904191617, 10.0, 0, 0]
AuTi_count = [20,2]
AuTi_std_season = [7.406765447816746, 8.450221890577785, 0, 0]
Au = [0,0,4.964539007092199,10.81081081081081]
Au_count = [7,4]
Au_std_season = [0, 0, 4.487817891594499, 10.349911105471579]
Ag = [10.344827586206897, 1.1111111111111112, 0, 0]
Ag_count = [9,1]
Ag_std_season = [9.285131865346104, 1.4814814814814818, 0, 0]
AgTS = [0, 0, 0.0, 3.0927835051546393]
AgTS_count = [0,3]
AgTS_std_season = [0, 0, 0.0, 2.6777879338617123]


plt.figure(figsize=(20,12))
for x in range(len(timePeriod)):
    if(x < 2):    
        plt.scatter(timePeriod[x],Ag[x],c='red',s=800,marker='o')
        plt.errorbar(timePeriod[x],Ag[x],yerr=Ag_std_season[x],fmt='none',capsize=20,ecolor='black')
    elif(x >= 2):
        plt.scatter(timePeriod[x],AgTS[x],c='red',s=800,marker='o')
        plt.errorbar(timePeriod[x],AgTS[x],yerr=AgTS_std_season[x],fmt='none',capsize=20,ecolor='black') 
    x += 1
label = ['Spring','Summer','Autumn','Winter']
plt.xticks(np.arange(0,4,1),label,fontsize = 40)
plt.yticks(np.arange(0,31,5),fontsize = 40)
plt.grid(True,alpha=0.15)
#plt.title('Number of Shorted Junctions in Different Seasons',fontweight='bold',fontsize=18)
plt.xlabel('Seasons', fontsize=40)
plt.ylabel('Shorts per Chip(%)',fontsize=40)
plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter())
plt.ylim(-1,31)
#plt.text(-0.25,-7,'3/1-5/31',fontsize=40)
#plt.text(0.75,-7,'6/1-8/31',fontsize=40)
#plt.text(0.1,10,'No Measurement Taken in Spring and Summer',fontsize=40,color='red')
#plt.text(1.75,-7,'9/1-11/30',fontsize=40)
#plt.text(2.70,-7,'12/1-2/28(29)',fontsize=40)
plt.text(-0.1,22,'n =' + str(Ag_count[0]),fontsize=40)
plt.text(0.8,4,'n =' + str(Ag_count[1]),fontsize=40)
plt.text(1.8,2,'n =' + str(AgTS_count[0]),fontsize=40)
plt.text(2.8,7,'n =' + str(AgTS_count[1]),fontsize=40)
        
#pointAgTS = Line2D([0], [0], label='AgTS', color='red',marker='o',linestyle='')
#pointAg = Line2D([0], [0], label='Ag', color='white',markeredgecolor="red",marker='o',linestyle='')
#plt.legend(handles=[pointAgTS,pointAg],fontsize=40,markerscale=4,loc='upper left')


plt.figure(figsize=(20,12))
for x in range(len(timePeriod)):
    if(x < 2):    
        plt.scatter(timePeriod[x],AuTi[x],c='red',s=800,marker='o')
        plt.errorbar(timePeriod[x],AuTi[x],yerr=AuTi_std_season[x],fmt='none',capsize=20,ecolor='black')
    elif(x >= 2):
        plt.scatter(timePeriod[x],Au[x],c='red',s=800,marker='o')
        plt.errorbar(timePeriod[x],Au[x],yerr=Au_std_season[x],fmt='none',capsize=20,ecolor='black')
    x += 1
label = ['Spring','Summer','Autumn','Winter']
plt.xticks(np.arange(0,4,1),label,fontsize = 40)
plt.yticks(np.arange(0,31,5),fontsize = 40)
plt.grid(True,alpha=0.15)
#plt.title('Number of Shorted Junctions in Different Seasons',fontweight='bold',fontsize=18)
plt.xlabel('Seasons', fontsize=40)
plt.ylabel('Shorts per Chip(%)',fontsize=40)
plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter())
plt.ylim(-1,31)
#plt.text(-0.25,-7,'3/1-5/31',fontsize=40)
#plt.text(0.75,-7,'6/1-8/31',fontsize=40)
#plt.text(0.1,10,'No Measurement Taken in Spring and Summer',fontsize=40,color='red')
#plt.text(1.75,-7,'9/1-11/30',fontsize=40)
#plt.text(2.70,-7,'12/1-2/28(29)',fontsize=40)
plt.text(-0.1,21,'n =' + str(AuTi_count[0]),fontsize=40)
plt.text(0.8,20,'n =' + str(AuTi_count[1]),fontsize=40)
plt.text(1.8,13,'n =' + str(Au_count[0]),fontsize=40)
plt.text(2.8,23,'n =' + str(Au_count[1]),fontsize=40)
#pointAuTi = Line2D([0], [0], label='AuTi', color='red',marker='o',linestyle='')
#pointAu = Line2D([0], [0], label='Au', color='white',markeredgecolor="red",marker='o',linestyle='')
#plt.legend(handles=[pointAuTi,pointAu],fontsize=40,markerscale=4,loc='upper left')