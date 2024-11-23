#
# PROJETO NÃO FINALIZADO(EM ANDAMENTO)
#


#import de bibliotecas e df
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import numpy as np
import textwrap
import matplotlib.font_manager as fm

df = pd.read_csv('O Desafio/winemag-data-130k-v2.csv')

#Tratamento de erro de espaços vazios no dataset

for column in df.columns:
    if pd.api.types.is_numeric_dtype(df[column]):
        df[column] = df[column].fillna(0)  # Substitui valores nulos por 0
    else:
        df[column] = df[column].fillna('Valor Desconhecido')  # Substitui valores nulos por 'Valor Desconhecido'



'''
# 1. Qual país tem mais vinhos no dataset

df['country'].fillna('nao integrado', inplace=True)
df_2 = pd.DataFrame(df['country'].value_counts().head(10), columns=['count'])
print(df_2)

# Plotar gráfico
plt.figure(figsize=(10, 6))
ax = sns.barplot(data=df_2, x='count', y=df_2.index, palette='Greens')

# Adicionar título e rótulos
plt.title('Países com Mais Vinhos no Dataset (Top 10)', fontsize=16)
plt.xlabel('Vinhos (unidades)', fontsize=14)
plt.ylabel('Países', fontsize=14)

# Adicionar valores ao final de cada barra
for container in ax.containers:  # Itera pelos "containers" das barras
    ax.bar_label(container, fmt='%d', padding=3)  # Exibe valores inteiros (%d) com padding de 3px

plt.tight_layout()  # Ajusta o layout para evitar sobreposições
plt.show()



#2 Qual é a média de pontos dos vinhos por país?

# Calculando a média de pontos por país
media = df.groupby('country')['points'].mean().reset_index().head(10)
print(media)

# Criando um gráfico de barras para visualizar a média
sns.barplot(x='country', y='points', data=media, palette=[ "#C6F91F"])

# Título do gráfico e complementos
plt.title('Média de Pontos dos Vinhos por País')
plt.xlabel('PAÍSES', fontsize=12, labelpad=12)
plt.ylabel('PONTOS', fontsize=12, labelpad=12)
labels = [textwrap.fill(label, 11) for label in media['country']]
plt.xticks(ticks=range(len(media['country'])), labels=labels, ha='center')

for i, row in media.iterrows():
    plt.text(i, row['points'] + 0.5, f"{int(row['points'])}", ha='center', fontsize=10)
    
plt.show()



# 3 Existe uma correlação entre o preço e os pontos dos vinhos?

# Calcular o coeficiente de correlação de Pearson
correlation = df['price'].corr(df['points'])

# Criar o gráfico de dispersão com a linha de regressão
plt.figure(figsize=(10, 6))
sns.scatterplot(x='price', y='points', data=df, alpha=0.7)
sns.regplot(x='price', y='points', data=df, color='#C6F91F', line_kws={'lw':2})
plt.title(f'Relação entre Preço e Pontuação dos Vinhos (r={correlation:.2f})')
plt.xlabel('Preço')
plt.ylabel('Pontuação')
plt.grid(True)
plt.show()



# 4 Quais regiões têm os vinhos com as maiores classificações

more = df.groupby('province').max('points').nlargest(10, 'points').reset_index()

plt.figure(figsize=(12, 8))
sns.barplot(x='points', y='province', data=more, order=more['province'], palette=["#C6F91F"])

# Adicionando as pontuações no final das barras
for index, row in more.iterrows():
    plt.text(row['points'] + 0.5, index, f"{row['points']}", color='black', va='center')

plt.title('Regiões com Melhores Classificações de Vinhos')
plt.xlabel('Pontuação Máxima')
plt.ylabel('Região')
sns.set_style('dark')
plt.show()



# 5 Qual é a variedade de vinho mais comum no dataset?

# Identificar as 5 variedades de vinho mais comuns e suas contagens
top_varieties = df['variety'].value_counts().head(5)

# Modificar os rótulos do eixo y para incluir uma quebra de linha
top_varieties.index = [label.replace(" ", "\n") for label in top_varieties.index]

# Configurar o gráfico de barras horizontal
plt.figure(figsize=(10, 6))
bars = top_varieties.plot(kind='barh', color='#C6F91F')

# Adicionar o total de variedades no final de cada barra
for index, value in enumerate(top_varieties):
    plt.text(value, index, str(value), va='center')

# Adicionar título e rótulos
plt.title('Top 5 Variedades de Vinho Mais Comuns', fontsize=16)
plt.xlabel('Número de Ocorrências', fontsize=14)
plt.ylabel('Variedade de Vinho', fontsize=14)

# Inverter a ordem das variedades para mostrar a mais comum no topo
plt.gca().invert_yaxis()

# Exibir o gráfico
plt.show()



# 6 Como o preço dos vinhos varia entre os diferentes países?

# Remover valores nulos na coluna de preço, se houver
df = df.dropna(subset=['price'])

# Calcular a média dos preços por país
avg_price_per_country = df.groupby('country')['price'].mean().sort_values(ascending=False).head(5)

# Criar DataFrame para facilitar a manipulação
avg_price_per_country_df = avg_price_per_country.reset_index()

# Configurar o gráfico de barras horizontal
plt.figure(figsize=(16, 15))
bars = plt.barh(avg_price_per_country_df['country'], avg_price_per_country_df['price'], color='#C6F91F', height=0.5)

# Adicionar os preços ao lado de cada barra
for i, bar in enumerate(bars):
    plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2,
             f'${avg_price_per_country_df["price"][i]:.2f}',
             va='center', ha='left', fontsize=12)

# Adicionar título e rótulos aos eixos
plt.title('Média de Preço dos Vinhos por País (Top 5)', fontsize=16)
plt.xlabel('Preço Médio (USD)', fontsize=14)
plt.ylabel('País', fontsize=14)

# Exibir o gráfico
plt.tight_layout()
plt.show()



# 7 Existe alguma tendência nos pontos dos vinhos ao longo dos anos?

# Usar expressão regular para extrair o ano (caso não tenha sido feito)
df['year'] = df['title'].str.extract('\\d{4}')


sns.set_theme()
sns.set_context("paper")
sns.color_palette("tab10")

# Converter a coluna 'year' para tipo numérico (caso algum valor não tenha sido extraído corretamente)
df['year'] = pd.to_numeric(df['year'], errors='coerce')

# Filtrar para considerar apenas anos válidos (ex: entre 1900 e 2024)
df = df[(df['year'] >= 1900) & (df['year'] <= 2024)]

# Verificar se há valores nulos e removê-los
df = df.dropna(subset=['year', 'points'])

# Calcular a média dos pontos por ano
avg_points_per_year = df.groupby('year')['points'].mean().reset_index()

# Gráfico de linha para mostrar a evolução dos pontos ao longo dos anos
plt.figure(figsize=(14, 8))
sns.lineplot(data=avg_points_per_year, x='year', y='points', marker='o')

# Adicionar título e rótulos aos eixos
plt.title('Evolução dos Pontos dos Vinhos ao Longo dos Anos', fontsize=16)
plt.xlabel('Ano', fontsize=14)
plt.ylabel('Pontuação Média', fontsize=14)

# Ajuste do gráfico
plt.grid(True)
plt.tight_layout()

# Exibir gráfico
plt.show()



# 8 Qual é a variedade de vinho mais comum no dataset?

# Contar as ocorrências de cada variedade
variety_counts = df['variety'].value_counts().head(10)

# Configurar o gráfico
plt.figure(figsize=(12, 6))
variety_counts.plot(kind='bar', color='lightgreen', edgecolor='black')
sns.set_theme()
sns.set_context("paper")

# Adicionar título e rótulos
plt.title('Top 10 Variedades de Vinho Mais Comuns', fontsize=16)
plt.xlabel('Variedade', fontsize=14)
plt.ylabel('Frequência', fontsize=14)
plt.xticks(rotation=45, ha='right', fontsize=12)

# Exibir o gráfico
plt.tight_layout()
plt.show()



# 9 Como o preço dos vinhos varia entre os diferentes países?

# Remover valores nulos na coluna de preço e país
df = df.dropna(subset=['price', 'country'])

# Calcular a média de preço por país (Top 10 países com maiores preços médios)
avg_price_per_country = df.groupby('country')['price'].mean().sort_values(ascending=False).head(10)

# Configurar o gráfico de barras
plt.figure(figsize=(12, 6))
bars = avg_price_per_country.plot(kind='bar', color='orange', edgecolor='black')

# Ajustar o limite do eixo Y para atingir 90
plt.ylim(0, 90)

# Adicionar os valores no final de cada barra
for index, value in enumerate(avg_price_per_country):
    plt.text(index, value + 1.8, f'${value:.2f}', ha='center', fontsize=10, color='black')

# Adicionar título e rótulos
plt.title('Média de Preço dos Vinhos por País (Top 10)', fontsize=16)
plt.xlabel('País', fontsize=14)
plt.ylabel('Preço Médio (USD)', fontsize=14)
plt.xticks(rotation=45, ha='right', fontsize=12)

# Ajustar layout e exibir o gráfico
plt.tight_layout()
plt.show()



# 11 QUAIS SÃO OS 5 VINHOS COM A MAIOR PONTUAÇÃO ?

# Selecionando as colunas relevantes
relevant_columns = ['title', 'country', 'variety', 'price', 'points']

# Filtrando os 20 vinhos com as maiores pontuações
top_20_wines = df[relevant_columns].nlargest(20, 'points')

# Exibindo os dados completos no console
print("Os 20 Vinhos com as Maiores Pontuações:")
print(top_20_wines.to_string(index=False))  # Removendo o índice para facilitar a leitura



# 12 Quais são os 5 vinhos com o menor preço?

# Selecionando as colunas relevantes
relevant_columns = ['title', 'country', 'variety', 'price', 'points']

# Filtrando os vinhos com preços válidos (não nulos e maiores que 0)
df_valid_prices = df[df['price'].notna() & (df['price'] > 0)]

# Filtrando os 20 vinhos com os menores preços entre os preços válidos
top_5_wines = df_valid_prices[relevant_columns].nsmallest(20, 'price')

# Exibindo os dados completos no console
print("Os 5 Vinhos com os Menores Preços (Preços Válidos):")
print(top_5_wines.to_string(index=False))  # Removendo o índice para facilitar a leitura



# 13 Como a pontuação média dos vinhos varia por região?

# Agrupar por região e calcular a média da pontuação
media_por_regiao = df.groupby('region_1')['points'].mean().reset_index()

# Ordenar por pontuação média (do maior para o menor)
media_por_regiao = media_por_regiao.sort_values(by='points', ascending=False)

# Separar as melhores e piores regiões
top_5_regioes = media_por_regiao.head(5)
pior_5_regioes = media_por_regiao.tail(5)

# Combinar as duas partes para exibir no mesmo gráfico
combinado = pd.concat([top_5_regioes, pior_5_regioes])


# Função para truncar texto após o terceiro espaço ou hífen
def truncate_name(region_name, max_count=3):
    count = 0
    for i, char in enumerate(region_name):
        if char == ' ' or char == '-':
            count += 1
        if count == max_count:  # Se tiver 3 espaços ou hífens, corta
            return region_name[:i] + '...'  # Trunca e adiciona '...'

    return region_name  # Se não atingir 3 espaços ou hífens, retorna o nome completo


# Aplicar a função de truncamento aos nomes das regiões
top_5_regioes['region_1'] = top_5_regioes['region_1'].apply(truncate_name)
pior_5_regioes['region_1'] = pior_5_regioes['region_1'].apply(truncate_name)

# Criar o gráfico
plt.figure(figsize=(12, 8))

# Plot para as melhores regiões com gradiente verde
sns.barplot(x='points', y='region_1', data=top_5_regioes, palette='Greens', label='Melhores Regiões')

# Plot para as piores regiões com gradiente vermelho
sns.barplot(x='points', y='region_1', data=pior_5_regioes, palette='Reds', label='Piores Regiões')

# Ajustar os rótulos das regiões (agora já truncados) no eixo Y
plt.yticks(ticks=range(len(top_5_regioes) + len(pior_5_regioes)),
           labels=list(top_5_regioes['region_1']) + list(pior_5_regioes['region_1']))

# Adicionar título e rótulos com fonte itálica
plt.title('Top 5 Melhores e Piores Regiões com base na Pontuação Média', fontstyle='italic')
plt.xlabel('Pontuação Média', fontstyle='italic')
plt.ylabel('Região', fontstyle='italic')


# Exibir o gráfico
plt.show()



# 14 Qual é a distribuição dos preços dos vinhos?

# Filtrando os dados para garantir que apenas vinhos com preços válidos sejam analisados
df_valid_prices = df[df['price'].notna() & (df['price'] > 0)]

# Estatísticas descritivas sobre os preços
price_stats = df_valid_prices['price'].describe()
print("Estatísticas descritivas dos preços dos vinhos:")
print(price_stats)

# Criando o gráfico de distribuição dos preços com limite até 200
plt.figure(figsize=(12, 7))

# Ajuste do gráfico com KDE e bins, utilizando uma paleta de cores customizada
sns.histplot(df_valid_prices['price'], bins=50, kde=True, color='#1F77B4', linewidth=1.5, fill=True)

# Ajuste do limite do eixo X para não cortar os valores extremos
plt.xlim(0, df_valid_prices['price'].quantile(0.95))

# Adicionando as linhas de média e mediana
mean_price = df_valid_prices['price'].mean()
median_price = df_valid_prices['price'].median()

# Linha média (azul claro) e linha mediana (laranja)
plt.axvline(mean_price, color='#FF7F0E', linestyle='--', label=f'Média: {mean_price:.2f}', linewidth=2)
plt.axvline(median_price, color='#2CA02C', linestyle='-', label=f'Mediana: {median_price:.2f}', linewidth=2)

# Título e rótulos com cores e espaçamento
plt.title('Distribuição de Preços dos Vinhos (R$)', fontsize=18, loc='left', fontweight='bold', family='Arial', color='#1F77B4', pad=25)
plt.xlabel('Preço dos Vinhos (R$)', fontsize=14, fontweight='bold', family='Arial', color='#333333',)
plt.ylabel('Frequência', fontsize=14, fontweight='bold', family='Arial', color='#333333')

# Ajustando o grid para tornar mais elegante
plt.grid(True, linestyle='--', alpha=0.7)

# Adicionando a legenda com um fundo translúcido
plt.legend(loc='upper right', fontsize=12, frameon=True, facecolor='white', edgecolor='#333333', framealpha=0.7)

# Exibir o gráfico
plt.show()



# 15 Qual é a distribuição dos preços dos vinhos?

# Agrupando por tipo de vinho e calculando a média das pontuações
top_10_varieties = df.groupby('variety')['points'].mean().reset_index()

# Ordenando pelas 10 maiores pontuações
top_10_varieties = top_10_varieties.sort_values('points', ascending=False).head(10)

# Adicionando o valor do primeiro item ao final para fechar o gráfico de radar
top_10_varieties = pd.concat([top_10_varieties, top_10_varieties.iloc[:1]], ignore_index=True)

# Criando a tabela com os dados
table_data = pd.DataFrame({
    'Variedade de Vinho': top_10_varieties['variety'],
    'Pontuação Média': top_10_varieties['points']
})

# Exibindo a tabela no console
print(table_data)
'''