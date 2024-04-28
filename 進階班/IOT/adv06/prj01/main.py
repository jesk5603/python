import socket

HOST = "localhost"
PORT = 5487
server_socket = socket.socket()
server_socket.bind((HOST, PORT))
server_socket.listen(5)
print("server:{}port:{}start".format(HOST, PORT))
client, addr = server_socket.accept()
print("client address:{},port:{}".format(addr[0], addr[1]))

while True:
    msg = client.recv(128).decode("utf8")
    print("Receieve Message:" + msg)
    reply = ""
    if msg == "Hi":
        reply = "Hello!"
        client.send(reply.encode("utf8"))
    elif msg == "Bye":
        client.send(b"quit")
        break
    else:
        reply = "what?"
        client.send(reply.encode("utf8"))
client.close()
server_socket.close()
