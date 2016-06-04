#!/usr/bin/python

"""
----------------------------------------------------------------------------------------------
Exemplo de codigo de um Servidor TCP.
----------------------------------------------------------------------------------------------
"""

from socket import *
from MensagemParser import MensagemParser

# Porta que sera utilizada pelo Servidor para aguardar pedidos de conexao
serverPort = 12000

# Cria o socket da aplicacao
serverSocket = socket(AF_INET, SOCK_STREAM)

# Configura o socket realizando o bind (vinculo) da porta indicada no socket criado
serverSocket.bind(('', serverPort))

# Modifica o estado do socket para escuta de conexoes
serverSocket.listen(1)

print "O servidor esta pronto para receber!"

# Loop infinito onde fica aguardando e gerenciando os pedidos de conexao de clientes
while 1:
     connectionSocket, addr = serverSocket.accept()

     sentence = connectionSocket.recv(1024)

     # criar thread para processar a requisicao

     # instancia objeto que contem a logica dos comandos implementados
     messageParser = MensagemParser(sentence)
     # processa o comando passado pelo usuario
     mensagemRetorno = messageParser.processar()

     # fecha o socket
     connectionSocket.send(mensagemRetorno)
     connectionSocket.close()
