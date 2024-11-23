import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Titanic-Dataset.csv')
sns.set_style('whitegrid')

print(df.head())

sns.swarmplot(x='Pclass',y='Age', data=df,palette='magma')
plt.show()