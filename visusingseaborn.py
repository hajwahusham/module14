# importing necessary libraries
import pandas as pd  
import seaborn as sns 
import matplotlib.pyplot as plt 

# importing the dataset
dataset = pd.read_csv("Tips Dataset.csv")

# checking the distribution of features
sns.displot(dataset['tip'])
plt.show()

# histogram with kde parameters
sns.histplot(dataset['total_bill'], kde=True)
plt.show()

sns.kdeplot(dataset['size'])
plt.show()

# scatter plot
sns.jointplot(x='total_bill', y='tip', hue='time', data=dataset, palette='husl')
plt.show()

# pair plot
sns.pairplot(data=dataset, hue='gender', palette='magma')
plt.show()

sns.pairplot(data=dataset, hue='gender', palette='flare')
plt.show()

sns.pairplot(data=dataset, hue='gender', palette='crest')
plt.show()

sns.pairplot(data=dataset, hue='gender', palette='Set2')
plt.show()
