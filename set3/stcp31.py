#set3
#1.serverul primeste o lista de numere si 
#intoarce suma lor
import os
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("0.0.0.0",7777))
s.listen(5)
while True:
    cs,addr=s.accept()
    if os.fork() == 0:
        print("Client nou")
        b=cs.recv(50)
        sum=0
        print("Am primit "+str(b)+" de la "+str(addr))
        list=b.split(',')
        for el in list:
            sum=sum+int(el)
        cs.send(str(sum))
        cs.close()
        print("conexiune incheiata cu "+str(addr))
        os._exit(0)