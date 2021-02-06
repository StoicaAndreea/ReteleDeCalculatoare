#set2
#1.numarul de cuvinte din lista
import socket
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0",5555))
while True:
    data,addr=s.recvfrom(100)
    list=data.split(",")
    print("Am primit "+str(data)+" de la "+str(addr))
    s.sendto(str(len(list)),addr)
    print("conexiune incheiata cu "+str(addr))