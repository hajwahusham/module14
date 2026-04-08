#import necessary libraries
import pandas as pd  


mydataset = {
    'Id': ['1', '2', '3', '4'],
    'Name': ['Pankaj', 'Meghna', 'David', 'Lisa'],
    'Role': ['CEO', None, None, None],
    'Salary': [100, 200, None, None]
}

df = pd.DataFrame(mydataset)
# print initial and last two values
print(df.head(2))
print("*********************************")
print(df.tail(2))
print("*********************************")
# total number of null values
print(df.isnull().sum())
print("*********************************")
# print the details
print(df.info())
print("*********************************")
# drop the rows with null values, store it in a new dataframe and print it
newdf = df.dropna()
print(newdf)
print("*********************************")
# fill the null values and print
# in salary
df["Salary"] = df["Salary"].fillna(300)
print(df)
print("*********************************")
# in Role
df["Role"] = df["Role"].fillna("CEO")
print(df)