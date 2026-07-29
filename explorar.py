import pandas as pd

# nomes das colunas do dataset CMAPSS
colunas = ['engine_id', 'cycle', 'setting_1', 'setting_2', 'setting_3']
colunas += [f'sensor_{i}' for i in range(1, 22)]

# lê o arquivo (ajuste o nome/caminho se for diferente)
df = pd.read_csv('train_FD001.txt', sep=' ', header=None)

# remove colunas vazias (esse dataset tem espaços extras no final de cada linha)
df = df.dropna(axis=1, how='all')

# aplica os nomes
df.columns = colunas

# explora
print(df.info())
print(df.describe())
print("Valores nulos por coluna:")
print(df.isnull().sum())
