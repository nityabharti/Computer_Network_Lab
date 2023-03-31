import socket
HOST = "127.0.0.1"
PORT = 12345
BUFFERSIZE = 1024
ENCODE = "utf-8"
#  Dummy Data
urls = {
    "www.google.com": "123.111.2.21",
    "www.facebook.com": "4.2.3.1",
    "www.amazon.in": "64.42.23.1"
}
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
    server.bind((HOST, PORT))
    print(f"DNS Server is up and running on port {PORT}")
    # receives data and address of the client
    data, addr = server.recvfrom(BUFFERSIZE)
    print(f"Received data from {addr}")
    url = data.decode(ENCODE)
    print(f"[{addr}]: requesting ip for {url}")
    isFound = False

    # Checking for data in its memory
    for key in urls.keys():
        if url in key:
            isFound = True
            ip = urls[key]
            ip = ip.encode(ENCODE)
            # sends the results to the client
            server.sendto(ip, addr)
            print(f"IP for {url} is found")
    if not isFound:
        msg = "URL not found"
        msg = msg.encode()
        server.sendto(msg, addr)
        print(f"IP not found for {url}")
