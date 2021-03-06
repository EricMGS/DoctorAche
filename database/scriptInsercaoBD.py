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
sys.path.append('../modules/')
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

def submenu2():
	os.system('clear')
	print('0 - Doença')
	print('1 - Sintoma')
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
	if resposta == 'S' or resposta == 's':
		c.execute("insert into %s values(null, '%s')" %(tabela, nome))
		print('Elemento inserido')
	else:
		 print('\nCancelado')
	#input('Aperte Enter para continuar...')
	conn.commit()

def remover(nome, lista, tabela):
	consultar(nome, lista)
	nome = input('Digite o nome igual à lista: ')
	resposta = input('\nTem certeza que deseja remover? (S/N): ')
	if resposta == 'S':
		c.execute("delete from %s where nome='%s'" %(tabela, nome))
		print('Elemento removido')
	else:
		 print('\nCancelado')
	input('Aperte Enter para continuar...')

def consultaRelacao(nome, opcao): #opcao 1 para buscar doenca, opcao 2 para buscar sintoma
	if opcao == '0':
		c.execute("select id from doencas where nome='%s'" %nome)
		for linha in c:
			id_doenca = linha[0]

		c.execute("select id_sintoma from relacoes where id_doenca = %d" %id_doenca)	
		relacoes = []
		for linha in c:
			relacoes.append(linha[0])

		for i in range(len(relacoes)):
			c.execute("select nome from sintomas where id=%d" %relacoes[i])
			for linha in c:
				relacoes[i] = linha[0]

		if relacoes == []:
			print('Nenhuma relação cadastrada')
		else:
			for r in relacoes:
				print(r)

		input('\nAperte Enter para continuar...')

	elif opcao == '1':
		c.execute("select id from sintomas where nome='%s'" %nome)
		for linha in c:
			id_sintoma = linha[0]

		c.execute("select id_doenca from relacoes where id_sintoma = %d" %id_sintoma)	
		relacoes = []
		for linha in c:
			relacoes.append(linha[0])

		for i in range(len(relacoes)):
			c.execute("select nome from doencas where id=%d" %relacoes[i])
			for linha in c:
				relacoes[i] = linha[0]

		if relacoes == []:
			print('Nenhuma relação cadastrada')
		else:
			for r in relacoes:
				print(r)

		input('\nAperte Enter para continuar...')

def inserirRelacao(doenca, sintoma):
	c.execute("select id from doencas where nome='%s'" %doenca)
	for linha in c:
		id_doenca = linha[0]

	c.execute("select id from sintomas where nome='%s'" %sintoma)
	for linha in c:
		id_sintoma = linha[0]

	c.execute("insert into relacoes values(null, %d, %d)" %(id_doenca, id_sintoma))
	print("Relação inserida")
	input('\nAperte Enter para continuar...')
	
def removerRelacao(doenca, sintoma):
	c.execute("select id from doencas where nome='%s'" %doenca)
	for linha in c:
		id_doenca = linha[0]

	c.execute("select id from sintomas where nome='%s'" %sintoma)
	for linha in c:
		id_sintoma = linha[0]

	c.execute("delete from relacoes where id_doenca=%d and id_sintoma=%d" %(doenca, sintoma))
	print('Relação removida')
	input('\nAperte Enter para continuar...')

###############################################################################################
# MAIN

conn = sqlite3.connect('database')
c = conn.cursor()

opcao = menu()
while opcao != 'S':
	opcao2 = submenu()

	#Gera uma cópia local das tabelas para fazer a análise de semelhanças
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
			tipo_busca = submenu2()
			nome = input('Digite o nome a buscar: ')
			consultaRelacao(nome, tipo_busca)

	elif opcao == '1': #inserir
		if opcao2 == '0': #doença
			os.system('clear')

			insercao = input('Digite o nome da doença à inserir (0 para sair): ')
			while insercao != '0':

				lista_doencas = []
				c.execute('select nome from doencas')
				for linha in c:
					lista_doencas.append(linha[0]) #[0] pois é c é uma lista de tuplas

				inserir(insercao, lista_doencas, 'doencas')
				os.system('clear')
				insercao = input('Digite o nome da doença à inserir (0 para sair): ')
				conn.commit()

		elif opcao2 == '1': #sintoma
			os.system('clear')

			insercao = input('Digite o nome do sintomas à inserir (0 para sair): ')
			while insercao != '0':

				lista_doencas = []
				c.execute('select nome from doencas')
				for linha in c:
					lista_doencas.append(linha[0]) #[0] pois é c é uma lista de tuplas

				inserir(insercao, lista_sintomas, 'sintomas')
				os.system('clear')
				insercao = input('Digite o nome do sintomas à inserir (0 para sair): ')
				conn.commit()

		elif opcao2 == '2': #relação
			os.system('clear')
			nome_doenca = input('Digite o nome da doença (0 para sair): ')
			while nome_doenca != '0':
				nome_sintoma = input('Digite o nome do sintoma: ')
				inserirRelacao(nome_doenca, nome_sintoma)
				os.system('clear')
				nome_doenca = input('Digite o nome da doença (0 para sair): ')
				conn.commit()

	elif opcao == '2': #remover
		if opcao2 == '0': #doença
			remocao = input('Digite o nome da doença à remover: ')
			remover(remocao, lista_doencas, 'doencas')

		elif opcao2 == '1': #sintoma
			remocao = input('Digite o nome do sintoma à remover: ')
			remover(remocao, lista_sintomas, 'sintomas')

		elif opcao2 == '1': #relação

			pass

	conn.commit()
	opcao = menu()

c.close()
