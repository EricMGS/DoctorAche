import sqlite3
import os

conn = sqlite3.connect('database')
c = conn.cursor()
os.system('clear')

print('INSERÇÃO DE SINTOMAS\n')

opcao = int(input('Digite 0 para inserir doenças ou 1 para sintomas: '))
opcao = ['doencas', 'sintomas'][opcao]

nome = input('Digite 0 para sair ou\nDigite o nome: ')
while nome != '0':
	os.system('clear')
	c.execute("insert into %s values(null, '%s')" %(opcao,nome))
	conn.commit()
	os.system('clear')
	nome = input('Digite 0 para sair ou\nDigite o nome: ')

c.close()
