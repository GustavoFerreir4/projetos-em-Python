import pandas as pd
import plotly.express as px

# 1. Carregar os dados do arquivo CSV
df = pd.read_csv("./DataSets/br_ibge_populacao_uf/br_ibge_populacao_uf.csv")

# 2. Filtrar os dados apenas para o ano de 2022
df_2022 = df[df['ano'] == 2022].dropna(subset=['sigla_uf'])


populacao_total_2022 = df_2022['populacao'].sum()


# 4. Coordenadas geográficas aproximadas (centro de cada estado)
latitudes = {
    'AC': -9.02, 'AL': -9.57, 'AM': -3.47, 'AP': 1.41, 'BA': -12.96,
    'CE': -5.20, 'DF': -15.78, 'ES': -19.18, 'GO': -15.83, 'MA': -4.96,
    'MG': -18.10, 'MS': -20.77, 'MT': -12.64, 'PA': -5.54, 'PB': -7.24,
    'PE': -8.28, 'PI': -7.71, 'PR': -24.89, 'RJ': -22.39, 'RN': -5.74,
    'RO': -11.50, 'RR': 2.15, 'RS': -30.00, 'SC': -27.25, 'SE': -10.90,
    'SP': -22.26, 'TO': -10.17
}

longitudes = {
    'AC': -70.81, 'AL': -36.78, 'AM': -65.10, 'AP': -51.77, 'BA': -41.70,
    'CE': -39.53, 'DF': -47.93, 'ES': -40.34, 'GO': -49.83, 'MA': -45.27,
    'MG': -44.38, 'MS': -54.78, 'MT': -55.42, 'PA': -52.29, 'PB': -36.78,
    'PE': -37.94, 'PI': -42.71, 'PR': -51.55, 'RJ': -43.13, 'RN': -36.55,
    'RO': -63.58, 'RR': -61.38, 'RS': -53.50, 'SC': -50.49, 'SE': -37.16,
    'SP': -48.32, 'TO': -48.29
}

# 5. Adicionar as coordenadas ao DataFrame
df_2022['latitude'] = df_2022['sigla_uf'].map(latitudes)
df_2022['longitude'] = df_2022['sigla_uf'].map(longitudes)

# 6. Criar o gráfico de mapa (Scatter Geo)
fig = px.scatter_geo(
    df_2022,
    lat='latitude',
    lon='longitude',
    size='populacao',       # Tamanho da bolha pela proporção
    color='populacao',      # Cor da bolha pela proporção
    hover_name='sigla_uf',              # Mostra a sigla ao passar o mouse
    title='Mapa da Concentração da População Brasileira por Estado (2022)',
    labels={'populacao': 'População'}
)

# 7. Ajustar o mapa para focar automaticamente nas coordenadas do Brasil
fig.update_geos(
    fitbounds="locations", 
    showcountries=True, 
    countrycolor="LightGray"
)

# 8. Exibir o gráfico
fig.show()
