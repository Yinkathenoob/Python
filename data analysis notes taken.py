
'''
PROBLEM SOLVING STEPS
1.understand prob
2.break down prob
3.dev plan
4.implement plan
5.test
6.refine
7.document

analysis vs analytics

STEPS IN DA
-data collection
-data cleaning
-data exploration
-data visualization
-data analysis
-data modeling


cargo.com -> download data sets

1.NumPy

2.Pandas
-Series: 1 dim labeled -> single column in data set
-Data frame:2 dim labeled -> multi columns

import pandas as pd
#load data from a CSV file
data = pd.read_csv('house_price.csv)

#displays the first few rows of data
data.head()

#displays the last few rows of data
data.tail()

#displays information about the columns
data.info()

#displays summary/basic statistics of each column
data.describe()


#Columns
columns = data[['col1', 'col2', 'col3']]
columns.head()

#slicing with condition
subset = data[[data]<50]
'''




