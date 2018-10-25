#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from spellChecker import spellChecker as sc
import sqlite3

conn = sqlite3.connect('../database/database')
c = conn.cursor()

lista_sintomas = []

c.execute('select nome from sintomas')
for linha in c:
	lista_sintomas.append(linha)

sintomas = input('Digite os sintomas: ').split(',')
print(lista_sintomas)
c.close()