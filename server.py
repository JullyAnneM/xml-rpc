#!/usr/bin/python

import SimpleXMLRPCServer

#Cenario onde nao passamos nenhum argumento para uma funcao Void
def VoidMetodoSemParametros():
    return None

#Cenario onde passamos um Integer e recebemos um Integer
def EnviaIntRecebeInt(x):
    valor = x + 10
    valor = int(valor)
    return valor

#Cenrio onde passamos um Long e recebemos um Long
def EnviaLongRecebeLong(x):
    valor = x + 15
    valor = long(valor)
    return valor

#Cenario onde passamos 8 variaveis Long e recebemos um Long
def EnviaLong8RecebeLong(x, y, z, w, a, b, c, d):
    valor = x + y + z + w + a + b + c + d
    valor = long(valor)
    return valor

#Cenario onde passamos strings com valor de potencias de 10 MUITO grandes e recebemos uma string com uma frase
#EnviaStringPotencia10RecebeString

def main ():
    
    server = SimpleXMLRPCServer.SimpleXMLRPCServer(("0.0.0.0", 8080))
#    server.register_function(VoidMetodoSemParametros)
    server.register_function(EnviaIntRecebeInt)
    server.register_function(EnviaLongRecebeLong)
    server.register_function(EnviaLong8RecebeLong)
    print "Pressione CTRL + C para interromper..."
    server.serve_forever()

if __name__ == "__main__":
    main()

