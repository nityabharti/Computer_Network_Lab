# program to create an application for chat using TCP.
# importing time and socket library
import time
import socket
print("\nWelcome to Chat Room\n")
print("Initialising....\n")
time.sleep(1)
# creating a socket object
s = socket.socket()
# get local machine name
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 1234
# bind to the port
s.bind((host, port))
print(host, "(", ip, ")\n")
name = input(str("Enter your name: "))
# queue upto 1 requests
s.listen(1)
print("\nWaiting for incoming connections...\n")
# estabilshed a connection
conn, addr = s.accept()
# print message if connection established
print("Received connection from ", addr[0], "(", addr[1], ")\n")
# Receive no more than 1024 bytes
s_name = conn.recv(1024)
s_name = s_name.decode()
print(s_name, "has connected to the chat room\nEnter [e] to exit chat room\n")
# sending name to the client
conn.send(name.encode())
while True:
    # sending message to client
    message = input(str("Me : "))
    # condition to exit chat
    if message == "[e]":
      message = "Left chat room!"
      conn.send(message.encode())
      print("\n")
      break
    # sending message
    conn.send(message.encode())
    # reciving message
    message = conn.recv(1024)
    message = message.decode()
    # displaying message
    print(s_name, ":", message)