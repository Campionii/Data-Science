
import pandas as pd
'''
#Estrurura de Séries
dic = {'a': 1, 'b': 3}
dic2 = {'a': 1, 'b': 3}
serie = pd.Series(data=dic)
serie2 = pd.Series(data=dic2)

#Soma de Séries
serie3 = serie + serie2

#Contrução Data Frame
dic3 = {'nome': ['Luis', 'Matheus', 'Henrique'], 'idade' : [50,13,43]}

df = pd.DataFrame(dic3)
#print(df)
#print(------------------)
#print(df['idade'])

#Criação por listas
listas = [['Paris', 4, 3], ['Chile', 5, 3]]
df_pais = pd.DataFrame(listas,
                       columns=['Pais',
                                'Medalhas_Ouro',
                                'Medalhas_Prata'])
print(df_pais)
print('---------------------')
print(df_pais['Medalhas_Ouro'])

#Analise Estatistica

print(df_pais['Medalhas_Ouro'].mean())
print(df_pais['Medalhas_Ouro'].mode())
print(df_pais['Medalhas_Ouro'].median())
print(df_pais['Medalhas_Ouro'].var())
print(df_pais['Medalhas_Ouro'].max())
print(df_pais['Medalhas_Ouro'].min())
'''

#ETL
df = pd.read_csv('dados_pacientes.csv')
#Analise Inicial
#print(df.head())
#print(df.isna().sum())
#print(df.info())

#ETL
#df.dropna(inplace=True)
df.dropna(inplace=True, thresh=1)
df.dropna(inplace=True, thresh=1, axis=1)

df.fillna(value=0, inplace=True)

df = df['Nome_Paciente'].replace('Paciente_1', 'João')
print(df.head())

#Analise posterior
#print(df.isna().sum())
print(df.info())
