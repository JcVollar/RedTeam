import scapy.all as scapy
import socket

def getHosts (ip):
    #scapy.arping(ip)
    arpRequest = scapy.ARP(pdst = ip)
    #print(arpPack.summary())
    broadcst = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    request = broadcst/arpRequest
    (answerd, unanswerd) = scapy.srp(request, timeout=1, verbose=False);
    clients = [];
    for el in answerd:
        #print(el[1].psrc)
        #print(el[1].hwsrc)

        if el[1].psrc :
            try:
                tmp = socket.gethostbyaddr(el[1].psrc)
                host = tmp[0]
            except (socket.herror, socket.gaierror):
                host = "unknown"
        else:
            host = "unknown"
 
        clients.append({"ip":el[1].psrc, "mac":el[1].hwsrc, "host":host})
 
    return clients;

#scan("192.168.50.1/24")