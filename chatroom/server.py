import socket
import select
import os
import ast

HEADER_LENGH = 10
IP ="127.0.0.1"
PORT = 9000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# this will allows us to reconnect
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR ,1)

server_socket.bind((IP, PORT))

server_socket.listen()

sockets_list = [server_socket]
name_list = []

clients = {}

print(f'Listening for connections on {IP}:{PORT}...')

# Now we wanna receive messages

def receive_message(client_socket): 
    try:
        message_header = client_socket.recv(HEADER_LENGH)       

        if not len(message_header):                                    # If we received no data, client gracefully closed a connection.
            return False

        message_length = int(message_header.decode("utf-8").strip())
        
        return{'header': message_header, "data": client_socket.recv(message_length)}

    except:
        return False                                                   #client closed connection or lost connection


while True:                                                            # read list and write lists

    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()

            user = receive_message(client_socket)
            if user is False:
                continue
            sockets_list.append(client_socket)
            #name_list.append(user["data"].decode("utf-8"))
            clients[client_socket] = user

            print('Accepted new connection from {}:{}, username: {}'.format(*client_address, user['data'].decode('utf-8')))
        else:

            message = receive_message(notified_socket)
           
            if message is False:                                       # client disconnected

                print('Closed connection from: {}'.format(clients[notified_socket]['data'].decode('utf-8')))

                sockets_list.remove(notified_socket)                   # When disconnected we have to remove it from the list
                del clients[notified_socket]

                continue
         
            user = clients[notified_socket]

            print(f'Received message from {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')

            #if message["data"].decode("utf-8") == "rcv":
                 #print("list")
                #for client_socket in clients:                              
                 #   if client_socket != notified_socket:                    # Send list

                  #      client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])
            
            
            
            #if message["data"].decode("utf-8") == "ex":
            #    notified_socket.close()
            

            if message["data"].decode("utf-8") == "list":
                for client_socket in clients:   
                

                    client_socket.send(user["data"].decode("utf-8"))


            for client_socket in clients:                              
                if client_socket != notified_socket:                    # Send list

                    client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])
                
                   
    for notified_socket in exception_sockets:
        sockets_list.remove(notified_socket)
        del clients[notified_socket]




