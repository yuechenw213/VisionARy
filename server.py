import socket
import sys
import os
import struct
import numpy as np

import threading

HOST = '192.168.0.7'
PORT = 50001
output = "D:/thesis/accessability/test_docs/new.obj"


def recvnb(conn, n):
    buffer = conn.recv(n)
    while len(buffer) < n:
        buffer += conn.recv(n-len(buffer))
    return buffer

# depth image connect
def tcp_server():
    dc = 0
    serverHost = '192.168.0.7' # localhost
    serverPort = 50001
    save_folder = 'data/'

    if not os.path.isdir(save_folder):
        os.mkdir(save_folder)

    # Create a socket
    sSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind server to port
    try:
        sSock.bind((serverHost, serverPort))
        print('Server bind to port '+str(serverPort))
    except socket.error as msg:
        print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
        return

    sSock.listen(10)
    print('Start listening...')

    accept = True
    while True:
        try:
            conn, addr = sSock.accept() # Blocking, wait for incoming connection
            print('Connected with ' + addr[0] + ':' + str(addr[1]))
            file = open(output, "wb")
            while True:
                # Receiving from client
                data = conn.recv(1024)
                if(len(data) > 0):
                    print(f"Received message: {len(data)}")
                    if b'd' in data:
                        if accept:
                            file.write(data.split(b'd')[1])
                            accept = False
                        else:
                            file.write(data.split(b'd')[0])
                            file.close()
                            sys.exit(0)
                    else:
                        file.write(data)

        except KeyboardInterrupt:
            sys.exit(0)
        except Exception as e:
            print("exception:", str(e))
            continue



    print('Closing socket...')
    sSock.close()


if __name__ == "__main__":
    thread1 = threading.Thread(target=tcp_server)
    thread1.start()