import socket

def build_query(domain):
    transaction_id = b"\x12\x34"
    flags = b"\x01\x00"
    qdcount = b"\x00\x01"
    ancount = b"\x00\x00"
    nscount = b"\x00\x00"
    arcount = b"\x00\x00"

    header = transaction_id + flags + qdcount + ancount + nscount + arcount

    qname = b""
    for part in domain.split("."):
        qname += bytes([len(part)])
        qname += part.encode()

    qname += b"\x00"

    qtype = b"\x00\x01"
    qclass = b"\x00\x01"

    return header + qname + qtype + qclass


domains = [
    "google.com",
    "ucr.ac.cr",
    "proyecto.local"
]

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(5)

for domain in domains:
    query = build_query(domain)

    print(f"\nConsultando: {domain}")

    sock.sendto(query, ("127.0.0.1", 8053))

    try:
        response, addr = sock.recvfrom(512)

        print("Respuesta recibida")
        print(f"Servidor: {addr}")
        print(f"Tamaño: {len(response)} bytes")
        print(f"Hexadecimal: {response.hex()}")

    except socket.timeout:
        print("No se recibió respuesta")