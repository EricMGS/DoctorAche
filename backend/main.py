#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from spellChecker import spellChecker

# FUNÇÕES ####################################################################################### 
def provaveis(doen, sint):
    def chave(e): #chave de ordenação
        return e[1]
    
    p = []
    #busca cada um dos sintomas em cada doença
    for d in doen:
        total = 0 #marca a quantidade de sintomas relacionados
        for s in sint:
            if s in d.sintomas:
                total += 1
        if total > 0:
            p.append([d, total])
            
    if len(p) > 1:
        p.sort(key=chave, reverse=True) #ordena de acordo com a quantidade de sintomas
    
    return [e[0].nome for e in p] #retorna a lista sem os marcadores de total


def le_arquivo(arquivo): 
    class Doenca:
        def __init__(self):
            self.nome = ''
            self.sintomas = []
    
    doencas = []
    
    line = None
    while line != '':
        doencas.append(Doenca())
        line = arquivo.readline()
        doencas[-1].nome = line.replace('\n', '')
        line = arquivo.readline()
        doencas[-1].sintomas = line.replace('\n','').split(',')
        line = arquivo.readline()
    
    arquivo.close()
    return doencas

# MAIN ##########################################################################################

arquivo = open('doencas.txt', 'r')
doencas = le_arquivo(arquivo)

lista_sintomas = []
for d in doencas:
    lista_sintomas += d.sintomas

sintomas = input('Digite os sintomas: ').split(',')
sintomas = [spellChecker(x, lista_sintomas) for x in sintomas]

resultado = provaveis(doencas, sintomas)

if len(resultado) == 0:
    print('Nenhuma doença identificada')
else:
    print('\nAs doenças mais prováveis são:')
    for i in range(3):
        try:
            print(i + 1, '-', resultado[i])
        except:
            break