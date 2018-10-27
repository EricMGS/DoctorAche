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

		#Conta a frequência de relações para cada doença
		self.contagem = {}
		for relacao in self.lista_relacoes:
			if relacao[1] in self.sintomas:
				if relacao[0] in self.contagem:
					self.contagem[relacao[0]] += 1
				else:
					self.contagem.update({relacao[0] : 1})

		#Atribui à resultado uma lista dos sintomas ordenada por frequência de relações
		self.resultado = sorted(self.contagem, key = lambda e: self.contagem[e], reverse = True)
		#Substitui ids de doença pelos nomes
		for i in range(len(self.resultado)):
			self.cursor.execute("select nome from doencas where id=%d" %self.resultado[i])
			for linha in self.cursor:
				self.resultado[i] = linha[0]
