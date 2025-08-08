import pandas as pd
import numpy as np

# df=pd.DataFrame({'col1':[1,2,np.nan,4,5],'col2':[10,np.nan,30,40,50],'col3':['A','B','C','D',np.nan]})

# # print(df[(df['col1'] > 2) & (df['col2']>30)])  # Filter rows where col1 is greater than 2

# print(df)

# # print(df.isnull().sum())  # Count of null values in each column

# df2=df.fillna({'col1': df['col1'].mean(), 'col2': df['col2'].median(), 'col3': df['col3'].mode()[0]})  # Fill NaN values

# print(df2)

# df.fillna(0)

# df.fillna(method='bfill', inplace=True)  # Backward fill NaN values
# print(df)

# df.fillna(method='ffill', inplace=True)  # Forward fill NaN values
# print(df)

# df.dropna(axis=1,inplace=True)  # Drop columns with any NaN values
# print(df)

# print(df.describe())  # Get summary statistics of the DataFrame

df = pd.DataFrame({'A':[1,2,3,4,5,6,7,8,1,2,3],
'B':['a','b','c','d','e','f','g','h','a','b','c']})
# Check the original dataframe
print("Original dataframe:")
print(df)

print(df.duplicated())  # Check for duplicate rows

df.drop_duplicates(inplace=True)  # Drop duplicate rows
print("\nDataframe after dropping duplicates:")
print(df) 