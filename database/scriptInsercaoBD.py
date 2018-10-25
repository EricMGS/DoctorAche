#SCRIPT PARA AUXILIAR O MANUSEIO DO BANCO DE DADOS
#FACILITA A INSERÇÃO, REMOÇÃO E CONSULTA DE GRANDE QUANTIDADE DE DADOS
#AJUDA EM EVITAR A CRIAÇÃO DE DUPLICIDADES
#ericmgs
#outubro de 2018

########################################################################################
# IMPORTS

import sqlite3
import os 
import sys
sys.path.append('../backend/')
from spellChecker import spellChecker as sc

#########################################################################################
# FUNÇÕES


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
	print('\nAS %d OCORRÊNCIAS MAIS SEMELHANTES À %s:' %(limite, nome))
	for word in sc(nome, lista)[:limite]:
		print(word)
	input('\n\nAperte Enter para continuar...')

def inserir(nome, lista, tabela):	
	consultar(nome, lista)
	resposta = input('\nTem certeza que deseja inserir? (S/N): ')
	if resposta == 'S':
		c.execute("insert into %s values(null, '%s')" %(tabela, nome))
		print('Elemento inserido')
	else:
		 print('\nCancelado')
	input('Aperte Enter para continuar...')

def remover(nome, lista):
	pass

###############################################################################################3
# MAIN

conn = sqlite3.connect('database')
c = conn.cursor()

opcao = menu()
while opcao != 'S':
	opcao2 = submenu()


	lista_doencas = []
	c.execute('select nome from doencas')
	for linha in c:
		lista_doencas.append(linha[0]) #[0] pois é c é uma lista de tuplas

	lista_sintomas = []
	c.execute('select nome from sintomas')
	for linha in c:
		lista_sintomas.append(linha[0]) #[0] pois c é uma lista de tuplas



	if opcao == '0': #consultar
		if opcao2 == '0': #doença
			consulta = input('Digite o nome da doença à consultar: ')
			consultar(consulta, lista_doencas)

		elif opcao2 == '1': #sintoma
			consulta = input('Digite o nome do sintoma à consultar: ')
			consultar(consulta, lista_sintomas)

		elif opcao2 == '2': #relação
			pass

	elif opcao == '1': #inserir
		if opcao2 == '0': #doença
			insercao = input('Digite o nome da doença à inserir: ')
			inserir(insercao, lista_doencas, 'doencas')

		elif opcao2 == '1': #sintoma
			insercao = input('Digite o nome do sintomas à inserir: ')
			inserir(insercao, lista_sintomas, 'sintomas')

		elif opcao2 == '1': #relação
			pass

	elif opcao == '2': #remover
		pass
	elif opcao == 'S': #sair
		pass


	conn.commit()
	opcao = menu()

c.close()
