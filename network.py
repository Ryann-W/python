
# python for network basic


# TCP -- transport control protocol
# IP -- internet protocol


# from the FreeCodeCamp : in computer networking, an interent socket or network socket is an endpoint of a bidirectional(双向的)
#inter-process communication flow across an internet protocol-based computer network, such as the internet

# TCP Port Numbers
# a port is an application-specific or process-specific sofrware communications endpoint
# it allows multiple networked applications to coexist on the same server

# common tcp ports

# Telent(23) --Login
# SSH(22) --Secure Login
# HTTP(80) (HyperText Transfer Protocol)
# HTTPS(443)-Secure
# SMTP(25)--Mail
# IMAP(143/220/993) -Mail Retrieval
# POP(109/110) -Mail Retrieval
# DNS(53) - Domain Name
# FTP(21) - File Transfer

# the Protocol from FreeCodeCamp

# a set of rules that all parties follow so we can predict each other's behavior
# and not bump into each other
#   On two-way roads in USA, drive on the right-hand side of the road
#   On two-way roads in the UK, drive on the left-hand side of the road

# for example, http://www.dr-churk.com/page1.htm
#            protocol       host         document
 
# note from FreeCodeCamp : Getting data from the server
# each the user clicks on an anchor tag with an href=value to switch to a new page, the browser makes a connection to the web server
# and issues a "Get" request - to GET the content of the page at the specified URL

# the server returns the HTML document to the Browser which formats and displays the document to the user

### Write a Web Browser

import socket



mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(1024)
    if len(data) < 1:
        break
    print(data.decode())
mysock.close()

# Representing Simple Strings
# the ord() function tells us the numeric value of a simple ASCII character

print(ord('H')) #return 72
print(ord('e')) #return 101
print(ord('\n')) #return 10

# UTF-8
# in Python 3 , all strings are Unicode
# reading the data encode and decode 

# String Unicode ----------------->Bytes UTF-8 ------------>socket
#                      encode()                    send()
#socket--------------------------->Bytes UTF-8 -------------->String Unicode
#           recv()                                  decode

# using urllib in Python

import urllib.request, urllib.parse, urllib.error
fanhd = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fanhd:
    print(line.decode().strip())
