from socket import *
import sys
serverName = 'localhost'	#Change with Server Ip if running on different Host
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
try: # tries to connect to the serverin
    print('Trying to connect to the Server...')
    clientSocket.connect((serverName, serverPort))
except:#in case the server is not running / responding
    print("Wating for the Server to respond...")
    i=1
    while i==1:#This loop will run unless the client is connected to the server (after the server is available)
        try:
            clientSocket.connect((serverName, serverPort))
            i=2
        except:
            pass
print('Connected to: ',clientSocket.getsockname())
while 1:
    op = input("Enter basic math equation (Example: 2+22/234*534):")#A single line input from the user
    clientSocket.send(op.encode())#Client will send the inputs to the server
    response = clientSocket.recv(2048)#Fetch the response from the server
    print('From Server: ', response.decode())
    while 1:#Validation loop for conitnuing or terminating the client
        inp = input('Press 1 to Continue. Press 2 to Exit ')
        if inp=='2':
            print("Disconnecting...")
            clientSocket.close()
            print("Disconnected")
            sys.exit(0)
        elif inp=='1':
            break;
        else:
            print('Choose Again')
