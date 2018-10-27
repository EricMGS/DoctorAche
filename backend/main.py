#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#soprateste
from spellChecker import spellChecker as sc
import sqlite3

def provaveis(sintomas, lista_sintomas, lista_relacoes):
	d = {}
	for i in range(len(sintomas)):
		sintomas[i] = sc(sintomas[i], lista_sintomas)[0]
		c.execute("select id from sintomas where nome='%s'" %sintomas[i])
		for linha in c:
			sintomas[i] = linha[0]

	for e in lista_relacoes:
		if e[1] in sintomas:
			if e[0] in d:
				d[e[0]] += 1
			else:
				d.update({e[0]:1})
	
	d =  sorted(d, key= lambda e: d[e], reverse=True)
	for i in range(len(d)):
		c.execute("select nome from doencas where id=%d" %d[i])
		for linha in c:
			d[i] = linha[0]

	return d






conn = sqlite3.connect('../database/database')
c = conn.cursor()

lista_sintomas = []
c.execute('select nome from sintomas')
for linha in c:
	lista_sintomas.append(linha[0])

lista_relacoes = []
c.execute('select id_doenca, id_sintoma from relacoes')
for linha in c:
	lista_relacoes.append(linha)	


sintomas = input('Digite os sintomas: ').split(',')

print('As doenças mais prováveis são: ')
for e in provaveis(sintomas, lista_sintomas, lista_relacoes):
	print(e)

c.close()
