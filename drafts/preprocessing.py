#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 10:49:39 2020

@author: DariusSzablowski
"""

import numpy as np
import pandas as pd
from hmmlearn import hmm
import random

df = pd.read_csv("simplified_with_generated_covar2d_values.csv", usecols =["simplified.significance", "foldx.ddg", "covar.2d", "Allele.Frequency", "protein"]) 
df.dropna(inplace=True)

print(df['simplified.significance'].unique()) 

df.drop(df.loc[df['simplified.significance']=='gnomAD'].index, inplace=True)
# df.drop(df.loc[df['simplified.significance']=='1/10k'].index, inplace=True)
# df.drop(df.loc[df['simplified.significance']=='common variant'].index, inplace=True)


# df = df.drop(df[not(df['simplified.significance'] == 'pathogenic' or df['simplified.significance'] == 'pathogenic')].index)

print(df[:5])

# ['pathogenic' 'benign' 'gnomAD' '1/10k' 'common variant']

for index, row in df.iterrows():
    if row[0] == 'pathogenic':
        df.loc[index, 'simplified.significance'] = 1.0 
    elif df.loc[index, 'simplified.significance'] == 'benign':
        df.loc[index, 'simplified.significance'] = 0.0 
    elif row[0] == '1/10k':
        df.loc[index, 'simplified.significance'] = 0.0
    elif row[0] == 'common variant':
        df.loc[index, 'simplified.significance'] = 0.0
#    elif row[0] == 'gnomAD':
#        df.loc[index, 'simplified.significance'] = random.uniform(0.0, 0.01)
       
df.to_csv('new_with_generated_covar_2d_values.csv')