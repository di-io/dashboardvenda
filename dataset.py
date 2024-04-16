import json
import pandas as pd

file =  open('dados/vendas.json') # faz a leitura do arquivo json onde consta os dados
data = json.load(file) # carrega os dados json

#print(data)

df = pd.DataFrame.from_dict(data) # colaca os dados no dataframe de maneira que organizar os dados de forma tabular

#print(df)

df['Data da Compra'] = pd.to_datetime(df['Data da Compra'], format='%d/%m/%Y') # Mudando o formado da data de uma coluna

file.close()