import struct
import socket
from zone_reader import load_zone


def build_dns_response(query, domain_name):

    transaction_id = query[:2]

    flags = struct.pack("!H", 0x8180)

    qdcount = struct.pack("!H", 1)
    ancount = struct.pack("!H", 1)
    nscount = struct.pack("!H", 0)
    arcount = struct.pack("!H", 0)

    header = (
        transaction_id
        + flags
        + qdcount
        + ancount
        + nscount
        + arcount
    )

    question = query[12:]

    answer_name = struct.pack("!H", 0xC00C)

    answer_type = struct.pack("!H", 1)
    answer_class = struct.pack("!H", 1)

    ttl = struct.pack("!I", 60)

    rdlength = struct.pack("!H", 4)

    records = load_zone()

    ip_address = records.get(
        domain_name,
        "192.168.1.100"
    )

    ip = socket.inet_aton(ip_address)

    answer = (
        answer_name
        + answer_type
        + answer_class
        + ttl
        + rdlength
        + ip
    )

    return header + question + answer