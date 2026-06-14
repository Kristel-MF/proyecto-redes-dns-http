import socket
import time


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

    qtype = b"\x00\xff"  # ANY
    qclass = b"\x00\x01"

    return header + qname + qtype + qclass


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(2)

domain = "google.com"

print("Iniciando simulación de tráfico DNS anómalo...")

for i in range(10):
    query = build_query(domain)
    sock.sendto(query, ("127.0.0.1", 8053))

    try:
        sock.recvfrom(512)
    except socket.timeout:
        pass

    print(f"Consulta sospechosa enviada #{i + 1}")
    time.sleep(0.3)

print("Simulación finalizada")