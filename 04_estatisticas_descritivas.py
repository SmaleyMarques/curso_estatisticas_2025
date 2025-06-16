# %%
# Importando Bibliotecas

import pandas as pd

# %%
# Carregando dados

df = pd.read_csv('data/points_tmw.csv')
df.head()

# %%
# Calculando Estatísticas de Posição para Transações

minimo = df['qtdPontos'].min()
print('Mínimo: ', minimo)

media = df['qtdPontos'].mean()
print('Média: ', media)

quartil_1 = df['qtdPontos'].quantile(0.25)
print('1o Quartil: ', quartil_1)

mediana = df['qtdPontos'].median()
# mediana = df['qtdPontos'].quantile(0.5)
print('Mediana: ', mediana)

quartil_3 = df['qtdPontos'].quantile(0.75)
print('3o Quartil: ', quartil_3)

maximo = df['qtdPontos'].max()
print('Máximo: ', maximo)

# %%
# Usando função Pandas .describe()

df[['qtdPontos']].describe()

# %%
# Criando função para calcular estatisticas descritivas

def est_descritivas(df: pd.DataFrame):

    colunas_num =  df.select_dtypes(include={'int64', 'float64'})

    est = pd.DataFrame({})

    est['Mínimo'] = colunas_num.min()
    est['Média'] = colunas_num.mean()
    est['1o Quartil'] = colunas_num.quantile(0.25)
    est['Mediana'] = colunas_num.median()
    est['3o Quartil'] = colunas_num.quantile(0.75)
    est['Máximo'] = colunas_num.max()

    return est.T

# %%
# Calculando Estatísticas de Posição para Usuários

usuarios = df.groupby(['idUsuario']).agg(
            {
               'idTransacao': ['count'],
               'qtdPontos': ['sum']
            }).reset_index()

est_descritivas(usuarios)
# usuarios.describe()
