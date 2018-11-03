#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from spellChecker import spellChecker as sc
import sqlite3

class DoctorAche():
	def __init__(self):
		self.database = sqlite3.connect('../database/database')
		self.cursor = self.database.cursor()

		self.lista_doencas = []
		self.cursor.execute('select nome from doencas')
		for linha in self.cursor:
			self.lista_doencas.append(linha[0])

		self.lista_sintomas = []
		self.cursor.execute('select nome from sintomas')
		for linha in self.cursor:
			self.lista_sintomas.append(linha[0])

		self.lista_relacoes = []
		self.cursor.execute('select id_doenca, id_sintoma from relacoes')
		for linha in self.cursor:
			self.lista_relacoes.append(linha)
		
		self.sintomas = []
		self.contagem = {}
		self.resultado = []

	def get_sintomas(self, lista):
		self.sintomas = lista
		
	def provaveis(self):
		#Obtêm o id dos sintomas
		for i in range(len(self.sintomas)):
			self.sintomas[i] = sc(self.sintomas[i], self.lista_sintomas)[0]
			self.cursor.execute("select id from sintomas where nome='%s'" %self.sintomas[i])
			for linha in self.cursor:
				self.sintomas[i] = linha[0]

		#Conta as relações de cada doença com os sintomas informados
		self.contagem = {}
		for relacao in self.lista_relacoes:
			if relacao[1] in self.sintomas:
				if relacao[0] in self.contagem:
					self.contagem[relacao[0]] += 1
				else:
					self.contagem.update({relacao[0] : 1})

		#Conta o total de relações que cada doença retornada acima possui e calcula a probabilidade
		for d in list(self.contagem):
			total = 0
			for r in self.lista_relacoes:
				if r[0] == d:
					total += 1
			self.contagem[d] /= total
			self.contagem[d] /= len(self.contagem)
			self.contagem[d] *= 100

		#Atribui à resultado uma lista dos sintomas ordenada por frequência de relações
		self.resultado = []
		for c in self.contagem:
			self.resultado.append([self.contagem[c], c])
		self.resultado.sort(reverse=True)
		for i in range(len(self.resultado)):
			self.resultado[i] = [self.resultado[i][1], self.resultado[i][0]]

		#Substitui ids de doença pelos nomes
		for i in range(len(self.resultado)):
			self.cursor.execute("select nome from doencas where id=%d" %self.resultado[i][0])
			for linha in self.cursor:
				self.resultado[i][0] = linha[0]