import pandas as pd

#1. Importe a Vendas_Incorreto

#2. Trate todos os dados incorretos

#3. Analise estatisticamente o arquivo
import pandas as pd
from scipy.stats import chi2_contingency

df = pd.read_excel('Vendas_Incorreto.xlsx')

df.dropna(inplace=True, thresh=1)
df.dropna(inplace=True, thresh=1, axis=1)


print(df.isna())

#Produto Mais Vendido
print(df[['Quantidade', 'Total', 'Produto']].groupby('Produto').sum().sort_values(by='Quantidade', ascending=False).head(1))

#Melhor Vendedor
print(df[['Total','Quantidade','Vendedor']].groupby('Vendedor').sum().sort_values(by= 'Quantidade', ascending=False).head(1))

#Melhor Loja
melhorLojaDf = df[['Total', 'Quantidade', 'Loja']].groupby('Loja').sum()
print(melhorLojaDf.sort_values(by='Quantidade', ascending=False))

contigencia = pd.crosstab(df['País'], df['Devolucao'])
