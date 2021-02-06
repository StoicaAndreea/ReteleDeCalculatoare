import socket
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
info=raw_input("da un sir de cuvinte, separate prin vrgula:")
s.sendto(info,("127.0.0.1",5555))
print ("Am primit de la server: "+str(s.recvfrom(10)))