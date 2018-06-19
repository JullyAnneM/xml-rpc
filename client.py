#!/usr/bin/python

import xmlrpclib

def main():
    print "Esse eh o cliente!" 

    client = xmlrpclib.ServerProxy("http://localhost:8080")
    
    #variavel para metodo EnviaIntRecebeInt
    valor = int(10)

    #variaveis para metodos EnviaLongRecebeLong e EnviaLong8RecebeLong
    x = 10
    y = 20
    z = 30
    w = 40
    a = 50
    b = 60 
    c = 70
    d = 85
    print client.EnviaIntRecebeInt(valor)
    print client.EnviaLongRecebeLong(x)
    print client.EnviaLong8RecebeLong(x,y,z,w,a,b,c,d)

if __name__ == "__main__":
    main()
 
