# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 18:57:24 2016

@author: rtfly
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from scipy import stats
from projdictionaries import *

# Ensuring output is not truncated
pd.set_option('display.max_columns', 30)

df1 = pd.read_csv("~/Vehicles_2015.csv")

df1.describe() 

df1 = pd.read_csv("~/Vehicles_2015.csv", 
                  dtype={"Vehicle_Reference":str,
                         "Vehicle_Type":str,
                         "Towing_and_Articulation":str,
                         "Vehicle_Manoeuvre":str,
                         "Vehicle_Location-Restricted_Lane":str,
                         "Junction_Location":str,
                         "Skidding_and_Overturning":str,
                         "Hit_Object_in_Carriageway":str,
                         "Vehicle_Leaving_Carriageway":str,
                         "Hit_Object_off_Carriageway":str,
                         "1st_Point_of_Impact":str,
                         "Was_Vehicle_Left_Hand_Drive?":str,
                         "Journey_Purpose_of_Driver":str,
                         "Sex_of_Driver":str,
                         "Age_Band_of_Driver":str,
                         "Propulsion_Code":str,
                         "Driver_IMD_Decile":str,
                         "Driver_Home_Area_Type":str,
                         "Vehicle_IMD_Decile":str}, na_values="-1")

df1.head(5)
 
df2 = pd.read_csv("~/Accidents_2015_Datetime.csv",
                  dtype={"Day_of_Week":str}, na_values="-1")

df2.head(5)

# Merging df1 and df2 to form base table 
df = pd.merge(df1, df2, on='Accident_Index', how='inner')

df.head(5)

# Removing some unnecessary columns
df.drop(["Vehicle_Reference","Towing_and_Articulation","Was_Vehicle_Left_Hand_Drive?","Propulsion_Code"], 
        1, inplace = True)

df.describe().dropna()

#Some column names have characters, such as hyphens and brackets, that may be problematic
df.rename(columns={'Vehicle_Location-Restricted_Lane': 'Vehicle_Location_Restricted_Lane', 
                   'Engine_Capacity_(CC)':'Engine_Capacity_CC', 
                   '1st_Point_of_Impact':'Fst_Point_of_Impact'}, inplace=True)

df.info()

df.count().max()

# Format the 'Date' column to datetime datatype
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')

# Format the 'Time' column to datetime datatype
df['Time'] = pd.to_datetime(df['Time'], format='%H:%M')

df.Time[:10]

# Function to build value indexes, based on the order in which Python reads
# unique column values
def catindexer(mylist, mydict): # pass a list, then a dictionary
    # blank list to capture corresponding dictionary values
    catlabels = []
    for i in mylist:
        # checks the item in list against the key values in dictionary
        if i in mydict:
            # appends the dictionary value to the list in order of list items
            catlabels.append(mydict[i])
    return catlabels
   
# Creating lists of unique values for selected categorical columns 
lvehtype = df.Vehicle_Type.unique()
lvehmano = df.Vehicle_Manoeuvre.unique()
lvehloc = df.Vehicle_Location_Restricted_Lane.unique()
ljuncloc = df.Junction_Location.unique()
lskidot = df.Skidding_and_Overturning.unique()
lhitincw = df.Hit_Object_in_Carriageway.unique()
lvehlvcw = df.Vehicle_Leaving_Carriageway.unique()
lhitoffcw = df.Hit_Object_off_Carriageway.unique()
lfstptimp = df.Fst_Point_of_Impact.unique()
ljrnypurp = df.Journey_Purpose_of_Driver.unique()
lsexdrvr = df.Sex_of_Driver.unique()
lageband = df.Age_Band_of_Driver.unique()
lhomearea = df.Driver_Home_Area_Type.unique()
ldayofwk = df.Day_of_Week.unique()

# Running catindexer on those lists and their corresponding dictionaries
vlvehtype = catindexer(lvehtype, dvehtype)
vlvehmano = catindexer(lvehmano, dvehmano)
vlvehloc = catindexer(lvehloc, dvehloc)
vljuncloc = catindexer(ljuncloc, djuncloc)
vlskidot = catindexer(lskidot, dskidot)
vlhitincw = catindexer(lhitincw, dhitincw)
vlvehlvcw = catindexer(lvehlvcw, dvehlvcw)
vlhitoffcw = catindexer(lhitoffcw, dhitoffcw)
vlfstptimp = catindexer(lfstptimp, dfstptimp)
vljrnypurp = catindexer(ljrnypurp, djrnypurp)
vlsexdrvr = catindexer(lsexdrvr, dsexdrvr)
vlageband = catindexer(lageband, dageband)
vlhomearea = catindexer(lhomearea, dhomearea)
vldayofwk = catindexer(ldayofwk, ddayofwk)

# Test category references from projdictionaries script
print(lvehloc)
print(vlvehloc)

# Start cleaning by checking for missing values 
df.isnull().any()

# Function to return missing value counts, in order to find patterns
def missing_count(colx):
  return sum(colx.isnull())

# Use the apply function to run missing_count on the dataframe  
df.apply(missing_count, axis=0)
# Two columns have far too many missing values to be useful, drop them
df.drop(["Driver_IMD_Decile","Vehicle_IMD_Decile"], 1, inplace = True)

# For loop to identify and display group with highest count for columns with missing data,
# object datatype, to replace missing values (adapted from code by Kaggle member @apryor6)
string_data = df.select_dtypes(include=["object"]) # Selects columns of type 'object'
# list comprehension to identify columns with missing values
missing_columns = [col for col in string_data if string_data[col].isnull().any()]
for col in missing_columns:
    # Prints nicely formatted results, referencing col and string_data[col].value_counts().idxmax()
    print("Group with highest count for {0}:\n{1}\n".format
          (col,string_data[col].value_counts().idxmax()))
del string_data

# Filling missing data for variables where most common value is appropriate
df.loc[df.Vehicle_Type.isnull(),"Vehicle_Type"] = '9'
df.loc[df.Vehicle_Manoeuvre.isnull(),"Vehicle_Manoeuvre"] = '18'
df.loc[df.Vehicle_Location_Restricted_Lane.isnull(),"Vehicle_Location_Restricted_Lane"] = '0'
df.loc[df.Junction_Location.isnull(),"Junction_Location"] = '0'
df.loc[df.Skidding_and_Overturning.isnull(),"Skidding_and_Overturning"] = '0'
df.loc[df.Hit_Object_in_Carriageway.isnull(),"Hit_Object_in_Carriageway"] = '0'
df.loc[df.Vehicle_Leaving_Carriageway.isnull(),"Vehicle_Leaving_Carriageway"] = '0'
df.loc[df.Fst_Point_of_Impact.isnull(),"Fst_Point_of_Impact"] = '1'

# Filling missing data for variables with an 'unknown' or equivalent option
df.loc[df.Sex_of_Driver.isnull(),"Sex_of_Driver"] = '3'
df.loc[df.Journey_Purpose_of_Driver.isnull(),"Journey_Purpose_of_Driver"] = '15'

# Create an 'unknown' level for Driver_Home_Area_Type, which has a high numbers of missings values
df.loc[df.Driver_Home_Area_Type.isnull(),"Driver_Home_Area_Type"] = '0'
# Update dictionary!
dhomearea['0'] = "Unknown"
# Update indexes
lhomearea = df.Driver_Home_Area_Type.unique()
vlhomearea = catindexer(lhomearea, dhomearea)

sns.set_style("whitegrid")
labels = vlvehtype
tips = sns.load_dataset("tips")
ax = sns.boxplot(x=df["Vehicle_Type"].dropna(), y=df["Age_of_Vehicle"].dropna(),
                 data=tips, palette="husl", order=lvehtype)
plt.xticks = (ax.set_xticklabels(labels, rotation=75))

# Specific dates and times have too much variation, extract month into a new column
df['Month'] = pd.to_datetime(df['Date']).dt.month

# Extract hour into a new column
df['Hour'] = pd.to_datetime(df['Time'], format='%H:%M').dt.hour

# Distribution plot for time of accident
sns.distplot(df['Hour'].dropna())
plt.xlabel('Time of Accident')

# Using most frequent observation to fill  missing values
df.loc[df.Hour.isnull(),"Hour"] = 17.0

# Countplot for vehicle type       
sns.set_style("whitegrid")
labels = vlvehtype
ax = sns.countplot(x='Vehicle_Type', data=df, order=lvehtype)
plt.xticks = (ax.set_xticklabels(labels, rotation=75))  

# Countplot for day of week
sns.set_style("whitegrid")
labels = vldayofwk
ax = sns.countplot(x='Day_of_Week', data=df, order=ldayofwk)
plt.xticks = (ax.set_xticklabels(labels, rotation=75))    

# Countplot for month
sns.set_style("whitegrid")
sns.countplot(x='Month', data=df) 

df["Month"].value_counts()

# Function to count accident types
def accident_counter(colx):
    count = 0
    for i in colx:
        if i != '0':
            count += 1
    return count
    
count_skid_ot = accident_counter(df['Skidding_and_Overturning'])
print(count_skid_ot)

count_hit_in_cw = accident_counter(df['Hit_Object_in_Carriageway'])
print(count_hit_in_cw)

count_veh_lv_cw = accident_counter(df['Vehicle_Leaving_Carriageway'])
print(count_veh_lv_cw)

count_hit_off_cw = accident_counter(df['Hit_Object_off_Carriageway'])
print(count_hit_off_cw)

# Preparing a small dataset
accidentscounts = {
    'Accident_type':['skid_overturn', 'hit_in_carriageway', 'vehicle_left_carriageway', 'hit_off_carriageway'],
    'Frequency':[count_skid_ot, count_hit_in_cw, count_veh_lv_cw, count_hit_off_cw]}

dfaccidents = pd.DataFrame(accidentscounts, columns = ['Accident_type','Frequency'])
dfaccidents.head(5)

# Barplot showing most frequent accident type
sns.set_style("whitegrid")
tips = sns.load_dataset("tips")
ax = sns.barplot(x=dfaccidents['Accident_type'], y=dfaccidents['Frequency'], 
                 data=tips, palette="Set3")

# Crosstabulation of vehicle type and sex of driver
pd.crosstab(df.Sex_of_Driver, df.Vehicle_Type, margins=True)

# Distribution plot focused on most concentrated range of values
sns.distplot(df['Engine_Capacity_CC'].dropna(),bins=80, kde=False)
plt.xlabel('Engine Capacity Distribution')
plt.xlim(0,4000)

df.median(0)

# Creating series of male and female age values
male_ages = df[df['Sex_of_Driver'] == '1']['Age_of_Driver']
male_ages = male_ages.dropna()

female_ages = df[df['Sex_of_Driver'] == '2']['Age_of_Driver']
female_ages = female_ages.dropna()

male_ages.mean()
male_ages.median()

female_ages.mean()
female_ages.median()

# T-test to compare means of female_ages and male_ages
stats.ttest_ind(female_ages, male_ages, equal_var=False)

# Countplot showing driver home area distribution
sns.set_style("whitegrid")
labels = vlhomearea
ax = sns.countplot(x='Driver_Home_Area_Type', data=df, order=lhomearea)
plt.xticks = (ax.set_xticklabels(labels, rotation=75))
