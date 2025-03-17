
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# Criando a tabela de dados (base de dados)

df = pd.read_excel('Vendas.xlsx')

# Criando gráfico de barras
fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")

opcoes = list(df['ID Loja'].unique())
opcoes.append('Todas as Lojas')

app.layout = html.Div(children=[
    html.H1(children='Faturamento das Lojas'),
    html.H2(children='Gráfico com o faturamento de todos os produtos separados por Loja'),

    html.Div(children='''
        Esse gráfico mostra a quantidade de produtos vendidos, não o faturamento.
    '''),
    html.Div(id='Texto'),

    dcc.Dropdown(opcoes, value='Todas as Lojas', id='lista_lojas'),

    dcc.Graph(
        id='Gráfico_Quantidade_Vendas',
        figure=fig
    )
])


# call back
@app.callback(
    Output('Gráfico_Quantidade_Vendas', 'figure'),
    Input('lista_lojas', 'value')
)
def update_output(value):
    if value == "Todas as Lojas":
        fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    else:
        tabela_filtro = df.loc[df['ID Loja'] == value, :]
        fig = px.bar(tabela_filtro, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    return fig



if __name__ == '__main__':
    app.run_server(debug=True)