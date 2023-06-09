# -*- coding: utf-8 -*-
"""Uber Data Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CA-uXTO38xcbMdktPwM5vrg8dIxuGUfq

Uber Technologies, Inc., commonly known as Uber, is an American technology company. Its services include ride-hailing, food delivery, package delivery, couriers, freight transportation, and, through a partnership with Lime, electric bicycle and motorized scooter rental

# Import the Libraries
"""

# import all the necessary libraries
import numpy as np 
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import calendar

"""# Load a uber dataset"""

uber_data=pd.read_csv('/content/Uber Drives.csv')

# view first 10 records
uber_data.head(10)

"""# Dealing with the missing values"""

#checking for misssing values if present
# python identifies missing values as NaN
uber_data.isnull().apply(pd.value_counts)

# from the above we can see apart from start date and miles every features is having a missing value
#Drop NaN values
uber_data=uber_data.dropna()

uber_data.isnull().sum()

uber_data.dtypes

# from the above you can see that start date and end date datatype is showing object even when it is a datetime 
# so we need to convert that to datetime
uber_data['START_DATE*']=pd.to_datetime(uber_data['START_DATE*'],format='%m/%d/%Y %H:%M')
uber_data['END_DATE*']=pd.to_datetime(uber_data['END_DATE*'],format='%m/%d/%Y %H:%M')

uber_data.info()

uber_data.head()

hour=[]
day=[]
day_of_week=[]
month=[]
weekday=[]
for element in uber_data['START_DATE*']:
  hour.append(element.hour)
  day.append(element.day)
  day_of_week.append(element.day_of_week)
  month.append(element.month)
  weekday.append(calendar.day_name[day_of_week[-1]])
uber_data['HOUR']=hour
uber_data['DAY']=day
uber_data['DAY_OF_WEEK']=day_of_week
uber_data['MONTH']=month
uber_data['WEEKDAY']=weekday

uber_data.head()

"""# Getting inferences from the data"""

# category feature
plt.figure(figsize=(5,5))
sns.countplot(x=uber_data['CATEGORY*'])
plt.show()

# from the above plot it is clear that most of the time uber ride is used for Business purposes

"""# How long do people travel with uber?"""

plt.hist(x='MILES*',data=uber_data,color='Purple')
plt.ylabel('Frequency')
plt.xlabel('Miles')
plt.show()

"""# What hour do most people take uber ride"""

Hour=uber_data['START_DATE*'].dt.hour.value_counts()
Hour.plot(kind='bar',color='Green')
plt.xlabel('Hours')
plt.ylabel('Frequency')
plt.title('Number of trips Vs hours')
plt.show()

"""# Purpose of the trip"""

purpose=uber_data['PURPOSE*'].value_counts()
plt.figure(figsize=(10,5))
purpose.plot(kind='bar',color='Red')
plt.ylabel('frequency')
plt.show()

"""# Which day has a highest number of trips"""

highest_trip_day=uber_data['WEEKDAY'].value_counts()
highest_trip_day.plot(kind='bar')

"""# What are number of trips per day"""

trips_per_day=uber_data['DAY'].value_counts()
trips_per_day.plot(kind='bar',color='black')