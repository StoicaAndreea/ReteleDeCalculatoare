import socket
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0",5555))
data,addr=s.recvfrom(100)
list=data.split(",")
maxc=0
max=list[0]
for el in list:
    count=0
    for l in el:
        if l in ['a','e','i','o','u']:
            count=count+1
            if count>maxc:
                maxc=count
                max=el

print(data,addr)
s.sendto(str(max),addr)
