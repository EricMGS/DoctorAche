import sqlite3

database = sqlite3.connect('database')
cursor = database.cursor()

arquivo = open('doencas')
doencas = []
sintomas = []
relacoes = []

linha = arquivo.readline() #NOME
while linha != '':
	linha = arquivo.readline().replace('\n','') #nome da doença
	doencas.append([linha, 0])

	linha = arquivo.readline() #CASOS
	linha = arquivo.readline().replace('\n','') #número de casos
	doencas[-1][-1] = linha

	linha = arquivo.readline() #SINTOMAS
	linha = arquivo.readline().replace('\n','') #primeiro sintoma

	while '===' not in linha:
		if linha not in sintomas:
			sintomas.append(linha)

		relacoes.append([doencas[-1][0], linha])

		linha = arquivo.readline().replace('\n','') #próximos sintomas

	linha = arquivo.readline() #NOME

#Adicionar na base de dados
cursor.execute('delete from doencas')
cursor.execute('delete from sintomas')
cursor.execute('delete from relacoes')
for d in doencas:
	cursor.execute("insert into doencas values(null, '%s', '%s')" %(d[0], d[1]))

for s in sintomas:
	cursor.execute("insert into sintomas values(null, '%s')" %s)

for r in range(len(relacoes)):
	cursor.execute("select id from doencas where nome='%s'" %relacoes[r][0])
	for linha in cursor:
		id_doenca = linha[0]

	cursor.execute("select id from sintomas where nome='%s'" %relacoes[r][1])
	for linha in cursor:
		id_sintoma = linha[0]

	cursor.execute("insert into relacoes values(null, %d, %d)" %(id_doenca, id_sintoma))

database.commit()
cursor.close()
arquivo.close()