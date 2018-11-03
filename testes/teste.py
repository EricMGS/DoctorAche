#TESTE DE ACERTOS
#Testa os acertos para uma doença específica
#Passa todas as possibilidades de combinações de sintomas dessa doença
#Verifica quantas dessas combinações retornaram um resultado correto dentre os três retornados pelo programa
#Faz o teste para todas as doenças da base de dados
#Retorna um número em porcentagem

from DoctorAche import DoctorAche as DA 
import sqlite3

class Teste:
	def __init__(self):
		self.doctor = DA()
		self.conn = sqlite3.connect()
		self.cursor = conn.cursor()

	def combinacoes(self, lista)
		pass

	def resultado(self, lista):
		doctor.get_sintomas(lista)
		doctor.provaveis()
		return doctor.resultado