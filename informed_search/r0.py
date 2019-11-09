#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 18:32:25 2019

@author: ugoslight
"""
import os
import pandas as pd

dirr = '/Volumes/easystore/cleaned_data/'

for file in os.listdir(dirr):
    if file.endswith('.csv'):
        ff = dirr + str(file)
        csv_input = pd.read_csv(ff)
        csv_input['closest_person'] =  ''
        csv_input.to_csv(ff, index=False)