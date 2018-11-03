#TESTE DE ACERTOS
#Testa os acertos para uma doença específica
#Passa todas as possibilidades de combinações de sintomas dessa doença
#Verifica quantas dessas combinações retornaram um resultado correto dentre os três retornados pelo programa
#Faz o teste para todas as doenças da base de dados
#Retorna um número em porcentagem

import sys
sys.path.append('../backend/')
sys.path.append('')
from DoctorAche import DoctorAche as DA 
from itertools import combinations

class Teste:
	def __init__(self):
		self.doctor = DA()

		self.lista = []
		id = 0
		#cria uma matriz de sintomas, sendo cada linha uma doença
		for r in  self.doctor.lista_relacoes:
			if r[0] != id:
				id = r[0]
				#nome da doença
				self.doctor.cursor.execute("select nome from doencas where id=%d" %id)
				for linha in self.doctor.cursor:
					nome = linha[0]
				self.lista.append([nome])

			self.lista[-1].append(r[1])
			#Substitui id pelo nome
			self.doctor.cursor.execute("select nome from sintomas where id=%d" %self.lista[-1][-1])
			for linha in self.doctor.cursor:
				nome = linha[0]
			self.lista[-1][-1] = nome

	def combinacoes(self, subLista, r=None):
		comb =  list(combinations(subLista, r))
		return comb

	def resultado(self, lista):
		self.doctor.get_sintomas(lista)
		self.doctor.provaveis()
		return self.doctor.resultado

	def acertos(self, r):
		self.certas = 0
		self.erros = 0
		for subLista in self.lista:
			self.comb = self.combinacoes(subLista[1:], r)
			for combinacao in self.comb:
				self.res = self.resultado(list(combinacao))
				self.res = [e[0] for e in self.res]
				if subLista[0] in self.res:
					self.certas += 1
				else:
					self.erros += 1

		return self.certas / (self.certas + self.erros)