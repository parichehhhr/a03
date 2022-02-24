
# the function to connect to host an server with ip  
def inp():

    import socket
    #get port from user and convert to int val
    port = int(input ("Enter port :"))
    #get  host server ip 
    host = input("Enter host : ")
    
    #port = 8888
    #host = "10.0.0.23"
    # flag to control loop connection
    flag = True
    #creating the socket
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # connecting host 
    s.connect((host, port))
    
    while (flag):
        #get a message from user
        st = input ("$ ")
        # check user input if exit to finish connection
        if(st=="exit"):
            
            s.sendall(bytes(st+ "\n", "utf-8"))
            print("exit")
            flag = False
        else:
            #send bytes from convering  string to server  in  utf-8 format
            s.sendall(bytes(st+ "\n", "utf-8"))
            # get message from serve that is 'ok' word 
            msg = s.recv(1024)
            #print it 
            print('$ ', repr(msg))
    #close socket
    s.close()


    