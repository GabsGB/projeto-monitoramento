import socket

def enviar_zpl(ip, comando):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip, 9100))
        s.sendall(comando.encode())

enviar_zpl("192.168.50.56", "~HS")