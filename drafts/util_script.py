#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 20:32:57 2020

@author: DariusSzablowski
"""
import math
import pandas as pd

def matheus_covar2d_distribution_random_value_generator():
    return 0.0

df = pd.read_csv("simplified_with_generated_covar2d_values.csv", usecols =["simplified.significance", "foldx.ddg", "covar.2d", "Allele.Frequency", "protein"]) 

print(df[:5])

for index, row in df.iterrows():
    if math.isnan(df.loc[index, 'covar.2d']):
        print("i")
        df.loc[index, 'covar.2d'] = matheus_covar2d_distribution_random_value_generator()
        
df.to_csv('simplified_with_generated_covar2d_values.csv')
        
        
        

