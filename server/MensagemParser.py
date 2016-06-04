import json
import urllib2
from datetime import datetime

class MensagemParser:

	mensagem = ""

	def __init__(self, mensagem):
		self.mensagem = mensagem
	
	# processa a mensagem recebida do cliente
	# retorna o processamento do comando
	def processar(self):

		if self.mensagem.find('\cartola') > -1:
			palavrasMensagem = self.mensagem.split( )
			return self.getPontosDoTime( palavrasMensagem[1] )
		elif self.mensagem.find('\datahora') > -1:
			return self.getDataHora()
		elif self.mensagem.find('\donos') > -1:
			return self.getNomesDoGrupo()
		else:
			return "Comando informado nao existe."
	
	def getDataHora(self):
		now = datetime.now()
		return str(now.day) + "/" + str(now.month) + "/" + str(now.year)

	def getNomesDoGrupo(self):
		return "Mateus Eisenkraemer e Roger Bianchini"
		
	def getPontosDoTime(self, nomeDoTime):
		timeCartola = json.load(urllib2.urlopen("https://api.cartolafc.globo.com/time/" + nomeDoTime))

		atletasDoTime = "Lista de jogadores Escalados: \n"
		for atleta in timeCartola['atletas']:
			print atleta['nome']
			atletasDoTime = atletasDoTime + "\n" + atleta['nome'].encode('utf-8')

		return atletasDoTime