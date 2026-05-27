#testFile
from DSReader import CSV
topQueries = CSV("br_ibge_populacao_uf/br_ibge_populacao_uf.csv")

teste = topQueries.matrice()

for line in teste:
	print(line[0], "\t", line[1], "\t",line[2], "\t")




