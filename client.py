#!/usr/bin/python

import xmlrpclib

def main():
    print "This is a client" 

    client = xmlrpclib.ServerProxy("http://localhost:8080")
    print client.add(10,20)

if __name__ == "__main__":
    main()
