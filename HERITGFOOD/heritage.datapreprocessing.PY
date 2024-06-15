# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 09:55:11 2024

@author: vemul
"""

import pandas as pd
import numpy as np
import seaborn as sns
import sweetviz as sv
from sqlalchemy import create_engine



### LOADING THE FILE ###
data = pd.read_csv(r"C:\Users\vemul\Desktop\self_ project\HERITGFOOD\HERITGFOOD.NS.csv")

data.dtypes

data.info()

# Duplicates in rows
help(data.duplicated)

duplicate = data.duplicated()  # Returns Boolean Series denoting duplicate rows.
duplicate

sum(duplicate)

# Parameters
duplicate = data.duplicated(keep = 'last')
duplicate

duplicate = data.duplicated(keep = False)
duplicate


### FINDING NULL VALUES 


print("Null values in the DataFrame:")
print(data.isnull())


print("\nNull values count per column:")
print(data.isnull().sum())

data_cleaned = data.dropna()
print("\nDataFrame after dropping rows with any null values:")
print(data_cleaned.info())

###CHEAKING NULL VALUES AGAIN

print(data_cleaned.isnull())
print(data_cleaned.isnull().sum())

data_cleaned


s=sv.analyze(data)
s.show_html()

















# Load the data
data = data_cleaned
data.to_csv('out.csv')
data = pd.read_csv(r"C:\Users\vemul\Desktop\self_ project\HERITGFOOD\out.csv")



from sqlalchemy import create_engine

#pip install pymysql
engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user = "venkat",# user
                               pw = "sanju", # passwrd
                               db = "heretagefoods")) #database


data.to_sql('hf', con = engine, if_exists = 'replace', chunksize = None, index= False) # sending data into database and connecting with Engine by using "DataFrame.to_sql()"

# To get the data From DataBase




































