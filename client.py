#!/usr/bin/python

import xmlrpclib
import time

def main():
    print "Esse eh o cliente!" 

    client = xmlrpclib.ServerProxy("http://localhost:8080")
    
    #variavel para metodo EnviaIntRecebeInt
    valor = int(10)

    #variaveis para metodos EnviaLongRecebeLong e EnviaLong8RecebeLong
    x = long(10)
    y = long(20)
    z = long(30)
    w = long(40)
    a = long(50)
    b = long(60)
    c = long(70)
    d = long(85)
    
    #printa resultados e tempo de execucao
    start_time = time.time()
    result1 = client.EnviaIntRecebeInt(valor)
    end_time = time.time()
    print "EnviaIntRecebeInt resultou em:",result1,"e rodou em",end_time-start_time
    
    start_time = time.time()
    result2 = client.EnviaLongRecebeLong(x)
    end_time = time.time()
    print "EnviaLongRecebeLong resultou em:",result2,"e rodou em",end_time-start_time

    
    start_time = time.time()
    result3 = client.EnviaLong8RecebeLong(x,y,z,w,a,b,c,d)
    end_time = time.time()
    print "EnviaLong8RecebeLong resultou em:",result3,"e rodou em",end_time-start_time


if __name__ == "__main__":
    main()
 
