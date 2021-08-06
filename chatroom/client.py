#CLIENT 
    #1.tells username
    #2.send messages
    #3.receive messages

import socket
import select
import errno                                                                #error because there is no message received 
import os
import ast
HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 9000

my_username = input("Username: ")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)           # Create a socket
client_socket.connect((IP, PORT))                                           #connect
client_socket.setblocking(False)


username = my_username.encode('utf-8')

username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')       #In this case 10
client_socket.send(username_header + username)

print("Hello there :) , how can I help u ? \n 1.list \n 2.send \n 3.receive \n 4.exit: ")


while True:

    message = input(f'{my_username} > ')                                    # Wait for user

    if message :

        message = message.encode('utf-8')                                   # Encode message to bytes
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
        client_socket.send(message_header + message)                        #SENDING in 

    choice = message.decode('utf-8').strip()
    try:
        while True:
            if choice == "rcv":
            
                username_header = client_socket.recv(HEADER_LENGTH)             #size is defined

                if not len(username_header):                                     
                    print('Connection closed by the server')
                    sys.exit()

                username_length = int(username_header.decode('utf-8').strip())

                username = client_socket.recv(username_length).decode('utf-8') #the length of that username 

                message_header = client_socket.recv(HEADER_LENGTH)             #Now we want the message itself
                message_length = int(message_header.decode('utf-8').strip())
                message = client_socket.recv(message_length).decode('utf-8')
            
                print(f'{username} > {message}')
            if choice == "exit" :
                print('bye')
                sys.exit()
            
            if choice == "list":
                listi = client_socket.recv(HEADER_LENGTH)
                listii = listi.decode("utf-8").strip()
                print(listii)

            else:    
                break

    except IOError as e:
        
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error: {}'.format(str(e)))
            client_socket.exit()
        
        continue

    
    except Exception as e:
        # Any other exception - something happened, exit
        print('Reading error: '.format(str(e)))
        sys.exit()
        