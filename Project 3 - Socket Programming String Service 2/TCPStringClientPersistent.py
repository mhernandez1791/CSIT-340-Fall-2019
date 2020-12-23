from socket import *

serverName = 'localhost'
serverPort = 5000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
while True:
    sentence = input("Input a lowercase sentence. To end program enter Quit: ")
    clientSocket.send(sentence.encode())
    if sentence == "Quit":
        clientSocket.close()
        break
    modifiedSentence = clientSocket.recv(1024)
    print(modifiedSentence.decode())
