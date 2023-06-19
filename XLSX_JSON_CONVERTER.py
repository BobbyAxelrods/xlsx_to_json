#!/usr/bin/env python
# coding: utf-8

from queue import Empty
import openpyxl
import numpy as np
import os 
import json
import csv 
import pandas as pd
from csv import DictReader
versioning = pd.__version__

working_path = os.getcwd()
csv_folder = os.path.join(working_path,'csv_folder')
excel_folder = os.path.join(working_path,'excel_folder')
output_folder = os.path.join(working_path,'output')
print("Running Version Pandas :%s"%(versioning))
print('Im ready to convert sir')


xlsx_fileList = [f for f in os.listdir(excel_folder) if f.endswith('.xlsx')]
csv_fileList = [f for f in os.listdir(csv_folder) if f.endswith('.csv')]

if xlsx_fileList:
    print(f'{xlsx_fileList} ready to be converted')
else:
    print('No excel files available')

if csv_fileList:
    print(f'{csv_fileList} ready to be converted')
else:
    print('No csv files available')

if xlsx_fileList: 
    for sheet in xlsx_fileList:
        fileNameExcel = str(sheet)[:-5]    
        #define total row to read , if all remove nrows=xxxx,
        #dtypes added to avoid missing leading zeros, hence added dtype =str assuming all values a string 
        df = pd.read_excel(excel_folder+'/'+sheet,nrows=10, dtype=str) 
        os.chdir(output_folder)
        df.to_json("{}.json".format(fileNameExcel), orient='records', indent=2)

        jsonlist = [f for f in os.listdir(output_folder) if f.endswith('json')]
        print('Conversion to json {} success'.format(sheet))
else: 
    print('No excel to be converted')

if csv_fileList:   
    for sheet in csv_fileList:
        fileNameExcel = str(sheet)[:-5]    
        df = pd.read_csv(csv_folder+'/'+sheet,nrows=10, dtype=str)
        os.chdir(output_folder)
        df.to_json("{}.json".format(fileNameExcel), orient='records', indent=2)

        jsonlist = [f for f in os.listdir(output_folder) if f.endswith('json')]
        print('Conversion to json {} success'.format(sheet))
    
else: 
    print('No csv to be converted')
    
df3 = pd.DataFrame (jsonlist, columns = ['List of json Available '])

df3

