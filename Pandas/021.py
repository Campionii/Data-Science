#1.Importe a Base Aula 002 - Exemplo.xlsx
#
#2. Encontre a Informação
#	2.1 - Qual país vendeu mais(Total)?
#	2.2 - Qual o melhor vendedor?
#	2.3 - Qual o melhor tipo de loja?
#	2.4 - Qual é o tipo de envio mais usado?
#	2.5 - Qual o público que mais atendemos (Gênero)?
#	2.6 - Quem fez as 3 maiores vendas?
#	2.7 - Adicione uma nova coluna comissão (Total * 5%)

import pandas as pd

df = pd.read_excel('Base Aula 002 - Exemplo .xlsx')

#País que vendeu mais
print(df[['Total', 'País']].groupby('País').sum().sort_values(by='Total', ascending=False).head(1))

#Melhor vendedor
print(df[['Total','Quantidade','Vendedor']].groupby('Vendedor').sum().sort_values(by= 'Quantidade', ascending=False).head(1))

#Qual o melhor tipo de loja
melhorLojaDf = df[['Total', 'Quantidade', 'Loja']].groupby('Loja').sum()
print(melhorLojaDf.sort_values (by= 'Quantidade', ascending=False))

#Tipo de envio mais usado
print()