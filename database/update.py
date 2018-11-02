import sqlite3

conn = sqlite3.connect('database')
c = conn.cursor()
c.execute('delete from doencas')
c.execute('delete from sintomas')
c.execute('delete from relacoes')

def inserirRelacao(doenca, sintoma):
	c.execute("select id from doencas where nome='%s'" %doenca)
	for linha in c:
		id_doenca = linha[0]

	c.execute("select id from sintomas where nome='%s'" %sintoma)
	for linha in c:
		id_sintoma = linha[0]

	c.execute("insert into relacoes values(null, %d, %d)" %(id_doenca, id_sintoma))

def abre_arquivo():
	arquivo = open('doencas')
	return arquivo

def le_arquivo(arquivo):
	doencas = []
	sintomas = []

	linha = arquivo.readline() #NOME
	while linha != '':
		linha = arquivo.readline().replace('\n','') #nome de doença
		doencas.append([linha, 0])

		linha = arquivo.readline()#CASOS
		linha = arquivo.readline().replace('\n','') #número de casos
		doencas[-1][-1] = linha.replace('\n','')

		c.execute("insert into doencas values(null, '%s', '%s')" %(doencas[-1][0], doencas[-1][1]))

		linha = arquivo.readline() #SINTOMAS
		linha = arquivo.readline().replace('\n','') #primeiro sintoma

		while '===' not in linha:
			if linha not in sintomas:
				sintomas.append(linha)
				c.execute("insert into sintomas values(null, '%s')" %sintomas[-1])

				inserirRelacao(doencas[-1][0], sintomas[-1])

			linha = arquivo.readline().replace('\n','') #próximos sintomas
		
		linha = arquivo.readline() #NOME

arquivo = abre_arquivo()
le_arquivo(arquivo)
conn.commit()
c.close()
arquivo.close()