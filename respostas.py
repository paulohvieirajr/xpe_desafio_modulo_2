# imports
from datetime import datetime, date 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Caminho dos datasets
diretorio_pesquisa_preferencias = 'datasets/dados_pesquisa_preferencias.csv'
diretorio_estado_regiao = 'datasets/estado_regiao.csv'

# Import dos dados dos Datasets
df_prederencias = pd.read_csv(diretorio_pesquisa_preferencias, sep='|')
df_estado_regiao = pd.read_csv(diretorio_estado_regiao, sep=';')

# Merge dos dois Dataframes
df = pd.merge(df_prederencias, df_estado_regiao, on="cod_estado")

print('Questão 1: Existem dados duplicados?')
print(f'R: {df[df.duplicated()].count().max()} \n')

print('Questão 2: Existem dados ausentes? ')
print(f'R: {df.isnull().sum()}')

# Calculo de idade com base na data de nascimento.
def calculo_idade(born): 
    born = datetime.strptime(born, "%Y-%m-%d").date() 
    today = date.today() 
    return today.year - born.year - ((today.month,  
                                      today.day) < (born.month,  
                                                    born.day)) 

df['idade'] = df['data_nascimento'].apply(calculo_idade)

print('\nQuestão 3: Desvio padão da idade pós tratamento de dados?')
print(round(df.describe().get('idade')['std'], 2))

print('\nQuestão 4: Qual região tem maior média de idade?')
print(round(df.groupby('regiao')['idade'].mean(), 2))

print('\nQuestão 5: Distribuição de idades de clientes homens de minas gerais: \n')
print(pd.crosstab(df['idade'], df['genero']).transpose())

print('\nQuestão 6: Qual o animal de maior preferencia entre as mulheres?')
print(pd.crosstab(df['genero'], df['animal_estimacao']).transpose())

print('\nQuestão 7: Qual a quantidade de pessoas de minas gerais que gostam de chá?')
print(pd.crosstab(df['estado'], df['bebida_favorita'])['Chá'])

print('\nQuestão 8: Qual a quantidade de pessoas de minas gerais que gostam de chá?')
print(pd.crosstab(df['regiao'], df['idade']).transpose()['Nordeste'])

print('\nQuestão 9: Hobbies de mulheres de São Paulo:')
print(df.query('sigla == "SP" and genero == "Feminino"').groupby('hobbies')['hobbies'].count())

print('\nQuestão 10: Maior numero de participantes: \n')
print(df.groupby('sigla')['sigla'].count())

print('\nQuestão 11: Bebida preferida do sul: \n')
print(pd.crosstab(df['bebida_favorita'], df['regiao']).transpose())

print('\nQuestão 12: Bebida preferida do sul: \n')
print(df.groupby('clima')['clima'].count())

