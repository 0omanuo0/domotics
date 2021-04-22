# Import socket module 
import socket             
  
# Create a socket object 
s = socket.socket()         
  
# Define the port on which you want to connect 
port = 12348               
  
# connect to the server on local computer 
s.connect(('127.0.0.1', port)) 
  
# receive data from the server 
print (s.recv(1024))
s.send(b'wenas')
# close the connection 
s.close()   