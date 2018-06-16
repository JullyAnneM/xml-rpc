#!/usr/bin/python

import SimpleXMLRPCServer

def add(a,b):
    return a+b

def main ():
    print "This is a Server"
    
    server = SimpleXMLRPCServer.SimpleXMLRPCServer(("0.0.0.0", 8080))
    server.register_function(add)
    print "Pressione CTRL + C para interromper..."
    server.serve_forever()

if __name__ == "__main__":
    main()

