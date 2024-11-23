import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Titanic-Dataset.csv')

print(df.head())

sns.FacetGrid(x='Sex', data=df, hue='Survived')
plt.show()
