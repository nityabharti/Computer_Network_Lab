import socket
HOST = "127.0.0.1"
PORT = 12345
BUFFERSIZE = 1024
ENCODE = "utf-8"


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
    print(f"--------DNS Client is up--------\n")
    url = input("Enter the url: ")
    url = url.encode(ENCODE)
    # No need to connect, because this is a connectionless
    client.sendto(url, (HOST, PORT))

    data, addr = client.recvfrom(BUFFERSIZE)

    print(f"IP for {url.decode(ENCODE)} is {data.decode(ENCODE)}")
