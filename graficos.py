import plotly.express as px
from utils import df_rec_estado, df_rec_mesal, df_rec_categoria, df_vendedores


graf_map_rec_estado = px.scatter_geo( #plota um mapa na tela
            df_rec_estado,
            lat = 'lat',
            lon = 'lon',
            scope = 'south america',
            size = 'Preço',
            template = 'seaborn',
            hover_name = 'Local da compra',
            hover_data = {'lat':False, 'lon':False},
            title = 'Receita por Estado'
)

graf_rec_mensal = px.line( # Plota um gráfico de linha
                df_rec_mesal,
                x = 'Mes',
                y = 'Preço',
                markers = True,
                range_y = (0, df_rec_mesal.max()),
                color = 'Ano',
                line_dash = 'Ano',
                title = 'Receita Mensal'
)

graf_rec_mensal.update_layout(yaxis_title='Receita')

graf_rec_estado = px.bar(

                df_rec_estado.head(7), # Head é usado para ffazer o top10, top5 etc. Se quiser pegar os últimos, use tails
                x = 'Local da compra',
                y = 'Preço',
                text_auto=True,
                title='Top Receitas por Estados'
)

graf_rec_categoria = px.bar(
    df_rec_categoria.head(7),
    text_auto= True,
    title= 'Top 7 Categorias com Maior Receita'

)

graf_rec_vendedores = px.bar(
    df_vendedores[['sum']].sort_values('sum', ascending=False).head(7),
    x = 'sum',
    y = df_vendedores[['sum']].sort_values('sum', ascending=False).head(7).index,
    text_auto = True,
    title= 'Top 7 Vendedores por Receita'
)

graf_vendas_vendedores = px.bar(
    df_vendedores[['count']].sort_values('count', ascending=False).head(7),
    x = 'count',
    y = df_vendedores[['count']].sort_values('count', ascending=False).head(7).index,
    text_auto=True,
    title='Top 7 Vendedores por Venda'
)