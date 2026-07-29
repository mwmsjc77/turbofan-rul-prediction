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
# calcula o RUL: quantos ciclos faltam até a falha do motor
rul = df.groupby('engine_id')['cycle'].max().reset_index()
rul.columns = ['engine_id', 'max_cycle']

df = df.merge(rul, on='engine_id', how='left')
df['RUL'] = df['max_cycle'] - df['cycle']
df = df.drop('max_cycle', axis=1)

print(df[['engine_id', 'cycle', 'RUL']].head(10))