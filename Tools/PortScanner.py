import nmap
   
def portScanner(ip, fromPorts, toPorts):   
    # take the range of ports to 
    # be scanned
    begin = 10
    end = 80
     
    # instantiate a PortScanner object
    scanner = nmap.PortScanner()
    
    for i in range(fromPorts,toPorts+1):
    
        # scan the target port
        res = scanner.scan(ip,str(i))
    
        # the result is a dictionary containing 
        # several information we only need to
        # check if the port is opened or closed
        # so we will access only that information 
        # in the dictionary
        res = res['scan'][ip]['tcp'][i]['state']
    
        print(f'port {i} is {res}.')