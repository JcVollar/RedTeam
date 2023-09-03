#!/usr/bin/env python

from Tools.GetHosts import getHosts 
from  Tools.LocalhostInterfaces import getInterfaces



## Finding out what to scan
local = getInterfaces()
 
hosts = getHosts(local[0]['ip']+"/24")

for host in hosts:
    print (host)