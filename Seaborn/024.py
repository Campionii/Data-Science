import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Titanic-Dataset.csv')
sns.set_style('whitegrid')

print(df.head())

sns.jointplot(x='Fare', y = 'Age', data=df, hue='Pclass', palette='viridis')
plt.show()