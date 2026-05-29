import pandas as pd
import plotly.express as px

# 1. Carregar os dados do arquivo CSV
df = pd.read_csv("./DataSets/br_ibge_populacao_uf/br_ibge_populacao_uf.csv")

# 2. Filtrar os dados apenas para o ano de 2025
df_2025 = df[df['ano'] == 2025]

# 3. Filtrar os três estados específicos (São Paulo, Minas Gerais e Rio de Janeiro)
estados_alvo = ['SP', 'MG', 'RJ']
df_top3 = df_2025[df_2025['sigla_uf'].isin(estados_alvo)]

# 4. Criar o gráfico de barras utilizando px.bar()
fig = px.bar(
    df_top3, 
    x='sigla_uf', 
    y='populacao',
    title='Comparação Populacional (Estados brasileiros mais populosos): <br> <b>SP, MG e RJ (Ano 2025)</b>',
    labels={'sigla_uf': 'Estado (UF)', 'populacao': 'População Total'},
    width=600,
    height=700,
)

# 5. Exibir o gráfico
fig.show()