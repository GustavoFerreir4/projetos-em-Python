import pandas as pd
import plotly.express as px

# 1. Carregar os dados do arquivo CSV
df = pd.read_csv("./DataSets/br_ibge_populacao_uf/br_ibge_populacao_uf.csv")

# 2. Filtrar exclusivamente para o estado de São Paulo (SP)
# Ordenamos por 'ano' para que a linha siga a ordem cronológica correta
df_sp = df[df['sigla_uf'] == 'SP'].sort_values('ano')

# 3. Criar o gráfico de linha temporal com px.line()
fig = px.line(
    df_sp, 
    x='ano', 
    y='populacao',
    title='Linha Temporal: Crescimento Populacional do Estado de São Paulo',
    labels={'ano': 'Ano', 'populacao': 'População Total'},
    markers=True  # Adiciona pontinhos em cada ano para facilitar a leitura
)

# 4. Ajustar o layout para deixar o gráfico ainda mais limpo
fig.update_layout(
    xaxis_title="Ano",
    yaxis_title="População Total",
    hovermode="x unified"  # Mostra os dados ao passar o mouse verticalmente
)

# 5. Exibir o gráfico
fig.show()


