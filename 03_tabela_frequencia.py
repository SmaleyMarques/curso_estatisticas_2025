# %%
# Importando Bibliotecas

import pandas as pd
import sqlalchemy

# %%
# Carregando dados

df = pd.read_csv('data/points_tmw.csv')
df.head()

# %%
# Agrupando Produtos

freq_produto = (df.groupby(['descProduto'])['idTransacao']
                  .count()
                  .reset_index()
                  .rename(columns={'idTransacao': 'Freq Abs'})
                  .sort_values(by= 'Freq Abs')
                )

# %%
# Insirindo colunas restantes

freq_produto['Freq Abs Acum'] = freq_produto['Freq Abs'].cumsum()

freq_produto['%Freq'] = freq_produto['Freq Abs'] / freq_produto['Freq Abs'].sum()

freq_produto['%Freq Acum'] = freq_produto['%Freq'].cumsum()

freq_produto
# %%
# Abrindo conexão com BD SQL_Lite

engine = sqlalchemy.create_engine("sqlite:///data/tmw.db")

df.to_sql('points', engine, if_exists='replace', index=False)
