#!/usr/bin/python

from socket import *

"""
----------------------------------------------------------------------------------------------
Exemplo de codigo de um Cliente TCP.
----------------------------------------------------------------------------------------------
"""

# Nome ou IP utilizado para conectar ao Servidor Remoto
serverName = "localhost"
# Porta utilizada para conectar a aplicacao remota no lado Servidor
serverPort = 12000

# Cria o socket da aplicacao
clientSocket = socket(AF_INET, SOCK_STREAM)
# Configura o socket realizando o bind (vinculo) do endereco e da porta no socket
clientSocket.connect((serverName, serverPort))

# Aguarda entrada de dados pelo usuario no lado cliente
sentence = raw_input("Informe uma frase:")

# Pega a entrada do usuario, passa para o socket e envia o dado para o Servidor remoto
clientSocket.send(sentence)

# Le caracteres de retorno a partir do socket e salva string recebida do Servidor
# Note que no TCP nao ha necessidade de associar o nome do servidor, porta pelo fato de existir a conexao
modifiedSentence = clientSocket.recv(1024)

# Apenas realiza um print da mensagem retornada pelo Servidor
print "Resposta do Servidor:", modifiedSentence

# Encerrando o socket logo em seguida apos a troca de mensagens realizada com sucesso
clientSocket.close()
