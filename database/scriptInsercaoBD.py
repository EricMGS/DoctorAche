import sqlite3
import os 
import sys
sys.path.append('../backend/')
from spellChecker import spellChecker as sc

def menu():
	os.system('clear')
	print('0 - Consultar')
	print('1 - Inserir')
	print('2 - Remover')
	print('\nS - Sair\n')
	op = input('Digite a opção: ')
	os.system('clear')
	return op

def submenu():
	os.system('clear')
	print('0 - Doença')
	print('1 - Sintoma')
	print('2 - Relação')
	print('\nC - Cancelar\n')
	op = input('Digite a opção: ')
	os.system('clear')
	return op

def consultar(nome, lista, limite=10):
	for word in sc(nome, lista)[:limite]:
		print(word)
	input('\n\nAperte Enter para continuar...')

def inserir(nome, lista, limite=10):
	pass

def remover(nome, lista, limite=10):
	pass


conn = sqlite3.connect('database')
c = conn.cursor()

opcao = menu()
while opcao != 'S':
	opcao2 = submenu()

	if opcao == '0': #consultar
		if opcao2 == '0': #doença
			lista_doencas = []
			c.execute('select nome from doencas')
			for linha in c:
				lista_doencas.append(linha[0])

			str1 = input('Digite o nome da doença a consultar: ')
			print('\nAs doenças mais semelhantes')
			consultar(str1, lista_doencas)

		elif opcao2 == '1': #sintoma
			lista_sintomas = []
			c.execute('select nome from sintomas')
			for linha in c:
				lista_sintomas.append(linha[0])

			str1 = input('Digite o nome do sintoma a consultar: ')
			print('\nOs sintomas mais semelhantes')
			consultar(str1, lista_sintomas)

		elif opcao2 == '2': #relação
			pass

		else:
			print('Opção inválida')

	elif opcao == '1': #inserir
		pass
	elif opcao == '2': #remover
		pass
	elif opcao == 'S': #sair
		pass
	else:
		print('Opção inválida')

	opcao = menu()

conn.commit()
c.close()
