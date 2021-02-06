#set1
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    s.connect(("127.0.0.1",7777))
except:
    print("nu a putut sa se conecteze")
    quit()
s.send(raw_input("da un cuvant: "))
print("Am primit de la server: "+str(s.recv(10)))
s.close()