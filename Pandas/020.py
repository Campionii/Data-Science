# 1.Escreva um programa que leia, nome, idade, sexo e país de orígem.
#
# 2. Organize cada leitura como uma lista, e insira em outra lista de armazenamento.
#
# 3. Após isso, crie um data frame usando pandas com suas respectivas colunas.
#
# 4. Calcule usando pandas.
# 	4.1 média de idade
# 	4.2 moda de idade
# 	4.3 mediana da idade

import pandas as pd

lista = []
lista_menor = []

while True:
    while True:
        nome = input('Nome [sair para parar]: ').lower()
        if nome.isnumeric() == False:
            lista.append(nome)
            break
        else:
            print('digite apenas letras')

    while True:
        try:
            idade = int(input('Idade: '))
            lista.append(idade)
            break
        except ValueError:
            print('Apenas Números')

    while True:
            sexo = input('Sexo(F/M): ').strip().upper()[0]
            if sexo == 'M' or sexo == 'F':
                lista.append(sexo)
                break
            else:
                print('Digite apenas opções validas')

    pais_origem = input('País de Origem: ')

    lista_menor.append(pais_origem)
    lista.append(lista_menor[:])
    lista_menor.clear()

    continuar = input('Deseja continuar(S/N): ').strip().lower()

    if continuar == 'n':
        df = pd.DataFrame(lista,
                                columns=['nome',
                                         'idade',
                                         'sexo',
                                         'pais_origem'])

        print(df['idade'].mean())
        print(df)
        break