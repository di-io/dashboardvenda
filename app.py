import streamlit as st
import plotly.express as px
from dataset import df
from utils import format_number
from graficos import graf_map_rec_estado, graf_rec_mensal, graf_rec_estado, graf_rec_categoria, graf_rec_vendedores, graf_vendas_vendedores

st.set_page_config(layout='wide')
st.title("Dashboard de vendas :shopping_trolley:")

# Criando Filtros
st.sidebar.title('Filtro Vendedores')

filtro_vendedor = st.sidebar.multiselect(
    'Vendedores',
    df['Vendedor'].unique()
)
if filtro_vendedor:
    df = df[df['Vendedor'].isin(filtro_vendedor)]
aba1, aba2, aba3 = st.tabs(['Dataset', 'Receita', 'Vendedores']) # criando abas no dashboard 

with aba1: # Colocando informações e qualquer outras coisas na aba. Usa-se with e nome da aba
    st.dataframe(df) # neste exemplo está sendo atribuído na aba1 do dataset importado no arquivo dataset.py

with aba2:
    # Neste exemplo será criado 2 colunas para trabalhar gráficos de forma separada
    coluna1, coluna2 = st.columns(2)
    with coluna1: #na mesma maneira que atribuímos dados e informações nas abas, usar de mesma forma para colunas
       # st.metric('Receita Total', df['Preço'].sum()) # Usando metric (nome da metrica, coluna do dataframe e a função que queira)
        st.metric('Receita Total',format_number(df['Preço'].sum(), 'R$'))
        st.plotly_chart(graf_map_rec_estado, use_container_width=True) # informando a metrica dentro do grafico
        st.plotly_chart(graf_rec_estado, use_container_width=True)
    with coluna2:
        st.metric('Quantidade Vendas', format_number(df.shape[0])) # o shape conta desde o inicio do dataset inicio da coluna
        st.plotly_chart(graf_rec_mensal, use_container_width=True)
        st.plotly_chart(graf_rec_categoria,use_container_width=True)
with aba3:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.plotly_chart(graf_rec_vendedores)
    with coluna2:
        st.plotly_chart(graf_vendas_vendedores)