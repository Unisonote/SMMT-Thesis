# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 18:29:08 2023

@author: 15253
"""

import pandas as pd
import numpy as np
import os
import re
import shutil
from natsort import natsorted

c=chr(92)
dogs=np.linspace(9,17,9) #AuTi

def get_text_file_paths(folder_path):
    file_paths = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                file_paths.append(file_path)

    file_paths_series = pd.Series(file_paths)
    return file_paths_series

def extract_numbers_from_filename(filename):
    numbers = re.findall(r'\d+', filename)
    return [int(num) for num in numbers]


directory = r'F:\Thuo Research Group\10192023 Data from Martin-20231019T192206Z-001\10192023 Data from Martin\AgTS'
r = []                                                                                                            
subdirs = [x[0] for x in os.walk(directory)]                                                                            
for subdir in subdirs:                                                                                            
    files = os.walk(subdir).next()[2]                                                                             
    if (len(files) > 0):                                                                                          
        for file in files:                                                                                        
            r.append(os.path.join(subdir, file)) 
    


'''
for values in dogs:
    carbo_folder_path= r'F:\Thuo Research Group\10192023 Data from Martin-20231019T192206Z-001\10192023 Data from Martin\AgTS'
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
    print(unique_numbers)
'''