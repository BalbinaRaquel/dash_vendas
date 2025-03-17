
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# Criando a tabela de dados (base de dados)

df = pd.read_excel('Vendas.xlsx')

# Criando gráfico de barras
fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")



app.layout = html.Div(children=[
    html.H1(children='Faturamento das Lojas'),
    html.H2(children='Gráfico com o faturamento de todos os produtos separados por Loja'),

    html.Div(children='''
        Esse gráfico mostra a quantidade de produtos vendidos, não o faturamento.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)