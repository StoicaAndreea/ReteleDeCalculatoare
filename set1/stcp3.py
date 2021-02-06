import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("0.0.0.0",7777))
s.listen(5)
cs,addr=s.accept()
b=cs.recv(10)
a=str(b)
list=['a','e','i','o','u']
i=0
j=0
for l in a:
    if l in list:
        i=i+1
    else: j=j+1
print(b,addr)
cs.send(str(j).encode())
cs.close()