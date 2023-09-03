import netifaces as ni

def getInterfaces():
    interfaces = []
    for interface in ni.interfaces():
        try:
            ip = ni.ifaddresses(interface)[ni.AF_INET][0]['addr']
            netmask = ni.ifaddresses(interface)[ni.AF_INET][0]['netmask']
            if interface != "lo":
                interfaces.append({"interface": interface, "ip": ip, "netmask": netmask})
        except KeyError:
            continue
    return interfaces