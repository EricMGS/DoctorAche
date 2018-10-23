#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from spellChecker import spellChecker
import sqlite3

def provaveis(sint):
	conn = sqlite3.connect('database')
	c = conn.cursor()

	p = []
	c.execute("select nome from doencas where sintoma in %s;" %str(sint))
	c.close()
	return list(c)


sintomas = input('Digite os sintomas: ').split(',')
#sintomas = [spellChecker(x, lista_sintomas) for x in sintomas]

resultado = provaveis(sintomas)

if len(resultado) == 0:
    print('Nenhuma doença identificada')
else:
    print('\nAs doenças mais prováveis são:')
    for i in range(3):
        try:
            print(i + 1, '-', resultado[i])
        except:
            break