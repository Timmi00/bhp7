from socket import create_server


def server_socket():
    with create_server(('localhost', 8080), backlog=1) as sock:
        connection, client_address = sock.accept()
        print(f'Подключение: {client_address}')
        while True:
            data = connection.recv(1024)
            if data:
                print(f'in:{data.decode()}')
                connection.sendall(input('out: ').encode())
            else:
                break
        connection.close()


server_socket()

# sock = socket.socket(
#     family=socket.AF_INET,
#     type=socket.SOCK_STREAM
# )
# sock.bind(('localhost', 8080))
# sock.listen(1)
# while True:
#     connection, client_address = sock.accept()
#     data = connection.recv(1024)
#     if data:
#         connection.sendall(data.upper())
#     else:
#         connection.close()
