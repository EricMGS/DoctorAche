import sqlite3
import os

conn = sqlite3.connect('database')
c = conn.cursor()
os.system('clear')

print('INSERÇÃO DE DOENÇAS\n')

nome = input('Digite 0 para sair ou\nDigite o nome da doença: ')
while nome != '0':
	os.system('clear')
	c.execute("insert into doencas values(null, '%s')" %nome)
	conn.commit()
	os.system('clear')
	nome = input('Digite 0 para sair ou\nDigite o nome da doença: ')

c.close()
