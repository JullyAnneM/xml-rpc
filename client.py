#!/usr/bin/python

import xmlrpclib
import time
import math

def main():

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
    
    file = open("tempos_XML-RPC.txt", "w")

    for x in range(0, 50):
        arrayGrande = []
        i = int(10)
#        start_time = time.time()
#        client.VoidMetodoSemParametros()
#        end_time = time.time()
#        str_result0 = str(end_time-start_time)
#        file.write("#VoidMetodoSemParametros " + str_result0 + "\n")
    
        start_time = time.time()
        result1 = client.EnviaIntRecebeInt(valor)
        end_time = time.time()
        str_result1 = str(end_time-start_time)
        file.write("#EnviaIntRecebeInt " + str_result1 + "\n")
    
        start_time = time.time()
        result2 = client.EnviaLongRecebeLong(x)
        end_time = time.time()
        str_result2 = str(end_time-start_time)
        file.write("#EnviaLongRecebeLong " + str_result2 +"\n")
    
        start_time = time.time()
        result3 = client.EnviaLong8RecebeLong(x,y,z,w,a,b,c,d)
        end_time = time.time()
        str_result3 = str(end_time-start_time)
        file.write("#EnviaLong8RecebeLong " + str_result3 +"\n")

        
        while (i <= 100):
            x = _criaStringPotenciaDe10(i)
            start_time = time.time()
            result3 = client.EnviaStringPotencia10RecebeString(x)
            end_time = time.time()
            str_result3 = str(end_time-start_time)
            file.write("#EnviaStringPotencia10RecebeString " + str_result3 +"\n")
            i = i+10

        j = 100
        _criaArrayGrande(arrayGrande, j)
        start_time = time.time()
        result3 = client.EnviaArrayIntRecebeInt(arrayGrande)
        end_time = time.time()
        str_result3 = str(end_time-start_time)
        file.write("#EnviaArray100IntRecebeInt " + str_result3 +"\n")

        j = 100
        _criaArrayGrande(arrayGrande, j)
        start_time = time.time()
        result3 = client.EnviaArrayIntRecebeArray(arrayGrande)
        end_time = time.time()
        str_result3 = str(end_time-start_time)
        file.write("#EnviaArray100IntRecebeArray " + str_result3 +"\n")

        j = 1000
        _criaArrayGrande(arrayGrande, j)
        start_time = time.time()
        result3 = client.EnviaArrayIntRecebeInt(arrayGrande)
        end_time = time.time()
        str_result3 = str(end_time-start_time)
        file.write("#EnviaArray1000IntRecebeInt " + str_result3 +"\n")

        j = 1000
        _criaArrayGrande(arrayGrande, j)
        start_time = time.time()
        result3 = client.EnviaArrayIntRecebeArray(arrayGrande)
        end_time = time.time()
        str_result3 = str(end_time-start_time)
        file.write("#EnviaArray1000IntRecebeArray " + str_result3 +"\n")

        j = 10000
        _criaArrayGrande(arrayGrande, j)
        start_time = time.time()
        result3 = client.EnviaArrayIntRecebeInt(arrayGrande)
        end_time = time.time()
        str_result3 = str(end_time-start_time)
        file.write("#EnviaArray10000IntRecebeInt " + str_result3 +"\n")

        j = 10000
        _criaArrayGrande(arrayGrande, j)
        start_time = time.time()
        result3 = client.EnviaArrayIntRecebeArray(arrayGrande)
        end_time = time.time()
        str_result3 = str(end_time-start_time)
        file.write("#EnviaArray10000IntRecebeArray " + str_result3 +"\n")

        j = 100000
        _criaArrayGrande(arrayGrande, j)
        start_time = time.time()
        result3 = client.EnviaArrayIntRecebeInt(arrayGrande)
        end_time = time.time()
        str_result3 = str(end_time-start_time)
        file.write("#EnviaArray100000IntRecebeInt " + str_result3 +"\n")

        j = 100000
        _criaArrayGrande(arrayGrande, j)
        start_time = time.time()
        result3 = client.EnviaArrayIntRecebeArray(arrayGrande)
        end_time = time.time()
        str_result3 = str(end_time-start_time)
        file.write("#EnviaArray100000IntRecebeArray " + str_result3 +"\n")

def _criaStringPotenciaDe10(i):
    return str(math.pow(10, i))

def _criaArrayGrande(arrayGrande, j):
    for x in range(0, j):
        arrayGrande.append(x) 

if __name__ == "__main__":
    main()
 
