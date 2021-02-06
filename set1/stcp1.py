#set1
#1.Lungimea cuvantului
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("0.0.0.0",7777))
s.listen(5)
while True:
    cs,addr=s.accept()
    print("Client nou:")
    b=cs.recv(10)
    print("Am primit "+str(b)+" de la "+str(addr))
    cs.send(str(len(b)))
    cs.close()
    print("Connection ended")