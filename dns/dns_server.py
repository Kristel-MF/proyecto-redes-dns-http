import socket
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from parser_dns import parse_dns_header
from dns_response import build_dns_response
from detector.detector_dns import register_request

HOST = "0.0.0.0"
PORT = 8053

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print(f"Servidor DNS escuchando en UDP {PORT}...")

while True:

    data, addr = server_socket.recvfrom(512)

    print("\n================================")
    print(f"Paquete recibido desde: {addr}")
    print(f"Tamaño: {len(data)} bytes")

    domain = parse_dns_header(data)
    register_request(addr[0], domain)

    response = build_dns_response(data, domain)

    server_socket.sendto(response, addr)

    print("Respuesta DNS enviada")
    print("================================")