import sqlite3
import os

conn = sqlite3.connect('database')
c = conn.cursor()
os.system('clear')

print('INSERÇÃO DE DOENÇAS\n')

nome = input('Digite 0 para sair ou\nDigite o nome da doença: ')
while nome != '0':
	sintomas = []
	os.system('clear')
	s = input('Digite 0 para terminar ou\nDigite um sintoma: ')

	while s != '0':
		sintomas.append(s)
		os.system('clear')
		s = input('Digite 0 para terminar ou\nDigite um sintoma: ')

	for s in sintomas:
		c.execute("insert into doencas values('%s', '%s')" %(nome, s))
		conn.commit()
	
	os.system('clear')
	nome = input('Digite 0 para sair ou\nDigite o nome da doença: ')

c.close()
