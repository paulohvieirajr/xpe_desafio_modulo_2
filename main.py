
# imports
from datetime import datetime, date 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

born='2000-06-01'
print("Born :",born) 
  
#Identify given date as date month and year 
born = datetime.strptime(born, "%Y-%m-%d").date() 
print(born)

#Get today's date 
today = date.today() 

print("Age :", 
      today.year - born.year - ((today.month, 
                                          today.day) < (born.month, 
                                                        born.day)))

exit

# Caminho dos datasets
diretorio_pesquisa_preferencias = 'datasets/dados_pesquisa_preferencias.csv'
diretorio_estado_regiao = 'datasets/estado_regiao.csv'

# Carregando dados dos Datasets
df_prederencias = pd.read_csv(diretorio_pesquisa_preferencias, sep='|')
df_estado_regiao = pd.read_csv(diretorio_estado_regiao, sep=';')

# print('\nQuantidade de linhas e colunas dos datasets: \n')
# print(df_prederencias.shape)
#print(df_estado_regiao.shape)

# print('\nInformações dos datasets: \n')
# print(df_prederencias.info())
#print(df_estado_regiao.info())

# print('\nPrimeiras linhas do Dataset: \n')
# print(df_prederencias.head())

# print('\nUltimas linhas do Dataset: \n')
# print(df_prederencias.tail())

def calculo_idade(born): 
    born = datetime.strptime(born, "%Y-%m-%d").date() 
    today = date.today() 
    return today.year - born.year - ((today.month,  
                                      today.day) < (born.month,  
                                                    born.day)) 

df_prederencias['idade'] = df_prederencias['data_nascimento'].apply(calculo_idade)

print('\nEstatisticas descritivas sobre o dataset:\n')
print(round(df_prederencias.describe(), 2))

print('\nTranspose de estatisticas descritivas sobre o dataset:\n')
print(round(df_prederencias.describe().transpose(), 2))

print('\nContagem de valores unicos:\n')
print(df_prederencias['genero'].value_counts())

#contagem_generos = df_prederencias['genero'].value_counts()
#print(contagem_generos.plot.barh())

df = pd.merge(df_prederencias, df_estado_regiao, on="cod_estado")
print('Dataframe resultado do merge:')
# print(df.info())
print(df.head())
# print(df.tail())

print('\nMerges de dados: \n')
print(pd.crosstab(df['hobbies'], df['regiao']))

print('\nAnimal de preferencia entre as mulheres: \n')
print(pd.crosstab(df['genero'], df['animal_estimacao']))

print('\nMedia de idade por região: \n')
print(round(df.groupby('regiao')['idade'].mean()), 2)

print('\n\nAnalise exploratoria dos dados:\n')

print('Hobbies de mulheres de São Paulo:')
print(df.query('sigla == "SP" and genero == "Feminino"').groupby('hobbies')['hobbies'].count().max())

print('\nIdentificar dados duplicados:\n')
print(df[df.duplicated()])
print(df[df.duplicated()].count())

print('\nPreferecia pelo frio: \n')
print(df.groupby('clima')['clima'].count())

print('\nMaior numero de participantes: \n')
print(df.groupby('sigla')['sigla'].count())

print('\nRemover dados duplicados: \n')
print(df.shape)
df.drop_duplicates(inplace=True)
print(df.shape)

print('\nAgrupamento de hobbies e estados: \n')
print(pd.crosstab(df['bebida_favorita'], df['estado']).transpose())

print('\nDados nulos: \b')
print(df.isnull().sum())

print('\nBebida preferida do sul: \n')
print(pd.crosstab(df['bebida_favorita'], df['regiao']).transpose())

print('\nPegando valores mais usados: \n')
print(df['animal_estimacao'].mode())

