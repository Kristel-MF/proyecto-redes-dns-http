import socket

query = bytes.fromhex(
    "123401000001000000000000"
    "06676f6f676c6503636f6d00"
    "00010001"
)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.settimeout(5)

sock.sendto(query, ("127.0.0.1", 8053))

print("Consulta DNS enviada")

try:
    response, addr = sock.recvfrom(512)

    print("\nRespuesta recibida")
    print(f"Servidor: {addr}")
    print(f"Tamaño: {len(response)} bytes")
    print("\nHexadecimal:")
    print(response.hex())

except socket.timeout:
    print("No se recibió respuesta")