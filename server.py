import socket


TCP_IP = '0.0.0.0'
TCP_PORT = 2424
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print ('Connection address', addr)
try:
    while 1:
        data = conn.recv(BUFFER_SIZE)
        if not data: break
        print ("received data:", data)
        conn.send("Reciví: " + data)  # echo
except KeyboardInterrupt:
    print("keyboardinterrupt is caught")
    conn.close()