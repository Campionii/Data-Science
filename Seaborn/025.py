import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Titanic-Dataset.csv')

print(df.info())

sns.histplot(x='Fare', data=df, bins=30, color='red')
sns.despine(left=True, top=True)
plt.grid(True)
plt.show()