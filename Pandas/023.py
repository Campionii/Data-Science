# Crie um programa que
# Importe a biblioteca pandas como pd
# Leia um DataFrame “Salarios.csv” e nomei-o de sal
# Retorne o head do DataFrame
# Use o método .info(), para descobrir quantas entradas ele tem
# Qual é a média de Pagamento Base?
# Qual é o maior montante pago em OvertimePay?
# Qual é a profissão do ‘JOSEPH DRISCOLL’
# Qual o nome da pessoa mais bem paga
# Qual é a media de pagamento base por ano?
# Quantas profissoes únicas existem?

#import do Pandas e leitura do csv
import pandas as pd
sal = pd.read_csv('Salaries.csv')

# Head e Info
print(sal.head())
print(sal.info())#148654 entries

#Média do BasePay
print(f'A média de Pagamento Base é: {round(sal['BasePay'].mean(), 2)}')
print('--------------------------------------')

#Montante do OvertimePay
print(f'Maior OvertimePay: {round(sal['OvertimePay'].max(), 2)}')
print('--------------------------------------')

#Qual é a profissão do ‘JOSEPH DRISCOLL’
print(f'A profissão de Joseph Driscoll é {sal['JobTitle'][sal['EmployeeName'] == 'JOSEPH DRISCOLL'].values[0]}')
print('--------------------------------------')

# Qual o nome da pessoa mais bem paga
melhor_sal = sal[['TotalPay', 'EmployeeName']].groupby('EmployeeName').max().sort_values(by='TotalPay', ascending=False).head(1)
print(f'Pessoa mais bem paga {melhor_sal}')
print('--------------------------------------')

#Qual é a media de pagamento base por ano?
print(f'A média de pagamento é '
      f'\n{sal[['Year', 'TotalPay']].groupby('Year').mean().\
      sort_values(by='TotalPay', ascending=False)}')
print('--------------------------------------')

print(f'A quantidade de profissões que existem é {sal['JobTitle'].nunique()}')