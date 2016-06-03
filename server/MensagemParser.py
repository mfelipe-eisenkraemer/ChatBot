import json
import urllib2

class MensagemParser:

	mensagem = ""

	def __init__(self, mensagem):
		self.mensagem = mensagem
	
	# processa a mensagem recebida do cliente
	# retorna o processamento do comando
	def processar(self):

		# se achou o comando \even
		if self.mensagem.find('\even') > -1:
			return self.getPontosDoTime()
		# se achou o comando \prime
		elif self.mensagem.find('\prime') > -1:
			return self.prime()
		# se nao achou nenhum dos anteriores
		else:
			return self.getPontosDoTime()
	
	def prime(self):
		print "n is a prime number\n"
		return 1
		
	def getPontosDoTime(self):
		resposta = json.load(urllib2.urlopen("https://api.cartolafc.globo.com/time/FeelsGoodMan"))
		print resposta
		return resposta['pontos']