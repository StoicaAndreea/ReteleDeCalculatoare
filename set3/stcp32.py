#set3
#2.serverul intoarce numarul cel mai mare din lista
import os
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("0.0.0.0",7777))
s.listen(5)
while True:
    cs,addr=s.accept()
    if os.fork() == 0:
        print("Client nou:")
        b=cs.recv(50)
        max=0
        print("Am primit: "+str(b)+"de la "+str(addr))
        list=b.split(',')
        for el in list:
            if int(el)>max:
                max=int(el)
        cs.send(str(max))
        cs.close()
        print("Conexiune incheiata cu: "+str(addr))
        os._exit(0)
s.close()