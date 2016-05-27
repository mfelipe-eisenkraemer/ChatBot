class MensagemParser:
	mensagem = ""

	def __init__(self, mensagem):
		self.mensagem = mensagem
	
	# processa a mensagem recebida do cliente
	# retorna o processamento do comando
	def processar(self):
		# se achou o comando \even
		if self.mensagem.find('\even') > -1:
			even
		# se achou o comando \prime
		elifself.mensagem.find('\prime') > -1:
			prime
		# se nao achou nenhum dos anteriores
		else:
			even
	
	def prime():
		print "n is a prime number\n"
		
	def even():
		print "n is an even number\n"