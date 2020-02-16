import socket
import threading


p2p_socket = socket.socket()
host = ""
port = 9999

def send(connection = p2p_socket):
    while True:
        msg = input("Enter your message: ") + "\nEnter your message: "
        if "exitchat" in msg:
            connection.send(msg.encode("utf-8"))
            connection.close()
            return
        else:
            connection.send(msg.encode("utf-8"))

def receive(connection = p2p_socket):
    while True:
        msg = connection.recv(1024).decode("utf-8")
        if "exitchat" in msg:
            print("Exiting the connection...")
            connection.close()
            return
        else:
            print("\nPartner sent: " + msg, end= "")


def receive_connection():
    p2p_socket.bind((host, port))
    p2p_socket.listen()
    connection, connection_address = p2p_socket.accept()
    print(f"Connection received from {connection_address} on the port {port}")
    t1 = threading.Thread(target=send, args=[connection])
    t2 = threading.Thread(target=receive, args=[connection])
    t1.start()
    t2.start()
    t1.join()
    t2.join()



def send_connection():
    conn_host = input("Enter the IP of Partner: ")
    p2p_socket.bind((host, port))
    p2p_socket.connect((conn_host, port))
    print(f"Connected to {conn_host} on the port {port}")
    t1 = threading.Thread(target=send)
    t2 = threading.Thread(target=receive)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


while True:
    try:
        n = int(input("Press 1 to Send a connection\nPress 2 to receive a connection\n: "))
        if n == 1:
            send_connection()
        elif n == 2:
            receive_connection()
        else:
            print("Please enter a valid option")
    except:
        pass