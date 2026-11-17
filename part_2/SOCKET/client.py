import socket

obj = socket.socket()

host = "127.0.0.1"
port = 5001

obj.connect((host,port))

message = input("tupe message : ")

while message !="q":
    
    obj.send(message.encode())

    data = obj.recv(1024).decode()

    print(f"receved from server : {data}")

    message = input ("type message : ")

obj.close()