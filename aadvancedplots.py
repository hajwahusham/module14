# importing necessary libraries
import pandas as pd  
import seaborn as sns 
import matplotlib.pyplot as plt 

# importing the dataset
df = pd.read_csv('Iris Dataset.csv')

# creating a barplot with species (x) and sepallengthcm(y)
sns.barplot(x='Species', y='SepalLengthCm', data=df)
plt.show()

# creating a countplot
sns.countplot(x=df['Species'], hue=df['Species'], palette='Accent')
plt.show()

# creating a boxplot
sns.boxplot(x=df['Species'], y=df['SepalWidthCm'])
plt.show()

# creating a swarm plot
sns.swarmplot(x=df['Species'], y=df['SepalWidthCm'])
plt.show()

# checking the distribution of sepalwidthcm using;
# displot
sns.displot(x=df['SepalWidthCm'], hue=df['SepalWidthCm'], palette='Paired')
plt.show()

# jointplot
sns.jointplot(x='SepalWidthCm', y='SepalLengthCm', data=df)
plt.show()

# creating a pairplot
sns.pairplot(data=df, hue='Species', palette='cubehelix')
plt.show()