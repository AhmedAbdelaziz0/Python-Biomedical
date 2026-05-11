import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# show all data
pd.set_option('display.max_rows', 200)

# Load the data
dataset = pd.read_csv('data.csv')

# find the missing data
print(f"missing data: {dataset.isnull()}")
print(f"number of missing data:\n{dataset.isnull().sum()}")

# data discription
print(dataset.describe())

# clean the data
# Method 1 drop bad record, it can be useful if we have big dataset
dataset.dropna(inplace=True)

# Method 2 replace with mean, median, mode or any other value
# dataset.fillna(dataset.mean(), inplace=True)
# dataset.fillna(dataset.median(), inplace=True)
# dataset.fillna(dataset.mode(), inplace=True)

# data distribution
dataset.hist()
plt.show()

# visualize the data
dataset.boxplot()
plt.show()

# visualize data pares
sns.pairplot(dataset)
plt.show()

# plot specific data
sns.scatterplot(x='Duration', y='Calories', data=dataset)
plt.show()

# correlation
corr = dataset.corr()
sns.heatmap(corr, annot=True)
plt.show()
