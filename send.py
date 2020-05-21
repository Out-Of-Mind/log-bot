import requests as r

def send_mes(url, mes, fro):
    re = r.post(url, headers={'hjk':'UPj#*mUh:1%?k@ew'}, json={'s':False, 'mes':mes, 'ss':True, 'from':fro})

def watch_host(url, host):
    re = r.post(url, headers={'hjk':'UPj#*mUh:1%?k@ew'}, json={'s':True, 'host':host, 'ss':False})