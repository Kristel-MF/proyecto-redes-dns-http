import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

mensaje = b"hola servidor dns"

sock.sendto(mensaje, ("127.0.0.1", 8053))

print("Mensaje enviado correctamente")