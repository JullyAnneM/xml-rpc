#!/usr/bin/python

import SimpleXMLRPCServer

#Cenario onde nao passamos nenhum argumento para uma funcao Void
def VoidMetodoSemParametros():
    return None

#Cenario onde passamos um Integer e recebemos um Integer
def EnviaIntRecebeInt(x):
    valor = int(x)
    return valor

#Cenrio onde passamos um Long e recebemos um Long
def EnviaLongRecebeLong(x):
    valor = long(x)
    return x

#Cenario onde passamos 8 variaveis Long e recebemos um Long
def EnviaLong8RecebeLong(x, y, z, w, a, b, c, d):
    valor = long(x)
    return x

#Cenario onde passamos strings com valor de potencias de 10 MUITO grandes e recebemos uma string com uma frase
def EnviaStringPotencia10RecebeString(i):
    return str(i)

def EnviaArrayIntRecebeInt(dicionario):
    return int(0)

def EnviaArrayIntRecebeArray(dicionario):
    return dicionario

def main ():
    
    server = SimpleXMLRPCServer.SimpleXMLRPCServer(("0.0.0.0", 8080))
    server.register_function(EnviaIntRecebeInt)
    server.register_function(EnviaLongRecebeLong)
    server.register_function(EnviaLong8RecebeLong)
    server.register_function(EnviaStringPotencia10RecebeString)
    server.register_function(EnviaArrayIntRecebeInt)
    server.register_function(EnviaArrayIntRecebeArray)
    print "Pressione CTRL + C para interromper..."
    server.serve_forever()

if __name__ == "__main__":
    main()

