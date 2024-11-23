import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Titanic-Dataset.csv')
sns.set_style('whitegrid')

print(df.head())

sns.boxplot(x='Pclass',y='Age', data=df,palette='tab10',flierprops= dict(marker='d', color='blue',markersize=3))
plt.show()