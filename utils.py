from dataset import df
import pandas as pd
import streamlit as st
import time

def format_number(value, prefix=''): # essa função tem o objetivo de formatar os dados da tabela
    for unit in ['', 'mil']:
        if value < 1000:
            return f'{prefix} {value:.2f} {unit}'
        value /= 1000
    return f'{prefix}{value:.2f} milhões'

# 1 - Dataframe Receita Por Estado
df_rec_estado = df.groupby('Local da compra')[['Preço']].sum() # df_rec_estado(dataframe receita por estado). É o somatório do local de compra
df_rec_estado = df.drop_duplicates(subset='Local da compra')[['Local da compra', 'lat','lon']].merge(df_rec_estado, left_on='Local da compra', right_index=True).sort_values('Preço',ascending=False)

#print(df_rec_estado)

# 2 - Dataframe Receita Mensal
df_rec_mesal = df.set_index('Data da Compra').groupby(pd.Grouper(freq='M'))['Preço'].sum().reset_index()
df_rec_mesal['Ano'] = df_rec_mesal['Data da Compra'].dt.year # Pegando o ano
df_rec_mesal['Mes'] = df_rec_mesal['Data da Compra'].dt.month_name() # Pegando o ano


# 3 - Dataframe Receitas por Catagorias
df_rec_categoria = df.groupby('Categoria do Produto')[['Preço']].sum().sort_values('Preço', ascending=False)
#print(df_rec_categoria.head()) # head faz aparecer os 5 primeiros registros


# 4 - Dataframe Vendedores
df_vendedores = pd.DataFrame(df.groupby('Vendedor')['Preço'].agg(['sum', 'count']))
print(df_vendedores)

# Função para converter arquivo CSV
@st.cache_data
def converter_csv(df):
    return df.to_csv(index=False).encode('utf-8')

def mensagem_sucesso():
    success = st.success(
                    'Arquivo baixado com sucesso',
                    icon = "✅"
                    )
    time.sleep(3)
    success.empty()