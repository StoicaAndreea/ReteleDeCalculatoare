import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    s.connect(("127.0.0.1",7777))
except:
    print("nu a putut sa se conecteze")
    quit()
info=raw_input("dati o lista de numere, separata prin virgule: ")
s.send(info)
print("Am primit de la server: "+str(s.recv(10)))
s.close()